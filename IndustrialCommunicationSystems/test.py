import socket
import struct

host = '127.0.0.1'  # local IP
port = 502  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

transaction = 6
identifier = 0
length = 6
unitid = 0
fcode = 5
reg_addr = 8003
data = 255

message = struct.pack('>HHHBBH?', transaction, identifier, length, unitid,
                      fcode, reg_addr, data)

s.send(message)
s.close()