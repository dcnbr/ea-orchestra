def crossover_1():
    return 0


def whole_arithmetic_crossover(parent1, parent2):
    """whole arithmetic crossover for integer representations"""

    avg_freq = (parent1[0] + parent2[0]) / 2
    avg_amp = (parent1[1] + parent2[1]) / 2
    avg_phase = (parent1[2] + parent2[2]) / 2

    offspring1 = (avg_freq, avg_amp, avg_phase)
    offspring2 = (avg_freq, avg_amp, avg_phase)

    return offspring1, offspring2
