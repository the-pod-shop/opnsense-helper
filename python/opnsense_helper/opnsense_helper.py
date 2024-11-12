
from opnsense_helper.utils.baseclass import Base_Class 
from opnsense_helper.utils import utils
class Opnsense_Helper():
    def __init__(self, host=None, ssh_auth=None, api_auth=None, conf_path="/conf/config.xml", temp_path="./config.xml", verbose=False, init_config_manager=True):
        """
        Initialize an Opnsense_Helper instance.

        :param host: The hostname or ip address of the opnsense firewall.
        :param ssh_auth: A dictionary containing the ssh authentication data.
                         The dictionary must contain the keys "user" and "passw".
        :param api_auth: A dictionary containing the api authentication data.
                         The dictionary must contain the keys "api_key", "api_secret", "ssl" and "verify".
        :param conf_path: The path to the config.xml on the opnsense firewall.
        :param temp_path: The path to the temporary config.xml file.
        :param verbose: If True, the class will print debug messages.
        :param init_config_manager: If True, the class will initialize the config_manager.
        """
        base_class = Base_Class(host, ssh_auth, api_auth, conf_path, temp_path, verbose)
        self.config_manager=base_class.config_manager
        self.commands=base_class.commands
        self.scripts=base_class.scripts
