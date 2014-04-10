def update():
   global yaw
   global roll
   global pitch
   yaw = ahrsImu.yaw
   roll = ahrsImu.roll
   pitch = ahrsImu.pitch

if starting:
   yaw = 0
   roll = 0
   pitch = 0
   enabled = False
   ahrsImu.update += update

diagnostics.watch(yaw)
diagnostics.watch(roll)
diagnostics.watch(pitch)

deltaYaw = filters.delta(yaw)
deltaPitch = filters.delta(pitch)
deltaRoll = filters.delta(roll)
   
if (enabled):
   mouse.deltaX = deltaYaw*10
   mouse.deltaY = -deltaPitch*10

toggle = keyboard.getPressed(Key.Z)

if toggle:
   enabled = not enabled