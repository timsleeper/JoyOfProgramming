from pyjop import *
SimEnv.connect()

# hints for this tutorial SimEnv:
# find_all conveyor belts and save them in a list
all_convs = ConveyorBelt.find_all()

# iterate all_convs with a for loop (unlock from Perks menu)
for conv in all_convs:
    # print name of each conveyor belt
    print(conv.entity_name)
    # set_target_speed of each conveyor belt to 5.0 in the next line
    conv.set_target_speed(5.0)
    
    
    
    
from pyjop import *
SimEnv.connect()

#get a reference to the conveyor belt
conv = ConveyorBelt.find("_entityConveyorBelt0")
#get a reference to the range scanner
scanner = RangeFinder.find("_entityRangeFinder0")

while SimEnv.run_main():
    # add your code within this loop. mind the indendation
    
    # hints:
    # use variable conv to control "_entityConveyorBelt0"
    # use variable scanner to control "_entityRangeFinder0"
    # read the RFID tag scanned by scanner
    tag = scanner.get_rfid_tag()
    # if the tag is "Box" set conv's target_speed backwards (e.g. -2.0)
    # elif the tag is "Barrel", set it forwards (e.g. 2.0)
    # else (tag is empty / no tag) set conv's target_speed to 0
    if tag == "Box":
        conv.set_target_speed(-2.5)
    else:
        conv.set_target_speed(2.5)