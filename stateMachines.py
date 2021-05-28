from FMS import StateMachine
from FMS import States
from FMS import Action


class Attack(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Attack..")
        self.state = States.ATTACK
        return super().start()

    def update(self):
        print("Attacking..")
        new_state = input("Enter A State: ")
        if new_state == "DIE":
            self.action = Action.EXIT
            self.nexState = Die()
        elif new_state == "Walking":
            self.action = Action.EXIT

    def exit(self):
        print("Exiting Attack..")
        return super().exit()


class Die(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Dying..")
        self.state = States.DIE
        return super().start()

    def update(self):
        print("DIED..")
        self.action = Action.EXIT

    def exit(self):
        print("Exiting Dying..")
        return super().exit()


class Idle(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        self.state = States.IDLE
        print("Entering idle start..")
        return super().start()

    def update(self):
        print("IDLING..")
        new_state = input("Enter A Statement: ")

        if new_state == "WALKING":
            self.action = Action.EXIT
            self.nexState = Walk()
        elif new_state == "PATROL":
            self.action = Action.EXIT
            self.nexState = Patrol()

    def exit(self):
        print("Exiting Idle..")
        return super().exit()


class Patrol(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Patrolling..")
        self.state = States.PATROL
        return super().start()

    def update(self):
        print("Patrolling..")
        new_state = input("Enter A State: ")
        if new_state == "ATTACK":
            self.action = Action.EXIT
            self.nexState = Attack()
        elif new_state == "IDLE":
            self.action = Action.EXIT
            self.nexState = Idle()

    def exit(self):
        print("Exiting Patrolling..")
        return super().exit()


class Pursuit(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Run..")
        self.state = States.PURSUIT
        return super().start()

    def update(self):
        print("Running..")
        new_state = input("Enter A Statement: ")

        if new_state == "ATTACK":
            self.action = Action.EXIT
            self.state = Attack()
        elif new_state == "WALK":
            self.action = Action.EXIT
            # self.state = Walk()
        elif new_state == "DIE":
            self.action = Action.EXIT
            self.state = Die()

    def exit(self):
        print("EXIT RUNNING..")
        return super().exit()


class Walk(StateMachine):

    def __init__(self):
        super().__init__()

    def start(self):
        print("Entering Walking..")
        self.state = States.WALK
        return super().start()

    def update(self):
        print("WALKING..")
        new_state = input("Enter A Statement: ")

        if new_state == "ATTACK":
            self.action = Action.EXIT
            self.nexState = Attack()
        elif new_state == "PURSUIT":
            self.action = Action.EXIT
            self.nexState = Pursuit()
        elif new_state == "PATROL":
            self.action = Action.EXIT
            self.nexState = Patrol()

    def exit(self):
        print("Exiting Walking..")
        return super().exit()
