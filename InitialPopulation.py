import random
from ConfigLoader import load_config
from Individual import Individual

def get_initial_population():

    # Retrieve population_size and individual_size

    config = load_config()
    population_size = config['population_size']
    individual_size = config['individual_size']

    population = []
    for number_of_individual in range(population_size):
        # Generate a random binary string of the specified length
        chromosome = [random.randint(0, 1) for number_of_individual in range(individual_size)]

        # Create an Individual instance with the random chromosome
        individual = Individual(chromosome)
        print("Chromosome ", number_of_individual, " : ", chromosome)

        population.append(individual)
    return population