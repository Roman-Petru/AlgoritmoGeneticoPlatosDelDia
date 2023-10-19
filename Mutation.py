import random
from ConfigLoader import load_config
from Individual import Individual

def get_population_after_mutation(population):

    new_population = []
    config = load_config()

    for individual in population:
        # Create a copy of the individual's chromosome for mutation
        mutated_chromosome = list(individual.chromosome)

        # Perform mutation for each gene
        for i in range(len(mutated_chromosome)):
            if random.random() < config['mutation_probability']:
                mutated_chromosome[i] = 1 - mutated_chromosome[i]

        # Create a new individual with the mutated chromosome and add it to the new population
        mutated_individual = Individual(mutated_chromosome)
        new_population.append(mutated_individual)

    return new_population
