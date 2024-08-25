"""
Contains all the GUI-related functions.
"""
import threading
import tkinter as tk

from utils import Mfloat

class GUI:

    def __init__(self, quit_event: threading.Event, frequency: Mfloat):
        self.quit_event = quit_event
        self.frequency = frequency

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

        self.info_text = tk.Label(window, text="Select the frequency you want to listen to:")
        self.info_text.pack()
        self.info_text.pack(pady=30)

        self.spinner_value = tk.StringVar(window)
        self.spinner_value.set(self.frequency.str_value)
        freq_selector = tk.Spinbox(from_=80, to=108, increment=0.01, textvariable=self.spinner_value, width=30)
        freq_selector.pack(fill="y")
        self.spinner_value.trace_add('write', self.on_frequency_update)

        window.protocol("WM_DELETE_WINDOW", lambda arg=window: self.on_closing(arg))
        window.mainloop()


    def on_frequency_update(self, a, b, c):
        """
        Called when the user updates the frequency value in the spinner widget.
        """
        self.frequency.value = float(self.spinner_value.get())*1000000

    def on_closing(self, window):
        """
        Called upon closing the main window.
        """
        self.quit_event.set()
        window.destroy()

    
