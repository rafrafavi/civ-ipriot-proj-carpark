import paho.mqtt.subscribe as subscribe

if __name__ == '__main__':
    # Subscribe to the lot topic and print received messages
    msg = subscribe.simple("lot/sensor", hostname="localhost")
    print(msg.payload.decode())
