import threading

from radio_processing import listen_fm_live
from gui import GUI


if __name__ == "__main__":
    
    # TODO: Lancer listen_fm_live dans un thread différent
    # Partager les infos suivantes avec le thread principal :
    # - booléen qui indique s'il faut quitter ou non
    # - fréquence radio à jouer

    quit_event = threading.Event()
    gui = GUI(quit_event=quit_event)
    gui_thread = threading.Thread(target=gui.gui_loop)

    gui_thread.start()
    listen_fm_live(87.7e6, quit_event)
    gui_thread.join()
    
