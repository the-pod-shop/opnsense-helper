import xml.etree.ElementTree as ET
# import libraries
import json
import xml.etree.ElementTree as ET
import requests
import os

# deprecated
def get_backup(helper,output=None):
    """
    this function is currently deprecated
    it was used to get the config file using the api
    i left it in however if someone wants to fetch a certain backup 
    i need to implement the backup selection though
    """
    command = 'core/backup/download/this'
    backup=api_get(helper,command)
    helper.root=backup
    print(ET.tostring(backup, encoding='unicode'))
    # if output != None:
    #     path=output
    # else:
    #     path = self.temp_path
    # with open(path, 'w') as f:
    #     f.write(ET.tostring(backup, encoding='unicode', method='xml'))


# deprecated
def vlans_api(helper,vlans, command="add"):
    if command == "add":
        for value in vlans:
            print("---------add vlan-----------------")
            print(value)
            payload={"vlan":value}
            r=api_post(helper,"interfaces/vlan_settings/addItem",payload)
            print(r)
            r=api_post(helper,"interfaces/vlan_settings/reconfigure",{})
            print(r)
    elif command == "set":
        for value in vlans:
                print("---------set vlan-----------------")
                payload={"vlan":value}
                r=api_post(helper,"interfaces/vlan_settings/set",payload)
                print(r)
    

def ping(helper):
    response = os.system(f"ping -c 1 {helper.host}")
    if response == 0:
        print(f"IP {helper.host} is reachable")
        return 0
    else: return 1
def api_get(helper, command,params=None):
    #url= "https://192.168.1.103/api/interfaces/vlan_settings/get"
    s="s" if helper.ssl is True else ""
    url = f"http{s}://{helper.host}/api/{command}"
    r = requests.get(url, verify=helper.verify, params=params,  auth=(helper.api_key, helper.api_secret))


    if r.status_code == 200:
        if 'application/json' in r.headers['Content-Type']:
            # Verwenden Sie json.dump
            response = json.loads(r.content)
        else:
            # Verwenden Sie ET.fromstring
            response = ET.fromstring(r.content)
        return (response)
    else:
        print ('Connection / Authentication issue, response received:')
        print (r.text)
def api_post(helper, command, Data):
    def post(Data,url):
        return requests.post(url, verify=helper.verify, allow_redirects=False, headers={'Content-Type': 'application/json'},  auth=(helper.api_key, helper.api_secret), data=Data)
    def fail(error):
        print ('Connection / Authentication issue, response received:')
        print (error)
    def success(response):
        response = json.loads(r.text)
        return (response)
    Data=json.dumps(Data)
    s="s" if helper.ssl is True else ""
    url = f"http{s}://{helper.host}/api/{command}"
    r = post(Data,url)
    if r.status_code == 200:
        return success(r)
    # if we fail because of redirect we start a new request
    # if we allow redirect in the first place, our post request will get turned in a get request
    elif r.status_code == 301:
        new_url = r.headers['Location']
        r = post(Data,new_url)
        if r.status_code == 200:
            return success(r)
        else:
            fail(r.text)
    else:
        fail(r.text)
def get_vlans(helper):
    command="interfaces/vlan_settings/get"
    vlans=api_get(helper,command)
    print(vlans)     
