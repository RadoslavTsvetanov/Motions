import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

message = "name"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print("Received response:", data.decode(), "from", addr)

sock.close()
