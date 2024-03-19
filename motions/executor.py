from combination import Sequence,Key,HotKey,Scroll
from typing import List

class Executor():
    def __init__(self,sequence_to_execute: Sequence): #* if you only want a single thing to execute just pass an arr with one element
        self.sequence = sequence_to_execute
    
    def execute(self):
        for combination_item in self.sequence.key_combination:
            combination_item.execute_key()


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