from InitialPopulation import get_initial_population
from ConfigLoader import load_config
from Individual import get_best_individual
from Selection import get_population_after_selection
from CrossOver import get_population_after_crossover
from Mutation import get_population_after_mutation
import numpy

class Main:
    def run(self):
        #Run Genetic Algorithm
        print("Running Genetic Algorithm")
        config = load_config()
        solutions = []

        population = get_initial_population()
        best = get_best_individual(population)
        for gen_number in range(config['number_of_generations']):
            population = get_population_after_selection(population)
            population = get_population_after_crossover(population)
            population = get_population_after_mutation(population)
            inds = []
            for individual in population:
                inds.append(individual.fitness())
            print("All fitness of new population: ", inds)
            print("Average: ", numpy.average(inds))

            print("Best individual of generation ", str(gen_number + 1), " : ")
            gen_best = get_best_individual(population)
            solutions.append(gen_best.fitness())
            gen_best.print()
            print("Fitness function value: ", str(gen_best.fitness()))
            if gen_best.fitness() > best.fitness():
                best = gen_best
        return best.fitness


if __name__ == "__main__":
    program = Main()
    program.run()
