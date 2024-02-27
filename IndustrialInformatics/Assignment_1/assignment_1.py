"""
AUT.840 Assignment 1
Authors: Jukka Hirvonen, Valtteri Nikkanen, Jouni Kokko
Student IDs: H218618,
Created: 27.10.2022

An orchestrator program that routes a pallet to the workstation and draws
an ordered pattern using REST.

Orders are expected to come in JSON format ->

{"id": "order",
 "order": [recipe1,
           recipe2,
           recipe3]
 }

where recipe1 is a number between 1-3, recipe2 between 4-6 and recipe3
between 7-9

"""

import json
import time
import requests
from flask import Flask, request
#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address


class Orchestrator:

    def __init__(self, ipaddress):
        # Workstations by their ID -> {ID : Workstation}
        self.workstationsById = {}
        self.ipaddress = ipaddress
        # List of orders
        self.order_queue = []
        # Orders by PalletID -> {PalletID : Order}
        self.assigned_orders = {}

    def add_order(self, order):
        self.order_queue.append(order)

    def add_ws(self, id, workstation):
        self.workstationsById[id] = workstation

    def assign_order(self, pallet_id):
        if len(self.order_queue) != 0:
            print("PalletID:", pallet_id)
            self.assigned_orders[pallet_id] = self.order_queue.pop(0)
            print(self.assigned_orders)
        else:
            self.PrintLog("Cant assign order to pallet. No pending orders")

    def parse_conveyor_request(self, data):

        if len(data) == 0:
            self.PrintLog("empty request from conveyor")

        elif "Changed" in data["id"]:
            self.PrintLog("Zone change notification received")
            ws_id = workstation_id
            for c in data["id"]:
                if c.isdigit():
                    zone = c
            ###
            self.PrintLog(zone)

            # Call orchestrator to figure out what to do with the conveyor
            if data["payload"]["PalletID"] != "-1":  # Pallet arrived
                self.PrintLog("Pallet arrived")
                time.sleep(0.5)
                #self.workstationsById[ws_id].populate_zone(zone, -1)
                self.order_control(ws_id, zone, data["payload"]["PalletID"])

            else:  # Pallet left
                self.workstationsById[ws_id].populate_zone(zone, "-1")
                if zone == 2:
                    if self.workstationsById[ws_id].zone_status[1] != "-1":
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 1, 2)
                elif zone == 3:
                    if self.workstationsById[ws_id].zone_status[2] != "-1":
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 2, 3)
                elif zone == 4:
                    if self.workstationsById[ws_id].zone_status[1] != "-1":
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 1, 4)
                elif zone == 5:
                    if self.workstationsById[ws_id].zone_status[3] != "-1" and \
                            self.workstationsById[ws_id].recipe_iterator > 2:
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 3, 5)
                    elif self.workstationsById[ws_id].zone_status[4] != "-1":
                            self.transferZtoZ(self.workstationsById[
                                                  ws_id].conveyor, 4, 5)
        else:
            self.PrintLog("ERROR: Received an unknown request")

    def parse_robot_request(self, data):

        if len(data) == 0:
            self.PrintLog("empty request from robot")
        elif data["id"] == "DrawStartExecution":
            ws_id = workstation_id
            self.PrintLog("Started drawing " + str(data["payload"]))

        elif data["id"] == "DrawEndExecution":
            ws_id = workstation_id
            self.PrintLog("Ended drawing")
            self.workstationsById[ws_id].current_order.pop(0)
            if not self.workstationsById[ws_id].current_order:
                if self.workstationsById[ws_id].zone_status[5] == "-1":
                    self.transferZtoZ(self.workstationsById[ws_id].conveyor, 3, 5)
                else:
                    self.PrintLog("ERROR: Zone 5 is busy")
            else:
                self.workstationsById[ws_id].draw_recipes()
        else:
            self.PrintLog("ERROR: Received an unknown request")

    def parse_order(self, data):

        if len(data) == 0:
            self.PrintLog("empty request given as order")
        elif data["id"] == "order":
            self.PrintLog("Received a new order")
            self.add_order(data["order"])
        else:
            self.PrintLog("ERROR: Received an unknown request")

    """
    def parse_request(self, data):
        # Start by checking if the gotten data is a workstation event or an
        # order

        if len(data) == 0:
            print("empty request")

        elif data["id"] == "order":
            print("Request is an order")
            self.add_order(data["order"])

        elif data["id"] == "DrawStartExecution":
            ws_id = workstation_id
            print("Started drawing " + data["payload"])

        elif data["id"] == "DrawEndExecution":
            ws_id = workstation_id
            print("Ended drawing")
            self.workstationsById[ws_id].recipe_iterator += 1
            if self.workstationsById[ws_id].recipe_iterator > 2:
                if self.workstationsById[ws_id].zone_status[5] == "-1":
                    self.transferZtoZ(self.workstationsById[ws_id].conveyor, 3, 5)
                else:
                    self.PrintLog("ERROR: Zone 5 is busy")
            else:
                self.workstationsById[ws_id].draw_recipes()

        elif "Changed" in data["id"]:
            print("Zone change notification received")
            for c in data["id"]:
                if c.isdigit():
                    zone = c
            ws_id = workstation_id
            ###
            print(zone)
            # Call orchestrator to figure out what to do with the conveyor
            if data["payload"]["PalletID"] != "-1":  # Pallet arrived
                print("Pallet arrived")
                #self.workstationsById[ws_id].populate_zone(zone, -1)
                self.order_control(ws_id, zone, data["payload"]["PalletID"])

            else:  # Pallet left
                self.workstationsById[ws_id].populate_zone(zone, "-1")
                if zone == 2:
                    if self.workstationsById[ws_id].zone_status[1] != "-1":
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 1, 2)
                elif zone == 3:
                    if self.workstationsById[ws_id].zone_status[2] != "-1":
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 2, 3)
                elif zone == 4:
                    if self.workstationsById[ws_id].zone_status[1] != "-1":
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 1, 4)
                elif zone == 5:
                    if self.workstationsById[ws_id].zone_status[3] != "-1" and \
                            self.workstationsById[ws_id].recipe_iterator > 2:
                        self.transferZtoZ(self.workstationsById[
                                              ws_id].conveyor, 3, 5)
                    elif self.workstationsById[ws_id].zone_status[4] != "-1":
                            self.transferZtoZ(self.workstationsById[
                                                  ws_id].conveyor, 4, 5)

        else:
            print("Unknown request received")
            print(data)
    """

    def order_control(self, ws_id, current_zone, PalletId):

        #print("Order control")
        # Z1 -> Z2 -> Z3
        # If Z2 busy  Z1 -> Z4, remove from orders
        # If Z5 empty Z4 -> Z5
        # When Z3 finished -> Z5, remove from orders, report finished

        workstation = self.workstationsById[ws_id]
        conv = self.workstationsById[ws_id].conveyor

        if int(current_zone) == 1:
            #print("Zone 1")
            # Assign order to a pallet in the first zone
            workstation.zone_status[current_zone] = PalletId
            if (len(self.order_queue) > 0):
                self.assign_order(PalletId)
                # Check if Zone 2 is busy
                if workstation.zone_status[2] == "-1":
                    self.transferZtoZ(conv, current_zone, 2)
                    workstation.zone_status[1] = "-1"
                # Check if Zone 4 busy
                elif workstation.zone_status[4] == "-1":
                    self.PrintLog("Workstation full, discarding order")
                    del self.assigned_orders[PalletId]
                    self.transferZtoZ(conv, current_zone, 4)
                    workstation.zone_status[1] = "-1"
                # Error if both busy
                else:
                    self.PrintLog("ERROR: All zones full")
            else:  # No orders
                self.PrintLog("ERROR: No pending orders")
                self.transferZtoZ(conv, current_zone, 4)
                workstation.zone_status[1] = "-1"

        elif int(current_zone) == 2:
            if workstation.zone_status[3] == "-1":
                self.transferZtoZ(conv, current_zone, 3)
                workstation.zone_status[2] = "-1"
            else:
                self.PrintLog("Zone 3 is busy")

        elif int(current_zone) == 3:
            # Let workstation keep track of the drawing process
            workstation.update_current_order(self.assigned_orders[PalletId])
            workstation.draw_recipes()

        elif int(current_zone) == 4:
            if self.workstationsById[ws_id].zone_status[5] == "-1":
                self.transferZtoZ(conv, current_zone, 5)
                workstation.zone_status[4] = "-1"
            else:
                self.PrintLog("Zone 5 is busy")

        elif int(current_zone) == 5:
            self.PrintLog("Arrived at the end of current workstation")

    def transferZtoZ(self, conv, zone1, zone2):
        print("Transfer Z2Z")
        print(zone1 , " " , zone2)
        resp = conv.Transfer(zone1, zone2)
        str_resp = str(resp)
        if (str_resp == "<Response [202]>"):
            self.PrintLog(f"Transfer from Zone {zone1} ---> Zone"
                          f" {zone2} accepted")
        else:
            self.PrintLog(f"ERROR: Transfer from Zone {zone1} ---> Zone"
                          f" {zone2} "
                          f"failed")

    def PrintLog(self, msg):
        print(msg)


