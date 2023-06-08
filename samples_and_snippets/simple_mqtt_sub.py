import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage

class TestInClass:
    BROKER, PORT = "localhost", 1883

    def on_message(client, userdata, msg):
        print(f'Received {msg.payload.decode()}')

    client = paho.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.subscribe("lot/sensor")
    client.loop_forever()


if __name__ == '__main__':
    # TODO: Run each of these classes in a separate terminal. You should see the CarParkDisplay update when you click the buttons in the CarDetector.
    # These classes are not designed to be used in the same module - they are both blocking. If you uncomment one, comment-out the other.

    TestInClass()
    # CarDetector()
