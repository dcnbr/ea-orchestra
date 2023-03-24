import configparser
import sys
import os
from inspect import getmembers, isfunction
import numpy as np
import scipy
import librosa
from bisect import bisect_left
import soundfile as sf
import cmath


import fitness
import mutation
import crossover
import parents
import survivors

strat_classes = ['fitness', 'mutation', 'crossover', 'parents', 'survivors']
np.set_printoptions(precision=3,edgeitems=2, linewidth=180)

def main():
    # open config file
    try:
        config_path = sys.argv[1]
        config = configparser.ConfigParser()
        config.read(config_path)
        assert os.path.isfile(config_path)
    except IndexError:
        print("Missing path to config file.")
        return 1
    except AssertionError:
        print("Config file could not be read.")
        return 1

    # convert [(key, value)] tuples list to {key:value} dictionary
    def rel2dict(rel, di):
        for a,b in rel:
            di.setdefault(a, b)
        return di

    # aggregate all the strategies that have been implemented
    strategies_all = {}
    for cls in strat_classes:
        strategies_all.setdefault(cls,rel2dict(getmembers(eval(cls), isfunction),{}))

    # load the input audio file
    audio, sr = librosa.load(config['filepaths']['input_audio'])

    # fourier transform input audio into frequency space
    # result is 2D matrix where index element [f][t] is
    # the complex-valued signal of frequency bin 'f' at time frame 't'
    in_audio_stft = librosa.stft(audio, n_fft=2048)

    # seperate complex value into (amplitude, phase)
    in_audio_amp = np.abs(in_audio_stft)
    in_audio_phase = np.angle(in_audio_stft)

    # get the frequencies bins in Hertz
    in_audio_freqs = np.multiply(np.ones(in_audio_stft.shape),
                                 librosa.fft_frequencies()[:, None])

    # gather into (frequency, amplitude, phase) 3-tuples
    in_audio_tensor = np.stack((in_audio_freqs, in_audio_amp, in_audio_phase),
                                axis=-1)
    in_audio_tuples = in_audio_tensor.view([('frq', in_audio_tensor.dtype),
                                            ('amp', in_audio_tensor.dtype),
                                            ('phs', in_audio_tensor.dtype)])
    in_audio_tuples = in_audio_tuples.reshape(in_audio_tuples.shape[:-1])


    # do evolutionary algorithm
    # TODO: placeholder, just copy over the input signal
    out_audio_tuples = in_audio_tuples


    # round/lerp population back into frequency bins
    libfreqs = librosa.fft_frequencies()
    out_audio_stft = np.zeros(in_audio_stft.shape, np.complex128)
    for x in range(0,out_audio_tuples.shape[0]):
        for y in range(0,out_audio_tuples.shape[1]):
            # round individuals to their nearest bin
            freq, ix = take_closest(libfreqs, out_audio_tuples[x][y][0])

            # convert back to complex-valued signal
            polar_coord = out_audio_tuples[x][y][1]
            polar_coord *= np.exp(1j*out_audio_tuples[x][y][2])

            # accumulate individuals
            out_audio_stft[ix][y] += polar_coord

    # invert the population from frequency space back into an audio signal
    out_audio = librosa.istft(out_audio_stft)

    # save audio
    sf.write(config['filepaths']['output_audio'], out_audio, sr)


def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0], pos;
    if pos == len(myList):
        return myList[-1], pos;
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after, pos;
    else:
        return before, pos;

if __name__ == "__main__":
    main()


