
from opnsense_helper.config_manager.config_manager import Interface, Vlan, Dhcpd, Config_Manager
from opnsense_helper.utils.baseclass import Base_Class
from opnsense_helper.commands.commands import Commands
from opnsense_helper.scripts.scripts import Scripts
class Opnsense_Helper():
    def __init__(self, host=None, ssh_auth=None, api_auth=None, conf_path="/conf/config.xml", temp_path="./config.xml", verbose=False, init_config_manager=True):
        
        base_class = Base_Class(host, ssh_auth, api_auth, conf_path, temp_path, verbose)
        self.config_manager=Config_Manager(base_class)
        self.commands=Commands(base_class)
        self.scripts=Scripts(base_class)
        
        if init_config_manager:
            self.config_manager.get_conf()
            self.config_manager.initialize() 
