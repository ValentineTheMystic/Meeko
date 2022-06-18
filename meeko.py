import datetime
import toml
import time
## local modules
import Agent
import Environment
import Memory

## prepares config file
config = toml.load('default.toml')

## This declares and initiates the agent,
## environment, and memory objects
agent = Agent.Agent(config['agent'])
env = Environment.Client(config['environment'])
memory = Memory.Memory()

## The actual script starts below this point
#variable = env.getWifi()
variable = agent.reconScan(env,True,True)
for x in variable:
 print(x,'\n')
print(agent.chooseTarget(variable))
