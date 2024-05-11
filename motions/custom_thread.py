import threading

def start_thread(function_to_call):
    thread_to_be_started = threading.Thread(target=function_to_call)
    thread_to_be_started.start()