from opnsense_helper.utils.utils import exec
class Exec_Class():
     def __init__(self, base):
         self.base=base          
     def run(self, command,argument=None,flags=[]):
          command=self.commands[command]
          command["argument"]=argument
          command["flags"]=flags
          res=exec(self.base,command )
          return res