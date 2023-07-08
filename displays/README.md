# Car Park System

This project implements a real-time car park system using Python and MQTT.

## Prerequisites

- Python 3.x
- Paho MQTT library (`pip install paho-mqtt`)
- Tkinter library (included with most Python installations)
- TOML library (`pip install toml`)
- Mosquitto broker (MQTT broker)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/SicrosoftMurface/civ-ipriot-proj-carpark.git
   ```
2. Install the required libraries:

   ```shell
   pip install paho-mqtt toml
   ```

3. Start the Mosquitto broker:
Make sure you have the Mosquitto broker service running on your machine. If you don't have it installed, you can download it from the official Mosquitto website: https://mosquitto.org/download/
Once installed, start the Mosquitto broker service.

## Usage

Follow the steps below to run the car park system:

1. Generate the TOML configuration file:
Run the config_parser.py file to convert the config.json file to config.toml:

   ```shell
   python config_parser.py
   ```

2. Run the car park display:

   ```shell
   python carpark_display.py
   ```
This will start the car park display application.

3. Run the car detector:

   ```shell
   python car_detector.py
   ```
This will start the car detector application.

4. MQTT Publish and Subscribe (Optional):

If you want to test the MQTT functionality separately, you can use the mqtt_pub.py and mqtt_sub.py files.

Run the mqtt_pub.py file to publish a test message:

   ```shell
   python mqtt_pub.py
   ```

Run the mqtt_sub.py file to subscribe to the MQTT topic and print received messages:

   ```shell
   python mqtt_sub.py
   ```

This will subscribe to the "lot/sensor" topic and print the received messages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.