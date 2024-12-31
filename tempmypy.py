 
from pyjop import *
 
SimEnv.connect()
 
env = SimEnvManager.first()
while SimEnv.run_main():
     
     
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")
    
 
    reveal_locals()
SimEnv.disconnect()
reveal_locals()