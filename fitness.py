import numpy as np
from bisect import bisect_left

def fitness_random(individual, input_grid, config):
    return np.random.random_sample()

def nn_pitch(individual, spectrum, config):
    pitch = individual[0]
    amplitude = individual[1]
    freq_idx = max(0, min(1024, (round( (pitch*1024) / (11025) ))))
    #return - abs(pitch - spectrum[freq_idx][0])*abs(amplitude - spectrum[freq_idx][1])*spectrum[freq_idx][1]
    return spectrum[freq_idx][1]


