import time  # Import the time library for using sleep (pauses)
import digitalio  # Library for handling digital IO
import board  # Library for accessing the pins of the Raspberry Pi Pico
import usb_hid  # Library for USB HID communication
from adafruit_hid.keyboard import Keyboard  # Import the Keyboard class
from adafruit_hid.keycode import Keycode  # Import the Keycode class for special keys

# Time in seconds
DELAY = 0.1

# Define the buttons as constants
BTN_GP15 = board.GP15
BTN_GP14 = board.GP14
BTN_GP13 = board.GP13
BTN_GP12 = board.GP12
BTN_GP11 = board.GP11

# Initialize keyboard
keyboard_ = Keyboard(usb_hid.devices)


# Function to configure buttons
def configure_button(pin):
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    return button


# Configure buttons
BTN_GP15 = configure_button(BTN_GP15)  # Scene 1
BTN_GP14 = configure_button(BTN_GP14)  # Scene 2
BTN_GP13 = configure_button(BTN_GP13)  # Scene 3
BTN_GP12 = configure_button(BTN_GP12)  # Stop Streaming
BTN_GP11 = configure_button(BTN_GP11)  # Start Streaming


# Function to handle key presses and releases
def press_and_release(keyboard, *keycodes):
    keyboard.press(*keycodes)
    time.sleep(DELAY)
    keyboard.release(*keycodes)


# Main loop
while True:
    if BTN_GP15.value:
        print("BTN_GP15")
        press_and_release(
            keyboard_, Keycode.CONTROL, Keycode.SHIFT, Keycode.ONE
        )  # Scene 1
    if BTN_GP14.value:
        print("BTN_GP14")
        press_and_release(
            keyboard_, Keycode.CONTROL, Keycode.SHIFT, Keycode.TWO
        )  # Scene 2
    if BTN_GP13.value:
        print("BTN_GP13")
        press_and_release(
            keyboard_, Keycode.CONTROL, Keycode.SHIFT, Keycode.THREE
        )  # Scene 3
    if BTN_GP12.value:
        print("BTN_GP12")
        press_and_release(
            keyboard_, Keycode.CONTROL, Keycode.SHIFT, Keycode.A
        )  # Stop Streaming
    if BTN_GP11.value:
        print("BTN_GP11")
        press_and_release(
            keyboard_, Keycode.CONTROL, Keycode.SHIFT, Keycode.S
        )  # Start  Streaming
    time.sleep(DELAY)