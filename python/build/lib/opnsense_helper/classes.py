
import paramiko
from lxml import etree
import xml.etree.ElementTree as ET
import logging
from xmldiff import main, formatting
from opnsense_helper.utils import parseChild, update_xml_file, aliases, reconfigure_vlans
from opnsense_helper.frontend_utils import api_get,api_post

{"id":"router",'descr': 'router', 'enable': '1', 'ipaddr': '200.1.0.1','spoofmac': '00:00:00:01:00:01',"interface":"vtnet1"},

class Interface:
    """
    ***Creates a Interface object.***
    The ID is the technical identifier. 
    This is required and you need to find out which "opt" to use, 
    because rn there is no function that provides that.
    The interface key in the xml are the identifiers, in this case the class id`s.
    Im not sure if they have a certain naming convention 

    *Required params(man. usage):*
    * id: str
    * interface: str
    * enable: str
    * descr: str
    
    *Defaults:*
    * subnet: 32
    * ipaddr: None
    * spoofmac: None 
    
    """
    def __init__(self, id=None, descr =None, interface=None, enable=None, ipaddr=None, subnet="32", spoofmac=None):
        self.id=id
        self.interface=interface
        self.enable=enable
        self.subnet=subnet
        self.ipaddr=ipaddr
        self.spoofmac=spoofmac
        self.descr=descr
        self.descr= descr #if descr is not None else id if id is not None else None
        self.attr={}
    def initialize(self, parent):

        self.descr = parseChild(parent, "descr")
        self.interface = parseChild(parent, "if")
        self.enable = parseChild(parent, "enable")
        self.ipaddr = parseChild(parent, "ipaddr")
        self.subnet = parseChild(parent, "subnet")
        self.type = parseChild(parent, "type")
        self.virtual = parseChild(parent, "virtual")
        self.spoofmac=parseChild(parent, "spoofmac")
        
class Vlan:
    """
    ***Creates a vlan object.***

    *Required params(man. usage):*
    * id: str
    * tag: str
    
    *Defaults:*
    * pcp: 0 
    * descr: id
    * vlanif: "vlan0."+tag 
    """  
    def __init__(self, id=None, parentinterface=None, tag=None,  vlanif= None, pcp= '0', descr=None ):
        self.id=id
        self.parentinterface=parentinterface 
        self.pcp = pcp
        self.tag=tag
        self.descr= descr if descr is not None else id if id is not None else None 
        self.vlanif= vlanif if vlanif is not None else "vlan0."+str(tag) if tag is not None else None
        self.attr={}
    def initialize(self,parent):
        self.parentinterface =parseChild(parent, "if")
        self.tag = parseChild(parent,"tag")
        self.pcp = parseChild(parent,"pcp")
        self.proto = parseChild(parent,"proto")
        self.descr = parseChild(parent,"descr")
        self.vlanif = parseChild(parent,"vlanif")
        

class Dhcpd:
    """
    ***Creates a dhcp object.***

    *Required params(man. usage):*
    * id: str
    * enable: str
    * range: dict{_from:str,_to:str}
    
    *Defaults:*
    * ddnsdomainalgorithm: "hmac-md"
    """  
    def __init__(self,id=None,enable=None,range=None,ddnsdomainalgorithm="hmac-md"):
        self.id=id
        self.enable=enable
        self._range=range
        self.ddnsdomainalgorithm=ddnsdomainalgorithm
        self.attr={}
    def initialize(self, parent):
        self.enable = parseChild(parent, "enable")
        self.ddnsdomainalgorithm = parseChild(parent, "ddnsdomainalgorithm")
        self._range={
        "_from": parent.find("range/from"),
        "_to":parent.find("range/to")
        }
        if self._range["_from"] is not None:
            self._range["_from"]=self._range["_from"].text
            self._range["_to"]=self._range["_to"].text

