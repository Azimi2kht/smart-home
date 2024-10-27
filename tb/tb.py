import paho.mqtt.client as mqtt
import random
import time
import json

# ThingsBoard MQTT broker details
THINGSBOARD_HOST = 'thingsboard.cloud'
ACCESS_TOKEN = 'oc4JYo0py7EzX2tIHRkE'

# Callback function when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("v1/devices/me/telemetry")
    client.subscribe('v1/devices/me/rpc/request/+')


# Callback function when the client receives a message from the server
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    x = msg.payload
    data_str = x.decode('utf-8')
    data_dict = json.loads(data_str)
    temperature = data_dict["params"]["temperature"]
    humidity = data_dict["params"]["brightness"]

    print(temperature, humidity)

    save_data(temperature, humidity, "preferred.txt")


def save_data(temperature, brightness, file_path):
    with open(file_path, 'w') as file:
        file.write(f"{temperature},{brightness}\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard MQTT broker
client.connect(THINGSBOARD_HOST, 1883, 60)

# Start the loop
client.loop_start()

try:
    while True:
        # Generate a random integer
        time.sleep(1)
       
        # Publish the data to the telemetry topic
       # client.publish("v1/devices/me/telemetry", '{{"bluetooth_mac": {}}}'.format(data))
        #client.publish("v1/devices/me/telemetry", '{{"bluetooth_mac": {}}}'.format(data))
        # Wait for some time before sending the next data
        
        

except KeyboardInterrupt:
    pass

# Disconnect from ThingsBoard MQTT broker
client.loop_stop()
client.disconnect()
