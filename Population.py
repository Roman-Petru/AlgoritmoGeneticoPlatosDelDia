import random
from ConfigLoader import load_config

def get_initial_population():
    """
    Generate the initial population of individuals.

    Parameters:
    - population_size: The number of individuals in the population.
    - individual_size: The size of each individual (length of the binary string).

    Returns:
    A list of individuals, where each individual is represented as a binary string.
    """

    # Retrieve population_size and individual_size

    config = load_config('config.json')
    population_size = config['population_size']
    individual_size = config['individual_size']

    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(individual_size)]
        population.append(individual)
    return population