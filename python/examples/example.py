from opnsense_helper.classes import Opnsense_Helper, Vlan, Dhcpd, Interface
temp_path="./config.xml"
host= "192.168.1.103"
def backend():
    vlans=[
    Vlan("vlan1","vtnet1","1"),
    Vlan("vlan2","vtnet1","2"),
    Vlan("vlan3","vtnet1","3")
    ]

    interfaces=[
    Interface("opt1","router","vtnet1","1","200.1.0.1","24"),
    Interface("opt2","vlan1","vlan0.1", "1", '200.0.1.1', "24", '00:00:00:01:00:01'),
    Interface("opt3","vlan2","vlan0.2", "2", '200.0.2.1', "24", '00:00:00:01:00:02'),
    Interface("opt4","vlan3","vlan0.3", "3", '200.0.3.1', "24", '00:00:00:01:00:03'),
    ]
    
    dhcp=[
    Dhcpd("opt1","1",{'from': '200.1.0.2', '_to': '200.1.0.2'}),
    Dhcpd("opt2","1",{'from': '200.0.1.1', '_to': '200.0.1.100'}),
    Dhcpd("opt3","1",{'from': '200.0.2.1', '_to': '200.0.2.100'}),
    Dhcpd("opt4","1",{'from': '200.0.3.1', '_to': '200.0.3.100'}),
    ]
    
    auth={
    "user":"root",
    "passw":"opnsense",
    }
    
    helper=Opnsense_Helper(host=host,ssh_auth=auth,temp_path=temp_path, init=True)
    helper.set("interfaces",interfaces)
    helper.set("dhcpd",dhcp)
    helper.set("vlans",vlans)
    helper.save(temp_path)
    # helper.remove_items()




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

    helper=Opnsense_Helper(host=host,api_auth=api_auth,filepath=temp_path, verbose=False)
    helper.vlans_api(vlans_api,"add")


if __name__ == "__main__":
    backend()