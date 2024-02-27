import socket
import struct

def modbus(cmd, transaction, length, fcode, reg_addr, data):

    host = '127.0.0.1'           # local IP
    port = 502                   # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    identifier = 0
    unitid = 0

    message = struct.pack('>HHHBBHH', transaction, identifier, length, unitid,
                          fcode, reg_addr, data)
    s.send(message)

    data = s.recv(4096)

    print('Received', data)
    data = struct.unpack(cmd, data)
    print("Transaction identifier: ", data[0])
    print("Protocol identifier: ", data[1])
    print("Length", data[2])
    print("Unit identifier: ", data[3])
    print("Function code ", data[4])
    print("Address ", data[5])

    count = int(data[5])
    print("Data")
    for x in range(6, len(data)):
        print("  slot:", count, "-->", data[x])
        count += 1
        s.close()


def create_cmd(count):
    return '>HHHBBH' + 'H' * count


run = True
transaction_id = 0
while run:

    user_input = input("What would you like to do?\n"
                  "  1- Read Coil (Output) Status\n "   # DONE -ish Luettava byten kokoisia binäärilukuja
                  " 2- Read Discrete Inputs\n "         # DONE -ish Luettava byten kokoisia binäärilukuja
                  " 3- Read Holding Registers\n "       # DONE -ish Address ei toimi
                  " 4- Read Input Registers\n "         # DONE -ish Address ei toimi
                  " 5- Write Single Coil\n "            # DONE
                  " 6- Write Single Register\n "        # DONE
                  " q/Q to quit\n "                     # DONE
                  "----> ")

    if user_input == "q" or user_input == "Q":
        run = False
        continue

    transaction_id += 1

    reg_addr = input("Please enter the register address: ")

    # Read output coil
    if user_input == "1":

        length = 6
        fcode = 1

        count_input = input("Please insert how many you would like to read: ")

        bytes = int(count_input)//8
        if int(count_input) % 8 != 0:
            bytes += 1
        cmd = '>HHHBBB' + bytes*'B'

        modbus(cmd, transaction_id, length, fcode, int(reg_addr),
               int(count_input))

    # Read discrete inputs
    elif user_input == "2":
        length = 6
        fcode = 2
        count_input = input("Please insert how many you would like to read: ")

        bytes = int(count_input) // 8
        if int(count_input) % 8 != 0:
            bytes += 1
        cmd = '>HHHBBB' + bytes * 'B'

        modbus(cmd, transaction_id, length, fcode, int(reg_addr),
               int(count_input))

    # Read Holding Registers
    elif user_input == "3":
        length = 6
        fcode = 3
        count_input = input("Please insert how many you would like to read: ")
        #Transaction, Protocol, Length, UnitID, FuncCode, Byte count, x*H
        cmd = '>HHHBBB' + 'H' * int(count_input)
        modbus(cmd, transaction_id, length, fcode, int(reg_addr),
               int(count_input))

    # Read Input Registers
    elif user_input == "4":
        length = 6
        fcode = 4
        count_input = input("Please insert how many you would like to read: ")
        cmd = '>HHHBBB' + 'H' * int(count_input)
        modbus(cmd, transaction_id, length, fcode, int(reg_addr),
               int(count_input))

    # Write Single Coil
    elif user_input == "5":
        length = 6
        fcode = 5
        data_input = input("ON/OFF: ")
        if (data_input == "ON"):
            data = 65280
        else:
            data = 0
        cmd = create_cmd(1)
        modbus(cmd, transaction_id, length, fcode, int(reg_addr), data)

    # Write Single Register
    # WORKS
    elif user_input == "6":
        fcode = 6
        length = 6
        cmd = '>HHHBBHH'
        data_input = input("Please insert what you want to insert: ")
        cmd = create_cmd(1)
        modbus(cmd, transaction_id, length, fcode, int(reg_addr),
               int(data_input))

    else:
        print("Please enter valid command")
        continue

    print()
