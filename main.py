from stateMachines import Idle

_idle = Idle()

while _idle is not None:
    _idle = _idle.process()

print("FINITE STATE MACHINE GAME END..")
