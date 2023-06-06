import paho.mqtt.client as mqtt

class parking_lot:
    def __init__(self, config):
        self.location = config.get('location')
        self.total_spaces = config.get('total_spaces')
        self.available_spaces = config.get('total_spaces')
        self.mqtt_client = mqtt.Client()

        # Connect MQTT client to the broker
        self.mqtt_client.connect("mqtt_broker_address", 1883, 60)

        # Set MQTT client callbacks
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_publish = self.on_publish

        # Start the MQTT client loop in a non-blocking manner
        self.mqtt_client.loop_start()

    def enter(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            self.publish_update()
            print("Car entered the parking lot.")
        else:
            print("No available parking spaces.")

    def exit(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            self.publish_update()
            print("Car exited the parking lot.")
        else:
            print("No cars in the parking lot.")

    def publish_update(self):
        available_spaces = self.available_spaces()
        temperature = self.get_temperature()  # Method to retrieve temperature
        time = self.get_current_time()  # Method to retrieve current time

        message = {
            'available_spaces': self.available_spaces,
            'temperature': temperature,
            'time': time
        }

        # Publish the message to a specific MQTT topic
        self.mqtt_client.publish("parking_lot_updates", str(message))

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code " + str(rc))

    def on_publish(self, client, userdata, mid):
        print("Message published with mid " + str(mid))



# Example usage:
config = {
    'location': 'Parking Lot A',
    'total_spaces': 10
}