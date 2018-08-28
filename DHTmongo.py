import pymongo
import serial
import time    
import paho.mqtt.client as mqtt
import json
from flask import Flask,url_for, request, render_template
# import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
DHTdb = myclient["DHTdata"]

app = Flask(__name__)

def Test():
    # global GLO
    temp = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return temp


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor1")

def on_message(client, userdata, msg):
    date_time = Test()
    # now = datetime.datetime.now()
    # print(now)   
    date = date_time[0:10]
    time = date_time[11:19]
    # print(date_time)
    DHT = str(msg.payload)
    DHTcol = DHTdb[str(msg.topic)]
    number = DHTcol.find().count()
    print(number)
    if(len(DHT)==24):
        humidity = DHT[2:7]
        celsius = DHT[9:14]
        fahrenheit = DHT[16:21]
        number += 1
        DHT_data = {"_id" : number, "humidity" : humidity, "celsius" : celsius, "fahrenheit" : fahrenheit, "date" : str(date), "time" : str(time)}
        print(DHT_data)
        insertData = DHTcol.insert_one(DHT_data)

    # for data in DHTcol.find():
    #     print(data)

@app.route('/')
def index():
    datalist = []
    DHTcol = DHTdb["sensor1"]
    for data in DHTcol.find():
        print(data)
        datalist.append(data)
    return render_template('index.html', selectlist=datalist)

@app.route('/api/mongo/DHTdata/<sensor>/<key>/<c>', methods=['GET'])
def pub_my_msg(sensor, key, c):
    selectlist = []
    if len(sensor) == 0 or len(c) == 0 or len(key) == 0:
        abort(404)
    DHTcol = DHTdb[sensor]
    myquery = { key : c }
    for DHTdoc in DHTcol.find(myquery):
        selectlist.append(DHTdoc)
    print(selectlist)
    return render_template('index.html', selectlist=selectlist)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message    
    client.connect('127.0.0.1')
    client.loop_start()

    app.run(host='127.0.0.1', debug = False)
    

    