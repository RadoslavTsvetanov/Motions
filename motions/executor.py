from combination import Sequence, Key, HotKey, Scroll
import threading
from abc import ABC, abstractmethod
import subprocess
class AbstractExecutor(ABC):
    @abstractmethod
    def run(self):
        pass

    def execute(self): #TODO ask if potential problem will be that it wont keep order of operations since if it fires ine operation and then other of the other is shorter the shorter will be executed first. Potential fix is to reduce the multithreading part to just making a listening thread and executing thread 
        thread = threading.Thread(target=self.run)
        print("Executing...")
        thread.start()

class Executor(AbstractExecutor):
    def __init__(self, sequence_to_execute: Sequence):
        self.sequence = sequence_to_execute

    def run(self):
        for combination_item in self.sequence.key_combination:
            combination_item.execute_key()
        print("Execution completed.")

class ExeExecutor(AbstractExecutor):
    def __init__(self, command_to_execute):
        self.command_to_execute = command_to_execute

    def run(self):
        try:
            subprocess.run(self.command_to_execute, shell=True, check=True)
            print("Executable executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing executable: {e}")




exexe = ExeExecutor("node ./motions/index.js")


exexe.run()