class MqttDevice:
    def __init__(self, config):
        self.name = config['name']
        self.location = config['location']
        self.topic = config['topic']
        self.broker = config['broker']
        self.port = config['port']
        self.client = paho.Client()
        self.client.connect(self.broker,
                            self.port)
        self.type = config['type']  #entry and exit

        #initialise a paho client and bind it to the object(has-a)

        client = paho.Client()
        client.connect(self.broker,
                       self.port)
        client.publish("lot/sensor", "Car Detected")



    def on_detection(self, message):
        """The method that is triggered when a detection occurs"""
        message = f'{self.type}, {message}'
        print(message)
        self.client.publish(self.topic, message)

    def start_sensing(self):
        """a blocking event loop that waits for detection events, in this case"""
        while True:
            reply = input("Is there a car?")
            if reply == 'y':
                self.on_detection("Car, I saw a car!!")
            elif reply == 'n':
                self.on_detection("Car, I saw a car!!")
