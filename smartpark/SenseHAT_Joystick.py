from sense_hat import SenseHat

sense = SenseHAT()

def handle_joystick(event):
    event.action == "pressed"

sense.stick.direction_up = handle_joystick(event)