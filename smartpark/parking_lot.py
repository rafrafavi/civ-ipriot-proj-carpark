### Class: ParkingLot

import paho.mqtt.client as mqtt


class ParkingLot:

    def __init__(self, config) -> None:
        """Initialize the ParkingLot object with the given configuration."""
        # The parking lot's location.
        self.location = config["location"]
        # The total number of parking spaces.
        self.total_spaces = config["total_spaces"]
        # The number of available parking spaces.
        self.available_spaces = config["total_spaces"]
        # The MQTT client to send and receive messages.
        self.mqtt_client = None
        # MQTT Client Name
        self.mqtt_client_name = "L306-24"
        # MQTT Keep Alive value in seconds
        # Notify server we are still here, and is usually about 300s
        self.mqtt_keep_alive = 60
        # MQTT Broker/Server host name
        self.mqtt_host = config["broker_host"]
        # MQTT Broker/Server communications port
        self.mqtt_port = config["broker_port"]

        self.mqtt_connect()
        # The code never goes past this line...
        # Any code you want to run, needs to be triggered by
        # an event that occurs. These are the on_...
        self.mqtt_client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.publish("test/topic", "Hello from Python Paho!")

    def on_message(self, client, userdata, msg):
        print(f"{msg.topic}: {msg.payload.decode()}")

    def mqtt_connect(self) -> None:
        client_name = self.mqtt_client_name
        host = self.mqtt_host
        port = self.mqtt_port
        keep_alive = self.mqtt_keep_alive

        self.mqtt_client = mqtt.Client(client_name)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(host, port, keep_alive)

    def enter(self):
        """Register a car entering the parking lot."""
        pass

    def exit(self):
        """Register a car leaving the parking lot."""
        pass

    def publish_update(self):
        """Publish an update containing available_spaces, temperature, and time."""
        pass
