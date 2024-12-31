#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()
SimEnvManager.first().reset(stop_code=False)
speed = 20.0

#create references to entities in the SimEnv
env = SimEnvManager.first()
obj_spawner = ObjectSpawner.first()
conv_0 = ConveyorBelt.find("belt0")
conv_1 = ConveyorBelt.find("belt1")
conv_2 = ConveyorBelt.find("belt2")
conv_3 = ConveyorBelt.find("belt3")
conv_4 = ConveyorBelt.find("belt4")

scan_0 = RangeFinder.find("scan0")
scan_1 = RangeFinder.find("scan1")

conv_0.set_target_speed(speed)
conv_2.set_target_speed(speed)
conv_3.set_target_speed(speed)

while SimEnv.run_main():
    # main loop to retrieve data from the SimEnv, calculate stuff and send commands back into the SimEnv
    # for example, get current time and display it
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")
    if not conv_0.get_is_transporting() and not conv_1.get_is_transporting():
        obj_spawner.spawn()
    if scan_0.get_rfid_tag() == "Barrel":
        conv_1.set_target_speed(-speed)
    elif scan_0.get_rfid_tag() in ["Box", "Cone"]:
        conv_1.set_target_speed(speed)
    if scan_1.get_rfid_tag() == "Cone":
        conv_4.set_target_speed(speed)
    elif scan_1.get_rfid_tag() == "Box":
        conv_4.set_target_speed(-speed)

	
#cleanup close code
SimEnv.disconnect()
