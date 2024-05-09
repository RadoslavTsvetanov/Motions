from typing import List
from trigger import Trigger
from executor import Executor
import threading
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

class Motion:
    def __init__(self,Trigger: Trigger,Executor: Executor) -> None:
        self.Trigger = Trigger
        self.Executor = Executor


    def handle_motion(self,current_keys):
        if self.Trigger.check_trigger(current_keys): # check implementation since its probs firing in another thread and ytou should know that if debugging

            self.Executor.execute()

    def execute(self):
        self.Executor.execute()


class Motions:
    def __init__(self):
        self.motions: List[Motion] = []
    

    def add_motions(self, motions: List[Motion]):
        for motion in motions:
            self.motions.append(motion)


    def add_motion(self,motion: Motion): # just a wrapper
        self.add_motions([motion])

    def check_motions(self,current_keys):
        for motion in self.motions:
            motion_wrapper = motion.handle_motion(current_keys)
            (threading.Thread(target=motion_wrapper)).start()


    def remove_motion(self,Motion: Motion):
        self.motions.remove(Motion)

