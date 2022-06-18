import datetime
import time
import random
# Local modules

def sortFunction(e):
 return e['rssi']

class Agent:
 def __init__(self,config):
  self.name = config['name']
  self.genesis = datetime.time()
  self.targeting = config['targeting']
  self.recon = config['recon']

 def reconScan(self,env,filtered,trimmed):
#  env.cmd('set ticker.commands "clear;wifi.show"')
#  env.cmd("set wifi.interface wlan1")
  env.cmd("wifi.recon on;ticker on")
  time.sleep(self.recon['duration'])
  _scan = env.getWifi()
  env.cmd("ticker off;wifi.recon off;wifi.clear;clear")
  result = self.reconFilter(_scan,trimmed)
  return result

 def reconFilter(self,env,trimmed):
  _env = env
  _envScope = []
  for x in _env:
   _envFiltered = {
    'mac': x['mac'],
    'frequency': x['frequency'],
    'channel': x['channel'],
    'rssi': x['rssi'],
    'clients': len(x['clients']),
   }
   _envScope.append(_envFiltered)
  _envScope.sort(reverse=True,key=sortFunction)
  if trimmed:
   del _envScope[5:]
   return(_envScope)
  else:
   return(_envScope)

 def reconReward(self,reconScan):
  reward = 0
  for x in reconScan:
   _points = 1 + (x['clients'] * .5)
   reward += _points
  return reward

 def chooseTarget(self,envScope):
  _weights = self.targeting['targetWeights']
  _envScope = envScope
  _target = random.choices(_envScope,weights=_weights)
  target = _target[0]
  return target

 def debug(self):
  print(self.name)
#  config = toml.load('default.toml')
#  print(config['agent']['recon'])
