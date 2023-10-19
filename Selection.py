import random

def get_population_after_selection(population):
    # Calculate the total fitness of the population
    total_fitness = sum(individual.fitness() for individual in population)

    # Create a list of selection probabilities for each individual
    selection_probabilities = [individual.fitness() / total_fitness for individual in population]

    # Use roulette wheel selection to create the new population
    new_population = []
    for _ in range(len(population)):
        # Select an individual using roulette wheel selection
        selected_index = roulette_wheel_selection(selection_probabilities)
        new_population.append(population[selected_index])

    return new_population

def roulette_wheel_selection(selection_probabilities):
    # Generate a random number between 0 and 1
    random_value = random.random()

    # Use the random number to select an individual
    cumulative_probability = 0
    for index, probability in enumerate(selection_probabilities):
        cumulative_probability += probability
        if random_value <= cumulative_probability:
            return index