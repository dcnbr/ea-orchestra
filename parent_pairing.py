import random

def random_pair(parents_index, current_population, config):
    random.shuffle(parents_index)
    return parents_index

def sim_freq_pair(parents_index, current_population, config):
    parents_bodies = [(x, current_population[x]) for x in parents_index]
    parents_bodies.sort(key=lambda tup: tup[1][0])  # sort parents by frequency
    parents_index = [x for x, y in parents_bodies]

    return parents_index
