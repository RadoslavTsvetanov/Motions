from typing import List
from trigger import Trigger
from executor import Executor
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

class Motion:
    def __init__(self,Trigger: Trigger,Executor: Executor) -> None:
        self.Trigger = Trigger
        self.Executor = Executor


    def handle_motion(self,current_keys):
        if self.Trigger.check_trigger(current_keys):

            self.Executor.execute()

class Motions:
    def __init__(self):
        self.motions: List[Motion] = []

    def add_motion(self,Motion: Motion):
        self.motions.append(Motion)

    def listen_motions(self,current_keys):
        for motion in self.motions:
            motion.handle_motion(current_keys)


    def remove_motion(self,Motion: Motion):
        self.motions.remove(Motion)