class Workstation:
    def __init__(self, id, conveyor, robot):
        self.id = id
        self.conveyor = conveyor
        self.robot = robot
        self.zone_status = self.GetAllStatuses()
        self.current_order = []

    def GetAllStatuses(self):
        statuses = {}
        for i in range(1, 6):
            serviceName = "http://" + self.conveyor.ipaddress + "/rest/services/Z" + str(
                i)
            print(serviceName)
            response = requests.post(serviceName, json={}, timeout=(2, 10))
            print(response.json())
            time.sleep(0.1)
            # 2 seconds connect 10 seconds response
            statuses[i] = str((response.json())["PalletID"])  # -1 if empty or PalletID
        print(statuses)
        return statuses

    def populate_zone(self, zone, pallet_id):
        self.zone_status[zone] = pallet_id

    def update_current_order(self, order):
        self.current_order = order

    def draw_recipes(self):
        resp = self.robot.draw(self.current_order[0])
        print(resp)
        if str(resp) == "<Response [202]>":
            print("Drawing accepted")
        else:
            print("Drawing declined")


class Robot:

    def __init__(self, ipaddress, resp_ipaddress):
        self.ipaddress = ipaddress
        self.resp_address = resp_ipaddress
        # Calibrate and wait until calibration is finished ~3 minutes
        #requests.post("http://" + ipaddress + "/rest/services/Calibrate", timeout=(2, 10))
        #time.sleep(180)

    def draw(self, recipe):
        serviceName = "http://" + self.ipaddress + "/rest/services/Draw" + str(recipe)
        payload = str("{\"destUrl\": \"" + self.resp_address + ":" + str(server_port) + "/robot" + "\"}")
        response = requests.post(serviceName, json=json.loads(payload), timeout=(2, 10))
        # 2 seconds connect 10 seconds response
        return response  # 202 or 404


