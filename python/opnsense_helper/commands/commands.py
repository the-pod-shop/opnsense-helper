from opnsense_helper.utils.exec_class import Exec_Class
class Commands():
    """
    Class Commands
    --------------

    Initialize the Commands class.
    * its just a wrapper for the pluginctl, configctl and reconfigure classes.

    **Parameters**

    base : Base_Class 
        * The parent object containing the needed ssh connection and the temp path to the config.xml.

    **Returns**

    * None
    """
    def __init__(self,base):

        self.reconfigure=reconfigure(base)
        self.configctl=configctl(base)
        self.pluginctl=pluginctl(base)
class reconfigure(Exec_Class):
    """
    Class reconfigure
    ----------------
    
    * Initialize the reconfigure class.
    * Inherits from the Exec_Class class.
    
    **Usage**
    .. code-block:: python
        Commands.reconfigure.run(<command>,<argument>,<flags>)

    **Parameters**
    base : Base_Class instance
        The parent object containing necessary SSH connection details and
        configuration settings. If provided, its attributes will be copied
        to this instance.

    **Attributes**
    commands : dict
        A dictionary of command configurations with keys for 'vlans' and 'interfaces',
        each containing command details such as the command string, arguments, 
        and flags.
    
    """
    def __init__(self, base):

        print(base.__dict__)
        super(Exec_Class).__init__()
        if base is not None:
            self.__dict__.update(base.__dict__)

        self.commands={
        "vlans": {"command":'/usr/local/opnsense/scripts/interfaces/reconfigure_vlans.php',"argument":None,"flags":[]},
        "interfaces": {"command":"configctl interface reconfigure", "flags":[] }
}

class configctl(Exec_Class):
    def __init__(self, base):
        super(Exec_Class).__init__()
        if base is not None:
            self.__dict__.update(base.__dict__)

        self.commands={
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
class pluginctl(Exec_Class):
    def __init__(self, base):
            super(Exec_Class).__init__()
            if base is not None:
                self.__dict__.update(base.__dict__)

            self.commands={
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