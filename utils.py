"""
Miscallenous utility classes and functions.
"""

import numpy as np
from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.pyplot import figure, show

class Mfloat:
    """
    This class only stores a float: its instances are meant to be passed
    to functions so they can be used as mutable floats (floats are immutable
    in Python).
    """
    def __init__(self, value: float):
        self.__value = value
        # String representation in MHz
        self.str_value = str(self.__value/1000000) 
    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, new_value: float):
        self.__value = new_value
        self.str_value = str(new_value/1000000)




def plot_radio_input(center_frequency: float, sample_rate: float = 250e3):
    """
    Plots in real time the signal received by a RTL radio receiver. This
    function offers a quick way to make sure your RTL receiver is working.
    """

    sdr = RtlSdr()
    sdr.sample_rate = sample_rate  # Hz
    sdr.center_freq = center_frequency  # Hz
    sdr.freq_correction = 60  # PPM
    sdr.bandwidth = 50000
    sdr.gain = "auto"

    def animate(i):
        """
        Reads the incoming signal and plot it real-time
        """
        graph_out.clear()
        samples = sdr.read_samples(512 * 2048)

        # use matplotlib to estimate and plot the PSD
        graph_out.psd(
            samples, NFFT=1024, Fs=sdr.sample_rate / 1e5, Fc=sdr.center_freq / 1e6
        )
        # graph_out.xlabel('Frequency (MHz)')
        # graph_out.ylabel('Relative power (dB)')

    fig = figure()
    graph_out = fig.add_subplot(1, 1, 1)
    try:
        ani = animation.FuncAnimation(fig, animate, interval=5)
        show()
    except KeyboardInterrupt:
        pass
    finally:
        sdr.close()


def plot_spectrogram(center_frequency: float, sample_rate: float = 250e3):

    sdr = RtlSdr()
    sdr.sample_rate = sample_rate  # Hz
    sdr.center_freq = center_frequency  # Hz
    sdr.freq_correction = 60  # PPM
    sdr.bandwidth = 500000
    sdr.gain = "auto"
    fft_size = 1024
    num_rows = 500
    x = sdr.read_samples(2048)  # get rid of initial empty samples
    x = sdr.read_samples(
        fft_size * num_rows
    )  # get all the samples we need for the spectrogram
    spectrogram = np.zeros((num_rows, fft_size))
    for i in range(num_rows):
        spectrogram[i, :] = 10 * np.log10(
            np.abs(np.fft.fftshift(np.fft.fft(x[i * fft_size : (i + 1) * fft_size])))
            ** 2
        )
    extent = [
        (sdr.center_freq + sdr.sample_rate / -2) / 1e6,
        (sdr.center_freq + sdr.sample_rate / 2) / 1e6,
        len(x) / sdr.sample_rate,
        0,
    ]
    plt.imshow(spectrogram, aspect="auto", extent=extent)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Time [s]")
    plt.show()
