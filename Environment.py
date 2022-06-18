import requests
import json
import requests
from requests.auth import HTTPBasicAuth
## Local modules

class Client:
 def __init__(self,config):
  self.hostname = config['server']['hostname']
  self.scheme = config['server']['scheme']
  self.port = config['server']['port']
  self.username = config['server']['username']
  self.password = config['server']['password']
  _url = "{}://{}:{}/api"
  self.url = _url.format(self.scheme,self.hostname,self.port)
  self.auth = HTTPBasicAuth(self.username,self.password)

 def session(self):
  _request = "{}/session"
  _response = requests.get(_request.format(self.url),auth=self.auth)
  data = _response.json()
  return data

 def cmd(self,cmd):
  _request = "{}/session"
  _cmd = json.dumps({'cmd': cmd})
  _response = requests.post(_request.format(self.url),data=_cmd,auth=self.auth)

 def getWifi(self):
  _wifi = self.session()
  wifi = []
  for x in _wifi['wifi']['aps']:
   _ap = {}
   _ap['hostname'] = x['hostname']
   _ap['mac'] = x['mac']
   _ap['vendor'] = x['vendor']
   _ap['first_seen'] = x['first_seen']
   _ap['last_seen'] = x['last_seen']
   _ap['frequency'] = x['frequency']
   _ap['channel'] = x['channel']
   _ap['rssi'] = x['rssi']
   _ap['encryption'] = x['encryption']
   _ap['cipher'] = x['cipher']
   _ap['authentication'] = x['authentication']
   _ap['wps'] = x['wps']
   _ap['clients'] = x['clients']
   wifi.append(_ap)
  return wifi

 def debug(self):
  print(self.hostname)
  print(self.scheme)
  print(self.port)
  print(self.username)
  print(self.password)
  print(self.url)
