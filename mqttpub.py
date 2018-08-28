import serial
import paho.mqtt.client as mqtt
ser = serial.Serial("/dev/ttyACM1",9600) 
print(ser.name)


while True:
    data = ser.readline()
    print(data)
    print(len(str(data)))
    client = mqtt.Client()
    client.connect("127.0.0.1")
    client.publish("sensor1", data)     
#topic = "plusone"
#payload = "hello mqtt"
 


# If broker asks client ID.