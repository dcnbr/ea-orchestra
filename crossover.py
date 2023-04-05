import numpy as np

def whole_arithmetic_crossover(parent1, parent2, config=None):
    """whole arithmetic crossover for integer representations"""

    avg_freq = (parent1[0] + parent2[0]) / 2
    avg_amp = (parent1[1] + parent2[1]) / 2
    avg_phase = (parent1[2] + parent2[2]) / 2

    offspring1 = (avg_freq, avg_amp, avg_phase)
    offspring2 = (avg_freq, avg_amp, avg_phase)

    return offspring1, offspring2


def uniform_bounding_box(parent1, parent2, config):

    r = config.getfloat('box_ratio')

    avg_freq = (parent1[0] + parent2[0]) / 2
    avg_amp = (parent1[1] + parent2[1]) / 2
    avg_phase = (parent1[2] + parent2[2]) / 2

    dev_freq = abs(avg_freq - parent1[0])
    dev_amp = abs(avg_amp - parent1[1])
    dev_phase = abs(avg_phase - parent1[2])

    o1 = (np.random.uniform(avg_freq  - r*dev_freq,  avg_freq  + r*dev_freq),
          np.random.uniform(avg_amp   - r*dev_amp,   avg_amp   + r*dev_amp),
          np.random.uniform(avg_phase - r*dev_phase, avg_phase + r*dev_phase)
         )

    o2 = (np.random.uniform(avg_freq  - r*dev_freq,  avg_freq  + r*dev_freq),
          np.random.uniform(avg_amp   - r*dev_amp,   avg_amp   + r*dev_amp),
          np.random.uniform(avg_phase - r*dev_phase, avg_phase + r*dev_phase)
         )

    return o1, o2
