# Car Park System

This repository contains a car park system implementation. It consists of the following components:

- `config_parser.py`: A module that parses a JSON configuration file and converts it to TOML format.
- `car_detector.py`: A module that simulates a car detector and publishes car detection events using MQTT.
- `car_park_display.py`: A module that displays the car park information in a graphical window.
- `windowed_display.py`: A module that provides a windowed display for the car park information.
- `config.json`: A sample configuration file in JSON format.

## Prerequisites
To run the car park system, you need to have the following dependencies installed:

- Python 3.x
- Paho MQTT library (`pip install paho-mqtt`)
- Tkinter library (included with most Python installations)
- TOML library (`pip install toml`)

Additionally, you need to have a running instance of the Mosquitto MQTT broker. You can install it locally or use a cloud-based MQTT broker service.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/SicrosoftMurface/civ-ipriot-proj-carpark.git
   ```
   
2. Install the required dependencies as mentioned in the prerequisites section.
3. Configure the `config.json` file according to your car park settings. Make sure it is a valid JSON file.

## Usage

Follow the steps below to run the car park system.
Each step requires open a terminal or command prompt and navigating to the correct project subdirectory to run the following commands.

1. Generate the TOML configuration file:

   ```shell
   python config_parser.py
   ```
Run the config_parser.py file to convert the config.json file to config.toml:

2. Run the car park display:

   ```shell
   python carpark_display.py
   ```
This will open a graphical window showing the car park information.

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

## Running the Unit Tests

The unit tests are implemented using the `unittest` framework. To run the tests, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to execute the unit tests:

   ```shell
   python -m unittest discover tests
   ```
   
This command will discover and run all the test cases located in the `tests` directory.
Due to the nature of how these tests work, make sure to close the car detector display by pressing `x` each time it pops up during the tests.

Note: Make sure you have the correct directory structure and file names as mentioned in the previous instructions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.