# opnsense-helper
assign lan interfaces, create vlans, vlan-interfaces and setup dhcp in a single script.


## install 
## pip
```bash
pip install opnsense-helper
```

## usage
- before you create Vlan-Interfaces you need to add them first using the add_vlan method
- you can also add them via config file but this requires a reboot and it's not yet implemented
  
### python 

- import and create object
```python
from  opnsense_helper.opnsense_helper import OpennsenseHelper
helper=OpennsenseHelper(filepath,True,"root","opnsense","192.168.1.103")
```
- add some vars we need later
```python
filepath = '/home/ji/confignew.xml'
output="/home/ji/.ansible/collections/ansible_collections/ji_podhead/podnet/plugins/x.xml"
conf_path="/conf/config.xml"

# the variables of the things we will modif
# opnsense-helper
assign lan interfaces, create vlans, vlan-interfaces and setup dhcp in a single script.


## install 
## pip
```bash
pip install opnsense-helper
```

## usage
- before you create Vlan-Interfaces you need to add them first using the add_vlan method
- you can also add them via config file but this requires a reboot and it's not yet implemented
  

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
