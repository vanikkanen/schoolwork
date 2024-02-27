
from flask import Flask, render_template,request
import threading
import paho.mqtt.client as mqtt
import sqlite3
import json
import datetime


app = Flask(__name__)

threadStarted = False

robot_list = ['rob1', 'rob2', 'rob3', 'rob4', 'rob5', 'rob6', 'rob7', 'rob8', 'rob9', 'rob10']

@app.route('/hello', methods=['GET'])
def helloWorld():
    print("Hello world endpoint")
    return "Hello World"
@app.route('/dashboard/')
def index():
    return render_template('dashboard.html')
@app.route('/measurement-history/')
def history():
    return render_template('measurement-history.html')
@app.route('/event-history/')
def alarm():
    return render_template('event-history.html')


@app.route('/<string:page_name>/')
def static_page(page_name):
    nID = request.args.get('nID')
    return render_template('%s.html' % page_name, nID=nID)


@app.route('/start', methods=['GET'])
def startThreads():
    print("Start threads attempt")
    global threadStarted
    if threadStarted:
        return "Threads have started already"
    else:
        threadStarted = True
        # Mqtt
        x = threading.Thread(target=startSubscription)
        x.start()

        return "Starting threads"


@app.route('/rob/<string:number>/latest', methods=['GET'])
def get_latest_by_robot_id(number):
    robot_id = "rob"+number
    return get_latest_by_deviceId(robot_id)


@app.route('/rob/<string:number>', methods=['GET'])
def get_by_robot_id(number):
    robot_id = "rob"+number
    return get_by_deviceId(robot_id)


@app.route('/rob/<string:number>/<string:startdate>/<string:enddate>',
           methods=['GET'])
def get_by_date_range(number, startdate, enddate):
    robot_id = "rob" + number
    return get_between_dates(robot_id, startdate, enddate)


# DATABASE
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def init_database():
    global conn
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.row_factory = dict_factory

    global c
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS message;")
    c.execute("""CREATE TABLE IF NOT EXISTS message (
                 deviceId text,
                 state text,
                 time text,
                 sequenceNumber integer
                 );""")


# CREATE
# new entry
def insert_message(id, state, time, sequenceNumber):
    with conn:
        c.execute("INSERT INTO message VALUES (:deviceId,:state, :time, "
                  ":sequenceNumber)",
                  {'deviceId': id, 'state': state, 'time': time,
                         'sequenceNumber': sequenceNumber})


# READ
# All for a certain robot
def get_by_deviceId(deviceId):
    sqlSt="SELECT * FROM message WHERE deviceId='"+deviceId+"'"
    c.execute(sqlSt)
    return c.fetchall()


# Latest for certain robot
def get_latest_by_deviceId(deviceId):
    sqlSt="SELECT * FROM message WHERE deviceId='"+deviceId+"' ORDER BY " \
            " sequenceNumber DESC LIMIT 1;"
    c.execute(sqlSt)
    return c.fetchall()

# All from specific time period for certain robot
def get_between_dates(deviceId, startdate, enddate):
    sqlSt = "SELECT * FROM message WHERE time BETWEEN '"+startdate+"' AND '"+enddate+"'" \
            "AND deviceId='"+deviceId+"'"
    c.execute(sqlSt)
    return c.fetchall()


#Mqtt on message
def on_message(client, userdata, msg):
    print ("Got some Mqtt message ")
    print(msg.topic+" "+str(msg.payload))
    topic_parts = msg.topic.split('/')
    if topic_parts[2] in robot_list:
        msg_dict = json.loads(msg.payload)
        # convert time stamp to correct format
        d = datetime.datetime.strptime(msg_dict["time"][:len(msg_dict["time"])-4],
                       "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S")

        insert_message(msg_dict["deviceId"], msg_dict["state"], str(d),
                   msg_dict["sequenceNumber"])


#Mqtt thread
def startSubscription():
    print("Mqtt subscription started....")
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.mqttdashboard.com")
    client.subscribe("ii22/telemetry/#") #subscribe all nodes
    init_database()

    rc = 0
    while rc == 0:
        rc = client.loop()


if __name__ == '__main__':
    app.run()
