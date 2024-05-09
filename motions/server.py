import socket
import threading
from queue import Queue
from abc import ABC, abstractmethod
from motion import Motion
from typing import List

class Handler:
    @abstractmethod
    def handle(self, data, addr):
        pass

def udp_server(handler: Handler, udp_ip="127.0.0.1", udp_port=5005):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((udp_ip, udp_port))
    print("UDP server started")

    while True:
        data, addr = sock.recvfrom(1024)
        handler.handle(data.decode(), addr)
        sock.sendto(data, addr)

class MyHandler(Handler):
    def __init__(self,motions: List[Motion]):
        self.motions = motions

    def handle(self, data, addr):
        self.motions[0].execute()
        print(data)

