import asyncio

from matplotlib.pyplot import *
from matplotlib import animation
from rtlsdr import RtlSdr




def live_plot():
    """
    Plots in real time the signal received by the radio receiver.
    """

    def animate(i):
        """
        Reads the incoming signal and plot it real-time
        """
        graph_out.clear()
        samples = sdr.read_samples(512*1024)

        # use matplotlib to estimate and plot the PSD
        graph_out.psd(samples, NFFT=1024, Fs=sdr.sample_rate /
                    1e6, Fc=sdr.center_freq/1e6)
        #graph_out.xlabel('Frequency (MHz)')
        #graph_out.ylabel('Relative power (dB)')

    fig = figure()
    graph_out = fig.add_subplot(1, 1, 1)
    try:
        ani = animation.FuncAnimation(fig, animate, interval=10)
        show()
    except KeyboardInterrupt:
        pass
    finally:
        sdr.close()

def play_audio_sample():
    """
    Plays a short audio sample from the radio station being received.
    """
    from scipy.io.wavfile import write
    import numpy as np

    #samples = sdr.read_samples(256*1024)
    plot(samples)
    """rate = 44100
    #scaled = np.int16(samples / np.max(np.abs(samples)) * 32767)
    write('test.wav', rate, samples)"""


if __name__ == "__main__":
    sdr = RtlSdr()
    sdr.sample_rate = 2.048e6 # Hz
    sdr.center_freq = 95.5e6   # Hz
    sdr.freq_correction = 60  # PPM
    sdr.bandwidth = 50000
    sdr.gain = 'auto'
    live_plot()
    #play_audio_sample()

    

