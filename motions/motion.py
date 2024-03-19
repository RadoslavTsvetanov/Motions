from typing import List
from combination import Key_combination
from trigger import Trigger
from executor import Executor
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

class Motion:
    def __init__(self,position: Position,Trigger: Trigger,Executor: Executor) -> None:
        self.position = position
        self.Trigger = Trigger
        self.Executor = Executor


    def handle_motion(self):
        if self.Trigger.listen_for_trigger():
            self.Executor.execute()

class Motions:
    def __init__(self):
        self.motions: List[Motion] = []

    def add_motion(self,Motion: Motion):
        self.motions.append(Motion)

    def listen_motions(self):
        for motion in self.motions:
            motion.handle_motion()


    def remove_motions(self,Motion: Motion):
        self.motions.remove(Motion)



motions = Motions()

motions.add_motion(Motion(Position(100,100),Trigger()))