import paho.mqtt.client as paho
class MqttDevice:
    def __init__(self, config, device_name='sensor'):
        self.name = config['name']
        self.location = config['location']

        # Define topic components:
        self.topic_root = config['topic-root']
        self.topic_qualifier = config['topic-qualifier']
        self.topic_device = device_name
        self.topic = self._create_topic_string()

        # Configure broker
        self.broker = config['broker']
        self.port = config['port']

        # initialise a paho client and bind it to the object (has-a)

        self.client = paho.Client()
        self.client.connect(self.broker,
                            self.port)

    def _create_topic_string(self):
        return (f"{self.topic_root}/{self.location}/" +
                f"{self.topic_device}/{self.topic_qualifier}")