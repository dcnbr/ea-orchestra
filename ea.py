

import fitness
import mutation
import crossover
import parents
import survivors

import random
import numpy as np

def ea(input_grid, strat_for, config):
    fft_frames_count = input_grid.shape[0]

    # initialize population
    current_population = np.random.rand(input_grid.shape[1],3)
    current_population = current_population.view([('frq', current_population.dtype),
                                                  ('amp', current_population.dtype),
                                                  ('phs', current_population.dtype)])
    current_population = current_population.reshape(current_population.shape[:-1])
    current_population['frq'] = current_population['frq']*11025
    population_history = np.zeros(input_grid.shape, input_grid.dtype)
    population_history[0] = current_population

    # calculate population fitness
    current_fitness = [strat_for['fitness'](x, input_grid[0], config['fitness']) for x in current_population]


    meta_index = 0
    per_frame_counter = 0
    converged = False
    while not converged:
        print("working frame " + str(meta_index) + " / " + str(fft_frames_count), end='\r')
        # === parent selection ===
        parents_index = strat_for['parents'](current_fitness, config['parents'])
        random.shuffle(parents_index)

        # === crossover ===
        # siblings = [ crossover(p1, p2) for parents (p1, p2)] sampled w/o replacement
        # pairs parents like (first, last), (second, second-last), etc
        # x > y ensures only one of (first, last) and (last, first) is used
        siblings = [strat_for['crossover'](current_population[x], current_population[y], config['crossover'])
                    for x,y in zip(parents_index, parents_index[::-1]) if x > y]
        # flatten [(c1, c2), ...] to [c1, c2 ...]
        zygotes = [z for pair in siblings for z in pair]

        # === mutation ===
        # lambda to selectively mutate according to coin flip
        mutate = lambda o, prob : (strat_for['mutation'](o, config['mutation'])
                                   if prob < config['mutation'].getfloat('mutation_rate')
                                   else o )
        mutation_attempt = np.random.rand(len(zygotes))
        # mutate children into offspring via lambda
        offspring = [mutate(o, prob) for o, prob in zip(zygotes, mutation_attempt)]
        # flip <mutation_rate> coin for each child

        # === fitness ===
        offspring_fitness = [strat_for['fitness'](x, input_grid[meta_index], config['fitness']) for x in offspring]

        # === survivor selevtion & replacement ===
        next_population, next_fitness = (
                strat_for['survivors'](current_population, current_fitness,
                                        offspring, offspring_fitness))


        # loop maintenence and convergence testing

        if per_frame_counter >= config['general'].getint('per_frame_iteration'):
            population_history[meta_index] = current_population

            meta_index += 1
            per_frame_counter = 0
            converged = True if meta_index >= fft_frames_count else False

            current_population = next_population
            current_fitness = next_fitness
        else:
            per_frame_counter += 1

    return population_history


