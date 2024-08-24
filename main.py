import threading

from gui import GUI
from radio_processing import listen_fm_live
from utils import Mfloat


if __name__ == "__main__":
    
    # TODO: Lancer listen_fm_live dans un thread différent
    # Partager les infos suivantes avec le thread principal :
    # - booléen qui indique s'il faut quitter ou non
    # - fréquence radio à jouer

    frequency = Mfloat(87.7e6)

    quit_event = threading.Event()
    gui = GUI(quit_event=quit_event, frequency=frequency)
    gui_thread = threading.Thread(target=gui.gui_loop)

    gui_thread.start()
    listen_fm_live(frequency, quit_event)
    gui_thread.join()
    
