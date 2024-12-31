#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

SimEnvManager.first().reset(stop_code=False)

platform = MovablePlatform.first()
#set_target_location to move platform above dumpster
#sleep until arrived
#rotate platform to drop barrel

platform.set_target_location(0,0,400)
sleep(3)
platform.set_target_location(-2.5,0,400)
sleep(1)
platform.set_target_rotation(0,60,0)
#cleanup close code
SimEnv.disconnect()