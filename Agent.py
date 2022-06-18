import datetime
import time
import random
import toml
# Local modules
import Config

def sortFunction(e):
 return e['rssi']

class Agent:
 def __init__(self,config):
  self.name = config['name']
  self.genesis = datetime.time()
  self.targetWeights = config['targeting']['targetWeights']
  self.scopeSize = config['targeting']['scope']
  self.scanTime = 30
  self.channels = config['recon']['channels']

 def reconScan(self,env):
  env.cmd('set ticker.commands "clear;wifi.show"')
  env.cmd("set wifi.interface wlan1")
  env.cmd("wifi.recon on;ticker on")
  time.sleep(self.scanTime)
  _scan = env.get()
  env.cmd("ticker off;wifi.recon off;wifi.clear;clear")
  result = self.filterEnv(_scan)
  return result

 def filterEnv(self,env):
  _env = env
  _envScope = []
  for x in _env:
   _envScope.append(x)
  _envScope.sort(reverse=True,key=sortFunction)
  del _envScope[5:]
  return(_envScope)

 def chooseTarget(self,envScope):
  _weights = [3,2,2,1,1]
#  _weights = self.targetWeights
  _envScope = envScope
  for x in random.choices(_envScope,weights=_weights):
   _scopeTarget = {
    'hostname': x['hostname'],
    'mac': x['mac'],
    'vendor': x['vendor'],
    'frequency': x['frequency'],
    'channel': x['channel'],
    'rssi': x['rssi'],
    'encryption': x['encryption'],
    'authentication': x['authentication'],
    'Clients': len(x['vendor'])
   }
  return _scopeTarget

 def debug(self):
  print(self.name)
#  config = toml.load('default.toml')
#  print(config['agent']['recon'])
  print(self.scopeSize)
  print(type(self.targetWeights))
  print(self.channels)
