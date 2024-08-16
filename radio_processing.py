"""
This file contains functions used to process raw radio signal in order to
convert it into sound data.
"""

import numpy as np
from scipy.io import wavfile
from scipy.signal import bilinear, lfilter

def fm_to_wav(input_filepath: str, ouptut_filepath: str, sample_rate: float=250e3):
    """
    Converts the raw radio data stored in the file specified by input_filepath
    into a wav file saved at output_filepath.
    This code is based on Dr. Marc Lichtman's book "PySDR: A Guide to SDR and 
    DSP using Python".  

    input_filepath (str): path to the file that contains the raw radio data
    stored using IQ sampling.
    output_filepath: path to the file where the generated wav file should be 
    stored.
    """

    x = np.fromfile(input_filepath, dtype=np.complex64)

    # Demodulation
    x = np.diff(np.unwrap(np.angle(x)))

    # De-emphasis filter, H(s) = 1/(RC*s + 1), implemented as IIR via bilinear transform
    bz, az = bilinear(1, [75e-6, 1], fs=sample_rate)
    x = lfilter(bz, az, x)

    # decimate by 6 to get mono audio
    x = x[::6]
    sample_rate_audio = sample_rate/6

    # normalize volume so its between -1 and +1
    x /= np.max(np.abs(x))

    # some machines want int16s
    x *= 32767
    x = x.astype(np.int16)

    # Save to wav file, you can open this in Audacity for example
    wavfile.write('fm.wav', int(sample_rate_audio), x)


    
