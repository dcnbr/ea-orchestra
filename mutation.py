import random

allele_for = {
        "frequency": 0,
        "amplitude": 1,
        "phase"    : 2}


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
        individual[allele_for["frequency"]],
        individual[allele_for["amplitude"]] + amp_change,
        individual[allele_for["phase"]],
    )

    return mutant


def adjust_freq(individual, hyperparams):
    """Mutate frequency by a fixed amount, randomly up or down"""

    freq_change = int(hyperparams["freq_change"])
    freq_change = freq_change if random.randint(0, 1) else -freq_change

    mutant = (
        individual[allele_for["frequency"]] + freq_change,
        individual[allele_for["amplitude"]],
        individual[allele_for["phase"]],
    )

    return mutant


