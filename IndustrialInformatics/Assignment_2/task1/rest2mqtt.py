"""
AUT.840 Industrial Informatics
Assignment 2,Task 1

Authors: Jukka Hirvonen, Valtteri Nikkanen, Jouni Kokkonen

This program forwards received FASTORY line REST events to MQTT.
"""

import paho.mqtt.client as mqtt
import json
import time
import requests
from flask import Flask, request
from datetime import datetime

def parse(response):
    try:
        if response.get('senderID')[0:3] == "CNV":
            if response.get('payload') == {'PalletID': '-1'}:
                msg = response.get('senderID')+" reports "+response.get('id') + " to empty" + " at " + str(datetime.now())
            else:
                msg = response.get('senderID')+" reports "+response.get('id') + ", now contains pallet "+ str(response.get('payload')) + " at " + str(datetime.now())
        if response.get('senderID')[0:3] == "ROB":
            msg = response.get('senderID') + " reports " + response.get('id') + " " + str(response.get('payload')) + " at " + str(datetime.now())
    except:
        msg=response
    return(msg)

def subscribe(serviceName,payload):
    try:
        response = requests.post(serviceName, json=json.loads(payload),
                             timeout=(1, 6))
        print("Subscribing to " + serviceName + " \n " + str(response))
    except:
        print("Error subscribing to asset:" + serviceName)
        #print("Subscribing to " + serviceName + " \n " + str(response))
    time.sleep(.05)

def menu():
    global server_ip
    global server_port
    choice="x"
    while choice.lower() != "f":
        print("Please configure listening address. (current ip " + server_ip +", current port " + str(server_port) + ")")
        choice=str(input("Enter choice (P)ort, (I)P address, (F)inish: "))
        if choice.lower() == "p":
            server_port = str(input("Please enter listening port: "))
        if choice.lower() == "i":
            server_ip = str(input("Please enter listening ip address: "))

    choice="x"
    while choice.lower() != "f":
        print("Select assets to subscribe to. All events from conveyor or robot will be forwarded.\n"
              "To subscribe to custom assets, select \"other\".")
        choice=str(input("Enter choice (O)ther, (D)efault, (F)inish: "))
        if choice.lower() == "d":
            print("Subscribing to default set of assets.")
            # Subscribe to conveyor events
            for i in range(1, 6):
                serviceName = "http://" + conv_ip + "/rest/events/Z" + str(
                    i) + "_Changed/notifs"
                payload = "{\"destUrl\":\"http://" + server_ip + ":" + str(
                    server_port) + "/fw68452" + "\"}"
                subscribe(serviceName,payload)

            # Subscribe to robot draw events
            payload = "{\"destUrl\":\"http://" + server_ip + ":" + str(
                server_port) + "/fw68452" + "\"}"
            serviceName = "http://" + robot_ip + "/rest/events/DrawStartExecution/notifs"
            subscribe(serviceName,payload)
            serviceName = "http://" + robot_ip + "/rest/events/DrawEndExecution/notifs"
            subscribe(serviceName,payload)
        if choice.lower() == "o":
            serviceName = str(input("Please enter servicename to subscribe to (eg. http://192.168.10.1/rest/events/DrawStartExecution/notifs) : "))
            payload = str(input(
                "Please enter subscription payload (eg. {\"destUrl\":\"http://" + server_ip + ":" + str(
                server_port) + "/fw68452" + "\"}) : "))
            subscribe(serviceName, payload)
    print("Selections complete, starting client.")

# Default adresses
conv_ip = "192.168.10.2"
robot_ip = "192.168.10.1"
server_ip = "127.0.0.1"#"192.168.0.60" # "192.168.68.1" #"127.0.0.1"
server_port = 5000

menu()

app = Flask(__name__)

client = mqtt.Client()
client.connect("broker.mqttdashboard.com")

@app.route('/fw68452', methods=['POST'])
def forward():
    data = request.json
    print("Received event:")
    print(data)
    data = parse(data)
    print("Publishing to MQTT:\n" + data)
    client.publish("bluegoat897325oishdfhew/ii/task1/events", payload=str(data), qos=0,retain=False)
    return data

if __name__ == '__main__':
    app.run(host=server_ip, port=server_port)
