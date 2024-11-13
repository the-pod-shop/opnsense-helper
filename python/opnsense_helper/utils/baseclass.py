import logging
import paramiko
from opnsense_helper.utils.exec_class import Exec_Class
from opnsense_helper.commands.commands import Commands
from opnsense_helper.scripts.scripts import Scripts
from opnsense_helper.config_manager.config_manager import Interface, Vlan, Dhcpd, Config_Manager

class Base_Class():
    def __init__(self, host=None, ssh_auth=None, api_auth=None, conf_path="/conf/config.xml", temp_path="./config.xml", verbose=False, init_config_manager=True):
        if(verbose):
            self.logging=logging.basicConfig(level=logging.DEBUG)
        self.objects={
        "vlans":{},
        "dhcpd":{},
        "interfaces":{}
        }
        self.url = host
        self.conf_path=conf_path
        self.temp_path= temp_path


        if(ssh_auth!=None):
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
        exec_class = Exec_Class(self)
        self.commands=Commands(exec_class)
        self.scripts=Scripts(exec_class)
        self.config_manager=Config_Manager(self, init=True)

        if init_config_manager:
            self.config_manager.get_conf()
            self.config_manager.initialize() 

    def close(self):
       self.close_con()

    def close_con(self):
        self.sftp.close()
        self.ssh.close()

    def run(self, command):
        res=exec(self, self.commands[command])
        print( res)
        return res