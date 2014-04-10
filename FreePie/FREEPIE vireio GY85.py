def update():
   global yaw
   global roll
   global pitch
   
   yaw = ahrsImu.yaw
   roll = ahrsImu.roll
   pitch = ahrsImu.pitch
   
   vireioSMT.yaw = yaw - cyaw
   vireioSMT.roll = roll - croll
   vireioSMT.pitch = pitch - cpitch

   diagnostics.watch(yaw-cyaw)
   diagnostics.watch(roll-croll)
   diagnostics.watch(pitch-cpitch)
   
if starting:
   cyaw = 0
   croll = 0
   cpitch = 0
   ahrsImu.update += update

center = keyboard.getPressed(Key.Z)

if center:
   cyaw = yaw
   croll = roll
   cpitch = pitch