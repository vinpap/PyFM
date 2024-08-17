"""
Contains all the GUI-related functions.
"""
import tkinter as tk


def setup_gui():
    """
    Sets up the main window and all the necessay widgets.
    """
    ...
    

def main_loop():
    """
    Runs the main execution loop
    """
    window = tk.Tk()
    window.geometry("300x200")
    window.title("PyFM")
    frame = tk.Frame(window)
    frame.pack()

    freq_selector = tk.Spinbox(from_=88, to=108, increment=0.01)
    freq_selector.pack()

    ok_btn = tk.Button(
    text="Set frequency",
    )
    ok_btn.pack()
    window.mainloop()

def change_frequency(new_frequency: float):
    """
    Called upon clicking the button to change the FM frequency to listen to.
    """
    ...