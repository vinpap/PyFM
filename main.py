"""
Run this script to open the radio.
"""
import threading

from gui import GUI
from radio_processing import listen_fm_live
from utils import Mfloat


if __name__ == "__main__":
    # FM frequency that is opened by default upon running the software
    frequency = Mfloat(87.7e6)

    # Two threads are run: one for the GUI and the other for the radio reception
    # and processing
    quit_event = threading.Event()
    gui = GUI(quit_event=quit_event, frequency=frequency)
    gui_thread = threading.Thread(target=gui.gui_loop)

    gui_thread.start()
    listen_fm_live(frequency, quit_event)
    gui_thread.join()
    
