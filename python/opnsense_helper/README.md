# opnsense-helper
assign lan interfaces, create vlans, vlan-interfaces and setup dhcp in a single script using the opnsense backend.
## install 
## pip
```bash
pip install opnsense-helper
```
## usage
- before you create Vlan-Interfaces you need to add them first using the add_vlan method
- rn i try to find out how to reconfigure the vlans using the backend, but this is on todo list
  
```python
ffrom opnsense_helper.classes import Opnsense_Helper
output="./config.xml"
conf_path="/conf/config.xml"
host= "192.168.1.103"
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
```

### Frontend Api
```python 
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
```
### Variables
#### Opnsense_Helper 
(host=host,ssh_auth=auth,filepath=output, verbose=False)
| var | type | description |
| --- | --- | --- | 
| host| str | ip or hostname |
| auth | dict {user: str, passw: str} | SSH authentication dictionary |



#### Module Args
| var | type | elements |
| --- | --- | --- | 
| vlans | list[dict] | {id: str, parent: str, tag: int, pcp: str, proto: str } | None, descr: str, vlanif: str} |
| interfaces | list[dict] |  {id: str, descr: str, enable: int, ipaddr: str, subnet: str, type: str,  virtual: bool,  spoofmac: str, interface: str} |
| dhcp | list[dict] | {id: str, enable: str, ddnsdomainalgorithm: str, range: {from: str, _to: str}} |

## roadmap
- add routes
- firewall roules

### contribute
- clone, or fork `git@github.com:the-pod-shop/opnsense-helper.git`
- build when made changes
- make sure to use the right user
```bash
cd python
python setup.py bdist_wheel \
&& pip install --upgrade . \
&& python3 -m pip install --upgrade build #--force 
```
- you can also use the build.sh script
- create pull request

## motivation
- i couldnt find a single repo/collection/terraform provider/api that let me assign and enable lan interfaces
- i decided to create one mself
- opnsense api does not let me do it, it just replies with: controller not found
- but /conf/config.xml has the answer.
- however for phisical interfaces its the god damn conf.rc
- my opnsense runs in a vm, so it really doesnt matter for me
- i just add the interfaces via libvirt and all i need to do is to enable them, given the /conf/config.xml method
xml has the answer.
- however for phisical interfaces its the god damn conf.rc
- my opnsense runs in a vm, so it really doesnt matter for me
- i just add the interfaces via libvirt and all i need to do is to enable them, given the /conf/config.xml method