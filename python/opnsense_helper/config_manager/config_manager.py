
import xml.etree.ElementTree as ET
from xmldiff import main, formatting
from  opnsense_helper.utils.utils import parseChild, update_xml_file
class Interface:
    """
    class Interface
    --------------

    Creates a Interface object
    The ID is the technical identifier. 
    This is required and you need to find out which "opt" to use, 
    because rn there is no function that provides that.
    The interface key in the xml are the identifiers, in this case the class id`s.
    Im not sure if they have a certain naming convention 
    
    **Usage**

        .. code-block:: python
        
        
            from opnsense_helper.config_manager.config_manager import Interface
            interface=Interface(id="vlan", descr="vlan", interface="vlan", enable="1", ipaddr="38.0.101.76", subnet="32", spoofmac="00:00:00:00:00:00")
    
    **Required Args**
    
    - id : str 
        the technical identifier
    - interface : str 
        target interface
    - enable : str
        1, or 0 for disable or disable
    - descr : str
        description, or name

    **Defaults**
    
    - subnet : str
        CIDR notation, default="32"
    - ipaddr : str 
        the ipv4 address, default=None
    - spoofmac: str 
        the spoofed mac, default=None 
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
        """
        This method parses the xml parent and updates the class attributes.
        It is used in the config_manager to initialize the class with the data from the xml.
        The parent element of the xml tree is passed as an argument.
        """
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
        class Vlan
        ----------

        Creates a vlan object
        **Usage**

          .. code-block:: python
            
            
            from opnsense_helper.config_manager.config_manager import Vlan
            vlan=Vlan(id="vlan", tag="1", pcp="1", descr="vlan", vlanif="vlan0.1")
            
     

        **Required Args**

        - id: str
            the identifier needed for storage, since the technical identifier is always the same ("vlan")
        - tag: str
            the tag of the vlan

        **Defaults**

        - pcp: str
            the priority code point, default = 0  
        - descr: str 
            the description, default = $id
        - vlanif: str 
            the interface, default = "vlan0."+tag  
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
        """This method parses the xml parent and updates the class attributes."""
        self.parentinterface =parseChild(parent, "if")
        self.tag = parseChild(parent,"tag")
        self.pcp = parseChild(parent,"pcp")
        self.proto = parseChild(parent,"proto")
        self.descr = parseChild(parent,"descr")
        self.vlanif = parseChild(parent,"vlanif")
        

class Dhcpd:
    """
    class Dhcpd
    ----------

    Creates a dhcp object

    **Usage**

        .. code-block:: python
            
            from opnsense_helper.config_manager.config_manager import Dhcpd
            dhcpd=Dhcpd(id="vlan", enable="1", range={"_from":"237.84.2.178","_to":"244.178.44.111"})
    
    **Req params**
    ----------

    id : str
        the id of the object and identifier of the corresponding interface
    enable : str
        "1" or "0"
    range: dict{_from:str,_to:str}
        the range of ip addresses
    
    Defaults
    ---------

    ddnsdomainalgorithm : str
        Domain Generation Algorithm - default = "hmac-md"    
    """ 
    def __init__(self,id=None,enable=None,range=None,ddnsdomainalgorithm="hmac-md"):

        self.id=id
        self.enable=enable
        self._range=range
        self.ddnsdomainalgorithm=ddnsdomainalgorithm
        self.attr={}
    def initialize(self, parent):
        """This method parses the xml parent and updates the class attributes"""
        self.enable = parseChild(parent, "enable")
        self.ddnsdomainalgorithm = parseChild(parent, "ddnsdomainalgorithm")
        self._range={
        "_from": parent.find("range/from"),
        "_to":parent.find("range/to")
        }
        if self._range["_from"] is not None:
            self._range["_from"]=self._range["_from"].text
            self._range["_to"]=self._range["_to"].text



class Config_Manager():
    """Creates a Config_Manager object"""    
    def __init__(self,  base, init):
        """Creates a Config_Manager object
        
        **Params**
        
        - base : Base_Class instance
            includes the need objects for ssh and stores the objects
        - init : bool
            if True, the xml will get parsed when the Config_Manager object is created
        """

        super().__init__()
        if base is not None:
            self.__dict__.update(base.__dict__)
        if init:
            self.get_conf()
            self.initialize() 


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
        """
        Save the current configuration to a file.

        This method takes the current in-memory configuration and saves it to a
        file specified by the output parameter. The file is written in XML
        format.

        **Parameters**
        
        - output : str
            The path to the file to which the configuration should be written.
            default: self.temp_path
        - put: bool
            Automatically copies the configuration to the firewall
        """
        output= output if output is not None else self.temp_path
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

        **Parameters**

        - element : str
            The type of the objects to retrieve. Can be "dhcpd", "interfaces",
            or "vlans".

        **Returns**
        
        - dict
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
   # def reconfigure(self,type):
        
        
    def put_file(self, _from=None,_to=None):    
        """
        Apply the configuration.
        Transfer a file from the local host to the remote host.

        **Parameters**
        
        - _from : str
            The path to the file on the local host.
            default: self.temp_path
        - _to : str
            The destination path on the remote host where the file should be stored.
            default: self.conf_path
        """
        a=_from if _from is not None else self.temp_path
        b=_to if _to is not None  else self.conf_path
        self.sftp.put(a, b)
        if len(self.objects["vlans"]) > 0:
            self.commands.reconfigure.run("vlans")
        if len(self.objects["interfaces"]) > 0:
            for interface,values in self.objects["interfaces"].items():
                # check if interface is no vlan interface, but a phyInterface
                phy=values["interface"]
                if phy!= None and  "vtnet" in phy:
                    if values["enable"] == "1" and  len(phy)>0: 
                        self.commands.reconfigure.run("interfaces", values["interface"])
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
        """
        Retrieve a specific item from the in-memory XML data.

        This method retrieves an item of a specified type from the in-memory XML data, removes its 'attr' attribute,
        and returns the remaining attributes of the item.

        **Parameters**
        
        - type : str
            The type of the item to retrieve. Can be "dhcpd", "interfaces", or "vlans".
        - item : str
            The tag of the item to retrieve.

        **Returns**

        - dict
            A dictionary containing the remaining attributes of the item after removing the 'attr' attribute.
            If the item is not found, prints a message and returns None.
        """
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

        **Parameters**
        
        - type : str
            The type of the objects to add. Can be "dhcpd", "interfaces",
            or "vlans".

        - data : dict
            A dictionary containing the objects to add. The keys are the tags of
            the elements, and the values are dictionaries containing the
            attributes and subelements of the elements.

        **Returns**
        
        None
        """
        for value in data:
            id=value.id
            del value.id
            self.objects[type][id] = value.__dict__


    def get_conf(self,_from= None,_to=None):
        """
        Get the config file from the remote host and save it to a file.

        **Parameters**
        
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









