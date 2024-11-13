
from opnsense_helper.utils.baseclass import Base_Class 
from opnsense_helper.utils import utils
class Opnsense_Helper():

    """
    class Opnsense_Helper
    -----------

    Initialize an Opnsense_Helper instance.

    **Usage**
        see example.py
        
        .. code-block:: python

            from opnsense_helper.opnsense_helper import Opnsense_Helper
            from opnsense_helper.config_manager.config_manager import Vlan, Dhcpd, Interface
            helper=Opnsense_Helper(host=host,ssh_auth=auth,temp_path=temp_path, init_config_manager=True)

    **Parameters**
    
    - host : str
        The hostname or ip address of the opnsense firewall.
    - ssh_auth : dict
        A dictionary containing the ssh authentication data.
        The dictionary must contain the keys "user" and "passw".
    - api_auth : dict
        A dictionary containing the api authentication data.
        The dictionary must contain the keys "api_key", "api_secret", "ssl" and "verify".
    - conf_path : str
        The path to the config.xml on the opnsense firewall.
    - temp_path : str
        The path to the temporary config.xml file.
    - verbose : bool
        If True, the class will print debug messages.
    - init_config_manager : bool
        If True, the class will initialize the config_manager.
    
    **Attributes**
    
    - config_manager : Config_Manager
        An instance of the Config_Manager class.
    - commands : Commands
        An instance of the Commands class.
    - scripts : Scripts
        An instance of the Scripts class.
    """
    def __init__(self, host=None, ssh_auth=None, api_auth=None, conf_path="/conf/config.xml", temp_path="./config.xml", verbose=False, init_config_manager=True):

        base_class = Base_Class(host, ssh_auth, api_auth, conf_path, temp_path, verbose)
        self.config_manager=base_class.config_manager
        self.commands=base_class.commands
        self.scripts=base_class.scripts

