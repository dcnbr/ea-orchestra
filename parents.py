import random


def tournament(fitness, hyperparams):
    """Tournament selection without replacement"""

    mating_pool_size = int(hyperparams["mating_pool_size"])
    tournament_size = int(hyperparams["tournament_size"])
    selected_to_mate = []

    while len(selected_to_mate) < mating_pool_size:
        contestants = random.sample(fitness, tournament_size)
        winner = max(contestants)
        # Add the parent whose fitness was the winning fitness to the mating pool
        selected_to_mate.append(fitness.index(winner))

    return selected_to_mate


def MPS(fitness, hyperparams):
    """Multi-pointer selection (MPS)"""

    mating_pool_size = int(hyperparams["mating_pool_size"])
    selected_to_mate = []

    # Build the probability distribution (number line), where a value at a certain index is sum of the indivdual at that index's fitness plus all the ones before it
    prob_dist = []
    for index, value in enumerate(fitness):
        if index == 0:
            prob_dist.append(value)
        else:
            prob_dist.append(value + prob_dist[index - 1])

    arm_distance = sum(fitness) / mating_pool_size
    # Randomly choose position of pointer 1
    pointer_pos = random.uniform(0, arm_distance)

    # Add each individual that is being pointed to the parents pool until enough are selected
    individual_index = 0
    while len(selected_to_mate) < mating_pool_size:
        while pointer_pos <= prob_dist[individual_index]:
            selected_to_mate.append(individual_index)
            pointer_pos += arm_distance
        individual_index += 1

    return selected_to_mate


def random_uniform(fitness, hyperparams):
    """Random uniform selection"""
    population_size = int(hyperparams["population_size"])
    mating_pool_size = int(hyperparams["mating_pool_size"])
    selected_to_mate = []

    # student code starts
    possible_parents = list(range(population_size))
    selected_to_mate = random.sample(possible_parents, mating_pool_size)
    # student code ends

    return selected_to_mate


