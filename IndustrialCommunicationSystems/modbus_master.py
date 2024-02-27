import socket
import struct

"""
Authors:
Lauri Nuutinen
Valtteri Nikkanen
Väinö Kurvi

Date: 9.3.2023

This is a simple program for accessing and modifying data using modbus.
"""


def modbus(cmd, transaction, length, fcode, reg_addr, data):
    host = '127.0.0.1'  # local IP
    port = 502  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    identifier = 0
    unitid = 0

    # struct.pack formats the information
    message = struct.pack('>HHHBBHH', transaction, identifier, length, unitid,
                          fcode, reg_addr, data)
    s.send(message)

    rec = s.recv(4096)
    rec = struct.unpack(cmd, rec)

    print("Transaction identifier: ", rec[0])
    print("Protocol identifier: ", rec[1])
    print("Length", rec[2])
    print("Unit identifier: ", rec[3])
    print("Function code ", rec[4])
    if fcode < 5:
        print("Byte Count: ", rec[5])
    else:
        print("Address: ", rec[5])

    # different prints for different function codes.
    if fcode == 1 or fcode == 2:
        print_data(rec, reg_addr, data)

    elif fcode == 5:
        value = rec[6]
        if value != 0:
            value = 1
        print("  Coil", reg_addr, ":", value)

    else:
        count = reg_addr
        for x in range(6, len(rec)):
            print("  Register", count, ":", rec[x])
            count += 1

    s.close()


def create_cmd(count):
    return '>HHHBBH' + 'H' * count


def print_data(rec, reg_addr, data):
    count = 0
    for x in range(6, len(rec)):

        current = bin(rec[x])
        while len(current) != 10 and x != len(rec) - 1:
            current = current[:2] + "0" + current[2:]

        # if the rec is only filled with zeroes the bin fuction shortens it to just a single 0,
        # therefore the zeroes need to be added back
        if rec[x] == 0b0:
            y = 0
            while count + y < data - 1 and y < 8:
                current += '0'
                y += 1

        for bit in reversed(current[2:]):
            print(f"Coil {reg_addr + count}: {bit}")
            count += 1


run = True
transaction_id = 0
while run:

    user_input = input("What would you like to do?\n"
                       "  1- Read Coil (Output) Status\n "  # DONE -ish Luettava byten kokoisia bin채채rilukuja
                       " 2- Read Discrete Inputs\n "  # DONE -ish Luettava byten kokoisia bin채채rilukuja
                       " 3- Read Holding Registers\n "  # DONE -ish Address ei toimi
                       " 4- Read Input Registers\n "  # DONE -ish Address ei toimi
                       " 5- Write Single Coil\n "  # DONE
                       " 6- Write Single Register\n "  # DONE
                       " q/Q to quit\n "  # DONE
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

        bytes = int(count_input) // 8
        if int(count_input) % 8 != 0:
            bytes += 1
        cmd = '>HHHBBB' + bytes * 'B'

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
        # Transaction, Protocol, Length, UnitID, FuncCode, Byte count, x*H
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
        if data_input == "ON":
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
