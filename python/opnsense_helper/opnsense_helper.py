
from opnsense_helper.utils.baseclass import Base_Class 

class Opnsense_Helper():
    def __init__(self, host=None, ssh_auth=None, api_auth=None, conf_path="/conf/config.xml", temp_path="./config.xml", verbose=False, init_config_manager=True):
        base_class = Base_Class(host, ssh_auth, api_auth, conf_path, temp_path, verbose)
        self.config_manager=base_class.config_manager
        self.commands=base_class.commands
        self.scripts=base_class.scripts
