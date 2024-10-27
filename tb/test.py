import paho.mqtt.client as mqtt

# پیکربندی کلاینت MQTT
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("v1/devices/me/telemetry")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # پردازش داده‌های دریافتی
    data = json.loads(msg.payload)
    light_intensity = data.get('lightIntensity')
    temperature = data.get('temperature')
    print(f'Light Intensity: {light_intensity}, Temperature: {temperature}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# اتصال به سرور MQTT ThingsBoard
client.username_pw_set("YOUR_ACCESS_TOKEN")
client.connect("YOUR_THINGSBOARD_HOST", 1883, 60)

# شروع حلقه دریافت پیام‌ها
client.loop_forever()