class Opnsense_Helper():
    def __init__(self, host=None, ssh_auth=None, api_auth=None, conf_path="/conf/config.xml", temp_path="./config.xml", verbose=False, init=True):
        if(verbose):
            self.logging=logging.basicConfig(level=logging.DEBUG)
        self.objects={
        "vlans":{},
        "dhcpd":{},
        "interfaces":{}
        }
        self.url = host
        self.conf_path=conf_path

        if(ssh_auth!=None):
            self.temp_path= temp_path
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(host, username=ssh_auth["user"], password=ssh_auth["passw"])
            self.sftp = self.ssh.open_sftp() 
            
        if(api_auth!=None):
            self.api_key = api_auth["api_key"]
            self.api_secret = api_auth["api_secret"]
            self.ssl=api_auth["ssl"]
            self.verify=api_auth["verify"]
            self.host=host
        if init:
            self.get_conf()
            self.initialize() 

    def close(self):
       self.close_con()

    def get_dif(self):

        diff = main.diff_files('file1.xml', 'file2.xml', formatter=formatting.XMLFormatter())
    def initialize(self):
        """
        Initialize the configuration.

        This method reads the configuration from the in-memory configuration. 
        The configuration is read from the
        remote host via the SSH protocol or the opnsense API.
        Either run get_backup() or get_conf() before calling this method.
        This method is not called automatically when the class is instantiated, so you need to get the conf file before and then call this method.

        """
        self.get_all("dhcpd")
        self.get_all("vlans")
        self.get_all("interfaces")

    def save(self,output,put=True):
        output= output if output is not None else self.temp_path
        """
        Save the current configuration to a file.

        This method takes the current in-memory configuration and saves it to a
        file specified by the output parameter. The file is written in XML
        format.

        Parameters
        ----------
        output : str
            The path to the file to which the configuration should be written.
            default: self.temp_path
        put: bool
            Automatically copies the configuration to the firewall
        """
        if len(self.objects["dhcpd"]) > 0:
            print("saving dhcpd")
            update_xml_file(self.objects["dhcpd"],self.root,"dhcpd")
        if len(self.objects["interfaces"]) > 0:
            
            print("saving ifs")
            update_xml_file(self.objects["interfaces"],self.root,"interfaces")
        if len(self.objects["vlans"]) > 0:
            print("saving vlans")
            update_xml_file(self.objects["vlans"],self.root,"vlans")
        with open(output, 'w') as f:
            f.write(ET.tostring(self.root, encoding='unicode', method='xml'))
        print(self.objects)
        if(put==True):
            self.put_file()

    def get_all(self,element):
        """
        Get all objects of a given type from the in-memory xml data.

        This method returns a dictionary containing all objects of this type. The dictionary keys are the tags
        of the elements, and the values are dictionaries containing the
        attributes and subelements of the elements.

        Parameters
        ----------
        element : str
            The type of the objects to retrieve. Can be "dhcpd", "interfaces",
            or "vlans".

        Returns
        -------
        dict
            A dictionary containing all objects of the given type.
        """
        print(f'''          -----------------------------
                    {element}''')
        for parent in self.root.findall(element):
            for child in parent:

                if element== "dhcpd":
                        child_object = Dhcpd()
                        
                elif element== "interfaces":
                        child_object = Interface()
                elif element== "vlans":
                        child_object = Vlan()
                
                if element != "vlans": 
                    name = child.tag
                else:
                     name = child_object.descr

                child_object.initialize(child)
                del child_object.id
                child_object.attr=child.attrib if child.attrib is not None else {}
                print(child_object.attr) 
                self.objects[element][name]=child_object.__dict__
                print(f'''found {child.tag} : {child_object.__dict__}''')
        return(self.objects[element])
    
    def close_con(self):
        self.sftp.close()
        self.ssh.close()

    def put_file(self, _from=None,_to=None):    
        """
        Apply the configuration.
        Transfer a file from the local host to the remote host.

        Parameters
        ----------
        _from : str
            The path to the file on the local host.
            default: self.temp_path
        _to : str
            The destination path on the remote host where the file should be stored.
            default: self.conf_path
        """
        a=_from if _from is not None else self.temp_path
        b=_to if _to is not None  else self.conf_path
        self.sftp.put(a, b)
        if len(self.objects["vlans"]) > 0:
            reconfigure_vlans(self)

    def remove_items(self,type, items, init=True, apply=True):
        if init:
            self.get_conf()
            self.initialize() 
        for id in items:
            self.objects[type].pop(id)
        if apply:
            self.save()
            self.put_file()

    def get_item(self,type,item):
        o = self.objects[type][item]
        if o:
            o=o.__dict__.pop("attr")
            print(f"""recieved item of type{type}
            {o}""")
            return o
        else:
            return  print(f"{item} not found")

    def set(self,type, data):
        """
        Set objects of a given type to the in-memory xml data.

        This method adds all objects given in the data parameter to the in-memory
        xml data. The objects are stored in the self.objects dictionary.

        Parameters
        ----------
        type : str
            The type of the objects to add. Can be "dhcpd", "interfaces",
            or "vlans".

        data : dict
            A dictionary containing the objects to add. The keys are the tags of
            the elements, and the values are dictionaries containing the
            attributes and subelements of the elements.

        Returns
        -------
        None
        """
        for value in data:
            id=value.id
            del value.id
            self.objects[type][id] = value.__dict__


    def get_conf(self,_from= None,_to=None):
        """
        Get the config file from the remote host and save it to a file.

        Parameters
        ----------
        _from : str
            The path to the file on the remote host.
        _to : str
            The path to the file on the local host. If None, the file is saved
            to the location specified in self.temp_path.
        """
        _to = self.temp_path if _to is None else _to
        _from=self.conf_path if _from is None else _from
        self.sftp.get(_from,_to)
        self.tree = ET.parse(_to)
        self.root = self.tree.getroot()
















# deprecated
    def get_backup(self,output=None):
        """
        this function is currently deprecated
        it was used to get the config file using the api
        i left it in however if someone wants to fetch a certain backup 
        i need to implement the backup selection though
        """
        command = 'core/backup/download/this'
        backup=api_get(self,command)
        self.root=backup
        print(ET.tostring(backup, encoding='unicode'))
        # if output != None:
        #     path=output
        # else:
        #     path = self.temp_path
        # with open(path, 'w') as f:
        #     f.write(ET.tostring(backup, encoding='unicode', method='xml'))


# deprecated
    def vlans_api(self,vlans, command="add"):
        if command == "add":
            for value in vlans:
                print("---------add vlan-----------------")
                print(value)
                payload={"vlan":value}
                r=api_post(self,"interfaces/vlan_settings/addItem",payload)
                print(r)
                r=api_post(self,"interfaces/vlan_settings/reconfigure",{})
                print(r)
        elif command == "set":
            for value in vlans:
                    print("---------set vlan-----------------")
                    payload={"vlan":value}
                    r=api_post(self,"interfaces/vlan_settings/set",payload)
                    print(r)
    