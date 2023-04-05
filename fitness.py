import numpy as np
from bisect import bisect_left

def fitness_random(individual, input_grid, config):
    return np.random.random_sample()

def nn_pitch(individual, spectrum, config):
    pitch = individual[0]
    amplitude = individual[1]
    freq_idx = round( (pitch*1024) / (11025) )
    return 1 - abs(pitch - spectrum[freq_idx][0])*abs(amplitude - spectrum[freq_idx][1])

