import paho.mqtt.client as mqtt
import toml


class MqttDevice:
    def __init__(self, config):
        self.name = config['config']['name']
        self.location = config['config']['location']

        # Define topic components:
        self.topic_root = config['config']['topic_root']
        self.topic_qualifier = config['config']['topic_qualifier']
        self.topic = self._create_topic_string()

        # Configure broker
        self.broker = config['config']['broker_host']
        self.port = config['config']['broker_port']

        # initialise a mqtt client and bind it to the object (has-a)
        self.client = mqtt.Client()
        self.client.connect(self.broker, self.port)

    def _create_topic_string(self):
        return f"{self.name} / {self.topic_qualifier} / {self.topic_root} / {self.location}"