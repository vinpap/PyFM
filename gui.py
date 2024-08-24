"""
Contains all the GUI-related functions.
"""
import threading
import tkinter as tk

class GUI:

    def __init__(self, quit_event: threading.Event):
        self.quit_event = quit_event

    def setup_gui(self):
        """
        Sets up the main window and all the necessay widgets.
        """
        ...
        

    def gui_loop(self):
        """
        Runs the main GUI execution loop
        """
        window = tk.Tk()
        window.geometry("300x200")
        window.title("PyFM")
        frame = tk.Frame(window)
        frame.pack()

        freq_selector = tk.Spinbox(from_=80, to=108, increment=0.01)
        freq_selector.pack()

        ok_btn = tk.Button(
        text="Set frequency",
        )
        ok_btn.pack()

        window.protocol("WM_DELETE_WINDOW", lambda arg=window: self.on_closing(arg))
        window.mainloop()

    def change_frequency(self, new_frequency: float):
        """
        Called upon clicking the button to change the FM frequency to listen to.
        """
        ...

    def on_closing(self, window):
        """
        Called upon closing the main window.
        """
        self.quit_event.set()
        window.destroy()

    
