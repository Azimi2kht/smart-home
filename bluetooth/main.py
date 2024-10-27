import paho.mqtt.client as mqtt
import random
import time
import asyncio
from bleak import BleakScanner

# ThingsBoard MQTT broker details
THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "ReO62g53vHv7iJYiFjpU"


# Callback function when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code " + str(rc))
    client.subscribe("v1/devices/me/telemetry")


# Callback function when the client receives a message from the server
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def get_item_with_least_rssi(data):
    if not data:
        return None
    return min(data, key=lambda x: x["rssi"])


def tb_publish(mac):
    tb_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    tb_client.username_pw_set(ACCESS_TOKEN)

    tb_client.connect(THINGSBOARD_HOST, 1883, 60)
    tb_client.publish(
        "v1/devices/me/telemetry", '{{"bluetooth_mac": {}}}'.format(90))
    time.sleep(5)
    tb_client.disconnect()


async def scan_ble_devices():
    devices = await BleakScanner.discover(return_adv=True)
    devices = devices.items()
    ble_data = []

    for device in devices:
        rssi = device[1][1].rssi
        mac = device[0]
        if rssi > -40: 
            ble_data.append({"mac": mac, "rssi": rssi}) 
        
    print(ble_data)
                        
	
    return ble_data


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
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
        # Scan for BLE devices
        ble_devices = asyncio.run(scan_ble_devices())

except KeyboardInterrupt:
    pass

# Disconnect from ThingsBoard MQTT broker
client.loop_stop()
client.disconnect()
