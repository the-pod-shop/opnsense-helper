from opnsense_helper.classes import Opnsense_Helper

filepath = '/home/ji/confignew.xml'
output="./config.xml"
conf_path="/conf/config.xml"
vlans=[
    {'if': 'vtnet1', 'tag': '1', 'pcp': '0', 'proto': None, 'descr': 'vlan1', 'vlanif': 'vlan0.1'},
    {'if': 'vtnet1', 'tag': '2', 'pcp': '0', 'proto': None, 'descr': 'vlan2', 'vlanif': 'vlan0.2'}
    ]
dhcp={
"opt2": {'enable': '1', 'ddnsdomainalgorithm': 'hmac-md', "range":{'from': '200.0.3.10', '_to': '200.0.3.100'}},
"opt3": {'enable': '1', 'ddnsdomainalgorithm': 'hmac-md', "range":{'from': '200.0.4.10', '_to': '200.0.4.100'}}
}
interfaces={
"opt1": {'descr': 'router', 'enable': '1', 'ipaddr': None, 'subnet': None, 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:02:01',"interface":"vtnet1"},
"opt2": {'descr': 'vlan1', 'enable': '1', 'ipaddr': '200.0.3.1', 'subnet': '24', 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:00:01',"interface":"vlan0.1"},
"opt3": {'descr': 'vlan2', 'enable': '1', 'ipaddr': '200.0.4.1', 'subnet': '24', 'type': None, 'virtual': None, 'spoofmac': '00:00:00:00:00:02', "interface":"vlan0.2"}
}

ssh_auth={
"user":"root",
"passw":"opnsense",
}
api_auth={
# ONLY NEED WHEN YOU USE THE API
"api_key" :'ejl4fIU9yfNk+gaQmPk/rqIa15f1yX1snIKgcIEl2QNoJwhbekraWIE0ANRYceh9hey5IFGzlf3da4yJ',
"api_secret" : '5JVVGoatPbaAA+FozLDQY92/T6sRlmKD1+aRNl/YI8KA9/0TNiTDboLveqvd9FU8wFeDo3D3DY5wrUtF',
"ssl": True,
"verify": False
}
host= "192.168.1.103"
def test():
    helper=Opnsense_Helper(host=host,ssh_auth=ssh_auth,api_auth=api_auth,filepath=output, verbose=False)
    helper.add_vlans(vlans)
    #helper.set_vlans(vlans)
    helper.get_conf(conf_path)
    helper.initialize()
    helper.add_Items("interfaces",interfaces)
    helper.add_Items("dhcpd",dhcp)
    helper.save(output)
    helper.put_file(output,conf_path)
    helper.close_con()
    
if __name__ == "__main__":
    test()