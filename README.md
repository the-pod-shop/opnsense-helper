# opnsense-helper
assign lan interfaces, create vlans, vlan-interfaces and setup dhcp in a single script.

- i couldnt find a single repo/collection/terraform provider/api that let me assign and enable lan interfaces
- i decided to create one mself
- opnsense api does not let me do it, it just replies with: controller not found
- but /conf/config.xml has the answer.
- however for phisical interfaces its the god damn conf.rc
- my opnsense runs in a vm, so it really doesnt matter for me
- i just add the interfaces via libvirt and all i need to do is to enable them, given the /conf/config.xml method

### copy tjhe config file to your machine
```bash
scp root@192.168.1.103:/conf/config.xml /home/user/confignew.xml && chmod +x /home/user/confignew.xml &&  chown user:user /home/user/confignew.xml
```
### replace the original file
```bash
scp /home/user/config.xml root@192.168.1.103:/conf/config.xml
```
