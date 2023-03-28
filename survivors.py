import random


def survivors_1():
    return 0


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""

    population = []
    fitness = []

    # Combine fitness and population lists for all inviduals so their indices are linked during processing
    possible_survivors = zip(
        current_fitness + offspring_fitness, current_pop + offspring
    )
    # Select the top ranked candidates out of all individuals based on fitness
    survivors = sorted(possible_survivors, reverse=True)[: len(current_pop)]

    # Separate the lists
    fitness, population = zip(*survivors)
    fitness = list(fitness)
    population = list(population)

    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # Combine fitness and individual lists for current generation so their indices are linked during processing
    curr_gen = zip(current_fitness, current_pop)
    # Select the top ranked candidates in the current generation based on fitness
    curr_gen_survivors = sorted(curr_gen, reverse=True)[
        : (len(current_pop) - len(offspring))
    ]
    # Separate the lists
    fitness, population = zip(*curr_gen_survivors)
    fitness = list(fitness)
    population = list(population)

    population += offspring
    fitness += offspring_fitness

    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # Combine fitness and population lists for all inviduals so their indices are linked during processing
    possible_survivors = zip(
        current_fitness + offspring_fitness, current_pop + offspring
    )

    survivors = random.sample(list(possible_survivors), len(current_pop))

    # Separate the lists
    fitness, population = zip(*survivors)
    fitness = list(fitness)
    population = list(population)

    return population, fitness
