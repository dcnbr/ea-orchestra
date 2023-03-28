import random


def mutation_1():
    return 0


def adjust_amp_freq(individual, hyperparams):
    """Mutate amplitude by a fixed amount, randomly up or down, and then frequency by a fixed amount, randomly up or down"""

    mutant = adjust_amp(individual, hyperparams)
    mutant = adjust_freq(mutant, hyperparams)

    return mutant


def adjust_amp(individual, hyperparams):
    """Mutate amplitude by a fixed amount, randomly up or down"""

    amp_change = int(hyperparams["amp_change"])
    amp_change = amp_change if random.randint(0, 1) else -amp_change

    mutant = (
        individual["frequency"],
        individual["amplitude"] + amp_change,
        individual["phase"],
    )

    return mutant


def adjust_freq(individual, hyperparams):
    """Mutate frequency by a fixed amount, randomly up or down"""

    freq_change = int(hyperparams["freq_change"])
    freq_change = freq_change if random.randint(0, 1) else -freq_change

    mutant = (
        individual["frequency"] + freq_change,
        individual["amplitude"],
        individual["phase"],
    )

    return mutant
