#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()
SimEnvManager.first().reset(stop_code=False)
arm = RobotArm.first()
#set grabber location to x (forward) 0.2m; y (right) -1m (so actually 1 meter to the left); z (up) 1.5m

arm.set_grabber_location([1.5,1.5,0.9])
sleep(2)
arm.set_grabber_location([1.5,0.2,0.9])
sleep(2)
arm.set_grabber_location([1.5,0.2,0.4])
sleep(2)
arm.pickup()
sleep(2)
arm.set_grabber_location([1.5,0.2,5.0])
sleep(2)
arm.set_grabber_location([-2.5,0,5.0])
sleep(3)
arm.release()



#cleanup close code
SimEnv.disconnect()