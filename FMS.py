from abc import ABC, abstractmethod
from enum import Enum


class States(Enum):
    IDLE = 1
    PURSUIT = 2
    PATROL = 3
    ATTACK = 4
    DIE = 5
    WALK = 6


class Action(Enum):
    START = 1
    UPDATE = 2
    EXIT = 3


class StateMachine(ABC):
    nexState = None
    state = States(value=1)
    action = Action(value=1)

    @abstractmethod
    def start(self):
        self.action = Action.UPDATE

    @abstractmethod
    def update(self):
        self.action = Action.UPDATE

    @abstractmethod
    def exit(self):
        self.action = Action.EXIT

    def process(self):
        if self.action == Action.START:
            self.start()
        elif self.action == Action.UPDATE:
            self.update()
        elif self.action == Action.EXIT:
            self.exit()
            return self.nexState

        return self
