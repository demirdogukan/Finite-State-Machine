from FMS import StateMachine
from FMS import States
from FMS import Action


class Attack(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Attack..")
        self._state = States.ATTACK
        return super().start()

    def update(self):
        print("Attacking..")
        new_state = input("Enter A State: ")
        if new_state == "DIE":
            self.action = Action.EXIT
            self._nexState = Die()
        elif new_state == "Walking":
            self._action = Action.EXIT

    def exit(self):
        print("Exiting Attack..")
        return super().exit()


class Die(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Dying..")
        self._state = States.DIE
        return super().start()

    def update(self):
        print("DIED..")
        self._action = Action.EXIT

    def exit(self):
        print("Exiting Dying..")
        return super().exit()


class Idle(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        self._state = States.IDLE
        print("Entering idle start..")
        return super().start()

    def update(self):
        print("IDLING..")
        new_state = input("Enter A Statement: ")

        if new_state == "WALKING":
            self.action = Action.EXIT
            self._nexState = Walk()
        elif new_state == "PATROL":
            self.action = Action.EXIT
            self._nexState = Patrol()

    def exit(self):
        print("Exiting Idle..")
        return super().exit()


class Patrol(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Patrolling..")
        self._state = States.PATROL
        return super().start()

    def update(self):
        print("Patrolling..")
        new_state = input("Enter A State: ")
        if new_state == "ATTACK":
            self._action = Action.EXIT
            self._nexState = Attack()
        elif new_state == "IDLE":
            self._action = Action.EXIT
            self._nexState = Idle()

    def exit(self):
        print("Exiting Patrolling..")
        return super().exit()


class Pursuit(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Run..")
        self._state = States.PURSUIT
        return super().start()

    def update(self):
        print("Running..")
        new_state = input("Enter A Statement: ")

        if new_state == "ATTACK":
            self._action = Action.EXIT
            self._state = Attack()
        elif new_state == "WALK":
            self._action = Action.EXIT
            self._state = Walk()
        elif new_state == "DIE":
            self._action = Action.EXIT
            self._state = Die()

    def exit(self):
        print("EXIT RUNNING..")
        return super().exit()


class Walk(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Walking..")
        self._state = States.WALK
        return super().start()

    def update(self):
        print("WALKING..")
        new_state = input("Enter A Statement: ")

        if new_state == "ATTACK":
            self._action = Action.EXIT
            self._nexState = Attack()
        elif new_state == "PURSUIT":
            self._action = Action.EXIT
            self._nexState = Pursuit()
        elif new_state == "PATROL":
            self._action = Action.EXIT
            self._nexState = Patrol()

    def exit(self):
        print("Exiting Walking..")
        return super().exit()
