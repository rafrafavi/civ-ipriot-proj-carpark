import paho.mqtt.publish as publish

if __name__ == '__main__':
    # Publish a test message
    publish.single("lot/sensor", "Hello from Python", hostname="localhost")
