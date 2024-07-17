import asyncio

from matplotlib.pyplot import *
from matplotlib import animation
from rtlsdr import RtlSdr

"""sdr = RtlSdr()
sdr.sample_rate = 2.048e6 # Hz
sdr.center_freq = 95.5e6   # Hz
sdr.freq_correction = 60  # PPM
sdr.gain = 'auto'

#print(len(sdr.read_samples(1024)))
samples = sdr.read_samples(256*1024)
sdr.close()

# use matplotlib to estimate and plot the PSD
psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')

show()"""


sdr = RtlSdr()
sdr.sample_rate = 2.048e6 # Hz
sdr.center_freq = 95.5e6   # Hz
sdr.freq_correction = 60  # PPM
sdr.gain = 'auto'

fig = figure()
graph_out = fig.add_subplot(1, 1, 1)

def animate(i):
    graph_out.clear()
    samples = sdr.read_samples(256*1024)

    # use matplotlib to estimate and plot the PSD
    graph_out.psd(samples, NFFT=1024, Fs=sdr.sample_rate /
                  1e6, Fc=sdr.center_freq/1e6)
    #graph_out.xlabel('Frequency (MHz)')
    #graph_out.ylabel('Relative power (dB)')


try:
    ani = animation.FuncAnimation(fig, animate, interval=10)
    show()
except KeyboardInterrupt:
    pass
finally:
    sdr.close()


async def streaming():
    sdr = RtlSdr()
    sdr.sample_rate = 2.048e6 # Hz
    sdr.center_freq = 95.5e6   # Hz
    sdr.freq_correction = 60  # PPM
    sdr.gain = 'auto'

    async for samples in sdr.stream():
        print(samples)

    # to stop streaming:
    await sdr.stop()

    # done
    sdr.close()

"""loop = asyncio.get_event_loop()
loop.run_until_complete(streaming())"""
