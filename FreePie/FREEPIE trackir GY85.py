import math

def update():
   global yaw
   global roll
   global pitch
   
   yaw = round(ahrsImu.yaw)
   roll = round(ahrsImu.roll)
   pitch = round(ahrsImu.pitch) 
   
   trackIR.yaw = yaw - cyaw
   trackIR.roll = roll - croll
   trackIR.pitch = pitch - cpitch
   
   diagnostics.watch(yaw - cyaw)
   
if starting:
   cyaw=0
   croll=0
   cpitch=0
   ahrsImu.update += update

center = keyboard.getPressed(Key.Z)

if center:
   cyaw = yaw
   croll = roll
   cpitch = pitch