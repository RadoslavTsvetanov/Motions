from combination import Sequence,Key,HotKey,Scroll,Move_mouse_to_position,Click_on_mouse_position
from typing import List
from abc import ABC,abstractmethod
import threading
class AbstractExecutor(ABC):
    @abstractmethod
    def execute(self):
        pass

class Executor(AbstractExecutor):
    def __init__(self,sequence_to_execute: Sequence): #* if you only want a single thing to execute just pass an arr with one element
        self.sequence = sequence_to_execute
    
    def execute(self):
        def run():
            for combination_item in self.sequence.key_combination:
                combination_item.execute_key()
        print("executing")
        thread = threading.Thread(target=run)
        thread.start()

# class CUstom_executor(AbstractExecutor):
#     def __init__



# key1 = Key('ctrl')
# key2 = Key('c')
# hotkey = HotKey(['ctrl', 'shift', 't'])
# scroll_up = Scroll('up', 1)
# scroll_down = Scroll('down', -1)

# # Create a sequence
# sequence = Sequence([key1, key2, hotkey, scroll_up, scroll_down])

# # Create an executor
# executor = Executor(sequence)

# # Execute the combination
# executor.execute()