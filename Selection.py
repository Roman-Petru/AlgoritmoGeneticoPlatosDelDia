import random

def get_population_after_selection(population):
    total_fitness = sum(individual.fitness() for individual in population)

    selection_probabilities = [individual.fitness() / total_fitness for individual in population]

    new_population = []
    for _ in range(len(population)):
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