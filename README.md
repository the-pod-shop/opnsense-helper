# opnsense-helper
- assign and enable lan / phy interfaces! - ***Not enabled in the opnsense api***
- create vlans, vlan-interfaces - ***Not enabled in the opnsense api***
- setup dhcp
- uses the opnsense backend via shh - ***much faster than the frontend api!!!***
 
## Some of the docs are currently outdated

## install 
## pip
```bash
pip install opnsense-helper
```
## usage
> you can run the provided snippets directly by pulling the [example file](https://github.com/the-pod-shop/opnsense-helper/blob/main/python/examples/add_vlans.py)
* import the package and define the needed variables for the main class

```python
from opnsense_helper.classes import Opnsense_Helper

host= "192.168.1.103"
auth={
"user":"root",
"passw":"opnsense",
}
temp_path="./config.xml"
helper=Opnsense_Helper(host=host,ssh_auth=auth,temp_path=temp_path, init=True)
```
- create the objects of the modules you want to set
```python
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
```
- assign the config
```python
helper.set("interfaces",interfaces)
helper.set("dhcpd",dhcp)
helper.set("vlans",vlans)
helper.save(temp_path)
#helper.remove_items()
```

### Frontend Api
- you can download the config.xml and add vlans via api
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
| var | type | description |
| --- | --- | --- | 
| host| str | ip or hostname |
| auth | dict {user: str, passw: str} | SSH authentication dictionary |
| filepath | str | temp path required to copy the updated xml |
| verbose | bool | debug frontend api calls |



#### Module Args
| var | type | elements |
| --- | --- | --- | 
| vlans | list[dict] | {id: str, parent: str, tag: int, pcp: str, proto: str } | None, descr: str, vlanif: str} |
| interfaces | list[dict] |  {id: str, descr: str, enable: int, ipaddr: str, subnet: str, type: str,  virtual: bool,  spoofmac: str, interface: str} |
| dhcp | list[dict] | {id: str, enable: str, ddnsdomainalgorithm: str, range: {from: str, _to: str}} |

#### Manual steps

* pull the config.xml from the firewall via ssh

```python
helper.get_conf(conf_path)
```

* initialize the the Opnsense_Helper-class and parse the config.xml
```python
helper.initialize()
```
- add the items
```python
helper.add_Items("vlans",vlans)
```

* save the configuration as xml and copy it back to the firewall
> this will also reconfigure your vlans for you, if you have any 
```python
helper.save(output)
helper.put_file(output,conf_path)
helper.close_con()   
```


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
