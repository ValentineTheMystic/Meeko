import datetime
import json
# Local modules

class Memory:
 def __init__(self):
  self.history = 'history.toml'

 def commit(self,scope,target):
  _time = datetime.datetime.now()
  _timeStamp = _time.strftime("%x_%H:%M:%S")
  _decision = {'scope': scope,'target': target}
  _entry = json.dumps({_timeStamp: _decision}, indent=1)

  f = open(self.history, "a")
  f.write(_entry)
  f.write(",\n")
  f.close()

 def reflect(self):
  pass

 def debug(self):
  print(self.history)
