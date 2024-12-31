 
from pyjop import *
 
SimEnv.connect()
arm = RobotArm.first()
 
arm.set_grabber_location([0.8,0.2,0.3])
 
SimEnv.disconnect()
reveal_locals()