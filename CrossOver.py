import random
from Individual import Individual
from ConfigLoader import load_config


def get_population_after_crossover(population):
    config = load_config()

    if (config['crossover_type'] == "simple"):
        return get_simple_crossover(population, config)
    if (config['crossover_type'] == "random_binomial"):
        return get_random_binomial_crossover(population, config)
    else:
        return get_random_binomial_crossover(population, config)


def get_simple_crossover(population, config):
    new_population = []

    while len(new_population) < len(population):
        # Randomly select two parents for crossover
        parent1 = random.choice(population)
        parent2 = random.choice(population)

        # Check if crossover should occur based on the crossover rate
        if random.random() < config['crossover_rate']:
            # Perform a random one-point crossover
            crossover_point = random.randint(1, len(parent1.chromosome) - 1)
            child1_chromosome = parent1.chromosome[:crossover_point] + parent2.chromosome[crossover_point:]
            child2_chromosome = parent2.chromosome[:crossover_point] + parent1.chromosome[crossover_point:]
            child1 = Individual(child1_chromosome)
            child2 = Individual(child2_chromosome)
            new_population.extend([child1, child2])
        else:
            # If no crossover, just add parents to the new population
            new_population.extend([parent1, parent2])

    return new_population


def get_random_binomial_crossover(population, config):
    new_population = []

    while len(new_population) < len(population):
        parent1 = random.choice(population)
        parent2 = random.choice(population)

        # Initialize empty lists for child chromosomes
        child1_chromosome = []
        child2_chromosome = []

        # Perform random binomial crossover for each gene
        for gene1, gene2 in zip(parent1.chromosome, parent2.chromosome):
            if random.random() < config['crossover_rate']:
                child1_chromosome.append(gene1)
                child2_chromosome.append(gene2)
            else:
                child1_chromosome.append(gene2)
                child2_chromosome.append(gene1)

        # Create child individuals and add them to the new population
        child1 = Individual(child1_chromosome)
        child2 = Individual(child2_chromosome)
        new_population.extend([child1, child2])

    return new_population
