from opnsense_helper.classes import Opnsense_Helper
output="./config.xml"
conf_path="/conf/config.xml"
host= "192.168.1.103"
def using_api():
    vlans_api=[
    {'if': 'vtnet1', 'tag': '1', 'pcp': '0', 'proto': None, 'descr': 'vlan1', 'vlanif': 'vlan0.1'},
    {'if': 'vtnet1', 'tag': '2', 'pcp': '0', 'proto': None, 'descr': 'vlan2', 'vlanif': 'vlan0.2'}
    ]
    api_auth={
    "api_key" :'ejl4fIU9yfNk+gaQmPk/rqIa15f1yX1snIKgcIEl2QNoJwhbekraWIE0ANRYceh9hey5IFGzlf3da4yJ',
    "api_secret":'5JVVGoatPbaAA+FozLDQY92/T6sRlmKD1+aRNl/YI8KA9/0TNiTDboLveqvd9FU8wFeDo3D3DY5wrUtF',
    "ssl": True,
    "verify": False
    }    
    helper=Opnsense_Helper(host=host,api_auth=api_auth,filepath=output, verbose=False)
    helper.vlans_api(vlans_api,"add")

def backend():
    vlans=[
    {"id":"vlan1",'parent': 'vtnet1', 'tag': '1', 'pcp': '0', 'proto': None, 'descr': 'vlan1', 'vlanif': 'vlan0.1'},
    {"id":"vlan2",'parent': 'vtnet1', 'tag': '2', 'pcp': '0', 'proto': None, 'descr': 'vlan2', 'vlanif': 'vlan0.2'},
    {"id":"vlan3",'parent': 'vtnet1', 'tag': '3', 'pcp': '0', 'proto': None, 'descr': 'vlan3', 'vlanif': 'vlan0.3'}

    ]
    dhcp=[
    {"id":"opt2",'enable': '1', 'ddnsdomainalgorithm': 'hmac-md', "range":{'from': '200.0.3.10', '_to': '200.0.3.100'}},
    {"id":"opt3",'enable': '1', 'ddnsdomainalgorithm': 'hmac-md', "range":{'from': '200.0.4.10', '_to': '200.0.4.100'}}
    ]
    interfaces=[
    {"id":"opt1",'descr': 'router', 'enable': '1', 'ipaddr': None, 'subnet': None, 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:02:01',"interface":"vtnet1"},
    {"id":"opt2",'descr': 'vlan1', 'enable': '1', 'ipaddr': '200.0.3.1', 'subnet': '24', 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:00:01',"interface":"vlan0.1"},
    {"id":"opt3",'descr': 'vlan2', 'enable': '1', 'ipaddr': '200.0.4.1', 'subnet': '24', 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:00:02', "interface":"vlan0.2"},
    {"id":"opt4",'descr': 'vlan3', 'enable': '1', 'ipaddr': '200.0.5.1', 'subnet': '24', 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:00:03', "interface":"vlan0.3"}

    ]
    auth={
    "user":"root",
    "passw":"opnsense",
    }
    helper=Opnsense_Helper(host=host,ssh_auth=auth,filepath=output, verbose=False)
    #helper.set_vlans(vlans)
    helper.get_conf(conf_path)
    helper.initialize()
    helper.add_Items("interfaces",interfaces)
    helper.add_Items("dhcpd",dhcp)
    helper.add_Items("vlans",vlans)
    helper.save(output)
    helper.put_file(output,conf_path)
    helper.close_con()   
if __name__ == "__main__":
    backend()