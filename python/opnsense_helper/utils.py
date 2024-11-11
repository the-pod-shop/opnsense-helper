import xml.etree.ElementTree as ET
# import libraries
import json
import xml.etree.ElementTree as ET
import requests
import os
reconfigure={
    "vlans": {"command":'/usr/local/opnsense/scripts/interfaces/reconfigure_vlans.php'},
    "interfaces": {"command":"configctl interface reconfigure", "flags":[] }
}
configctl={
#    optional arguments:
#   -h, --help  show this help message and exit
#   -m          execute multiple arguments at once
#   -e          use as event handler, execute command on receiving input
#   -d          detach the execution of the command and return immediately
#   -q          run quietly by muting standard output
#   -w W        wait specified amount of seconds for socket to become available
#   -t T        threshold between events, wait this interval before executing commands, combine input into single events
"auth":{"command":"configctl auth", "argument":None,"flags":[]},
"captiveportal":{"command":"configctl captiveportal", "argument":None,"flags":[]},
"configd":{"command":"configctl configd", "argument":None,"flags":[]},
"cron":{"command":"configctl cron", "argument":None,"flags":[]},
"dhcpd":{"command":"configctl dhcpd", "argument":None,"flags":[]},
"dhcpd6":{"command":"configctl dhcpd6", "argument":None,"flags":[]},
"dns":{"command":"configctl dns", "argument":None,"flags":[]},
"filter":{"command":"configctl filter", "argument":None,"flags":[]},
"firmware":{"command":"configctl firmware", "argument":None,"flags":[]},
"health":{"command":"configctl health", "argument":None,"flags":[]},
"ids":{"command":"configctl ids", "argument":None,"flags":[]},
"interface":{"command":"configctl interface", "argument":None,"flags":[]},
"ipfw":{"command":"configctl ipfw", "argument":None,"flags":[]},
"ipsec":{"command":"configctl ipsec", "argument":None,"flags":[]},
"kea":{"command":"configctl kea", "argument":None,"flags":[]},
"monit":{"command":"configctl monit", "argument":None,"flags":[]},
"netflow":{"command":"configctl netflow", "argument":None,"flags":[]},
"openssh":{"command":"configctl openssh", "argument":None,"flags":[]},
"openvpn":{"command":"configctl openvpn", "argument":None,"flags":[]},
"syslog":{"command":"configctl syslog", "argument":None,"flags":[]},
"system":{"command":"configctl system", "argument":None,"flags":[]},
"template":{"command":"configctl template", "argument":None,"flags":[]},
"unbound":{"command":"configctl unbound", "argument":None,"flags":[]},
"webgui":{"command":"configctl webgui", "argument":None,"flags":[]},
"wireguard":{"command":"configctl wireguard", "argument":None,"flags":[]},
"zfs":{"command":"configctl zfs", "argument":None,"flags":[]},
}
pluginctl={
        #  -4 IPv4 address mode, return primary address of interface
        # -c configure mode (default), executes plugin [_configure] hook
        # -D ifconfig mode, lists available devices
        # -d device mode, lists registered devices
        # -f flush config property (raw, e.g. system.firmware.plugins)
        # -g get config property (raw, e.g. system.firmware.plugins)
        # -h show this help text and exit
        # -I information mode, lists registered device statistics
        # -i invoke dynamic interface registration
        # -r run mode (e.g. command)
        # -S service metadata dump
        # -s service mode (e.g. myservice restart)
    "ipv4":{"argument":None,"command":"pluginctl -4"},
    "config":{"argument":None, "flags":[],"command":"pluginctl -c"},
    "ifconfig":{"argument":None,"command":"pluginctl -D"},
    "device_info":{"argument":None,"command":"pluginctl -d"},
    "flush":{"argument":None,"command":"pluginctl -f"},
    "get":{"argument":None, "flags":[],"command":"pluginctl -g"},
    "info":{"argument":None, "flags":[],"command":"pluginctl -I" },
    "if_reg":{"argument":None,"command":"pluginctl -i"},
    "run":{"argument":None,"command":"pluginctl -r"},
    "service_dump":{"argument":None,"command":"pluginctl -S"},
    "service":{"argument":None, "flags":[],"command":"pluginctl -s"} # stop start resta, rt
}
aliases={
"parent": "if",
"_from":"from",
"_to":"to",
"interface":"if",
"_range":"range"
}

def parseChild(child, tag):
        result=child.find(tag)
        element=result.text if  result is not None else None
        return element

def ping(helper):
    response = os.system(f"ping -c 1 {helper.host}")
    if response == 0:
        print(f"IP {helper.host} is reachable")
        return 0
    else: return 1
def format_flags(flags_array):
    return ' '.join(map(str, flags_array))
def exec(helper, obj):
    flags= format_flags[obj["flags"]] if obj["flags"] is not [] else "" 
    stdin, stdout, stderr = helper.ssh.exec_command(f"""{obj["command"]} {obj["argument"]if obj["argument"] is not None else ""} {flags}""")
    output = stdout.read().decode('utf-8')
    print(output)
    error = stderr.read().decode('utf-8')
    if error:
        print(f"Fehler: {error}")


def get_element(root,id, obj):
    for x in root.findall(id):
        for key in obj.__dict__.keys():
#            if isinstance(obj.__dict__[key], dict):
            if(key!="_to"and key!="_from"):
                
                if key in aliases.keys():
                    key2 = aliases[key] 
                    y=parseChild(x, key2)
                else:
                    y=parseChild(x, key)
                setattr(obj, key, y)
    return obj

def recoursion(e, value):
    for key2, value2 in value.items():
        if(key2!="attr"):
            if key2 in aliases.keys():
                key2 = aliases[key2] 
            x=ET.SubElement(e, key2)
            if isinstance(value2, dict):
                recoursion(x,value2)
            else:
                x.text = value2

def update_xml_file(objects,root,type):
    el = root.find(type)
    el.clear()
    for key, value in objects.items():
        if(type=="vlans"):
            key="vlan"
        if value["attr"] is not {}:
             e = ET.SubElement(el, key,value["attr"])
        else:
            e=ET.SubElement(el,key)
        recoursion(e,value)

# deprecated due to a logic fail
def get_child(root,element, id, keys):
    elements=[]
    for parent in root.findall(element):
        child= {}
        for y in keys:
            child[y]=None
        for x in parent.findall(id):
            for key in keys:
                child[key]=parseChild(x, key)
        elements.append(child)
    return elements

def replace(item):
    Data = {}
    #data='{"vlan": {"descr": "example2", "if": "vtnet1", "tag": 110, "pcp": 0, "vlanif": "vlan0.110"}}'
    for key, value in item.items():
        if key in aliases.keys():
            Data[aliases[key]] = value
        else:
            Data[key] = value 
    return Data