class Conveyor:
    def __init__(self, ipaddress, resp_ipaddress):
        self.ipaddress = ipaddress
        self.resp_address = resp_ipaddress

    def Transfer(self, currentZone, destinationZone):
        serviceName = "http://" + self.ipaddress + "/rest/services/TransZone" + str(currentZone) + str(destinationZone)
        #payload = "{\"destUrl\":\"http://" + self.resp_address + ":5000}"
        payload = "{\"destUrl\":\"http://" + server_ip + ":" + str(server_port) + "\"}"
        #payload = str("{\"destUrl\": \"" + self.resp_address, "\"}")
        response = requests.post(serviceName, json=json.loads(payload), timeout=(4, 10))
        # 2 seconds connect 10 seconds response
        return response  # 202 or 404




app = Flask(__name__)

limiter = Limiter(app,
                key_func=get_remote_address,
                default_limits=["1/second"])


@app.route('/', methods=['POST'])
@limiter.exempt
def default():
    data = request.json
    return data


@app.route('/robot', methods=['POST'])
@limiter.limit("1 per second")
def parse_robot():
    data = request.json
    print("GOT EVENT FROM ROBOT")
    #print(data)
    orchestrator.parse_robot_request(data)
    return data


@app.route('/conveyor', methods=['POST'])
@limiter.limit("1 per second")
def parse_conveyor():
    data = request.json
    print("GOT EVENT FROM CONVEYOR")
    #print(data)
    orchestrator.parse_conveyor_request(data)
    return data


@app.route('/order', methods=['POST'])
@limiter.limit("1 per second")
def parse_order():
    data = request.json
    print("GOT ORDER")
    #print(data)
    orchestrator.parse_order(data)
    return data


conv_ip = "192.168.10.2"
robot_ip = "192.168.10.1"
server_ip = "192.168.0.50"
server_port = 5000
workstation_id = 12

# Subscription payload
#payload = "{\"destUrl\":\"http://" + server_ip + ":" + str(server_port) + "\"}"


# Subscribe to conveyor events
for i in range(1, 6):
    serviceName = "http://" + conv_ip + "/rest/events/Z" + str(
        i) + "_Changed/notifs"
    payload = "{\"destUrl\":\"http://" + server_ip + ":" + str(
        server_port) + "/conveyor" + "\"}"
    response = requests.post(serviceName, json=json.loads(payload),
                             timeout=(4, 10))
    print(response)

payload = "{\"destUrl\":\"http://" + server_ip + ":" + str(
        server_port) + "/robot" + "\"}"
# Subscribe to robot draw events
serviceName = "http://" + robot_ip + "/rest/events/DrawStartExecution/notifs"
response = requests.post(serviceName, json=json.loads(payload),
                         timeout=(4, 10))
print(response)
serviceName = "http://" + robot_ip + "/rest/events/DrawEndExecution/notifs"
response = requests.post(serviceName, json=json.loads(payload),
                         timeout=(4, 10))
print(response)

# Create the objects
conveyor = Conveyor(conv_ip, server_ip)
robot = Robot(robot_ip, server_ip)
workstation = Workstation(workstation_id, conveyor, robot)
orchestrator = Orchestrator(server_ip)
orchestrator.add_ws(workstation.id, workstation)

if __name__ == '__main__':
    app.run(host=server_ip, port=server_port)  # host="0.0.0.0",
