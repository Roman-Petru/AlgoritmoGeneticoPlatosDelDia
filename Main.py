from InitialPopulation import get_initial_population
from ConfigLoader import load_config
from Individual import get_best_individual
from Selection import get_population_after_selection
from CrossOver import get_population_after_crossover
from Mutation import get_population_after_mutation
import matplotlib.pyplot as plt

class Main:
    def run(self):
        #Run Genetic Algorithm
        print("Running Genetic Algorithm")
        config = load_config()
        solutions = []
        x_axis = []
        x_marker = 0

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
            print("Best individual of generation ", str(gen_number + 1), " : ")

            gen_best = get_best_individual(population)
            solutions.append(gen_best.fitness())
            x_axis.append(x_marker)
            x_marker = x_marker + 1

            gen_best.print()
            print("Fitness function value: ", str(gen_best.fitness()))
            if gen_best.fitness() > best.fitness():
                best = gen_best

        print("Best of run Fitness value: ", best.fitness())
        print("Best of run Chromosome: ", best.number_of_dishes())

        plt.figure(figsize=(12, 9))
        plt.plot(x_axis, solutions)

        # Add labels and title
        plt.xlabel('Corridas')
        plt.ylabel('Ganancia total')

        title = ("Cantidad de generaciones: ", config['number_of_generations'], "Tasa de cruzamiento: ", config['crossover_rate'],
                 "Función de cruzamiento: ", config['crossover_type'], "Probabilidad de mutacion: ", config['mutation_probability'])
        plt.title(title)

        subtitle = 'Mejor funcion de la corrida: ', best.fitness(), ' - genes del mejor: ',  best.number_of_dishes()
        plt.suptitle(subtitle, fontsize=12, color='gray')

        plt.grid(True)
        plt.show()
        return


if __name__ == "__main__":
    program = Main()
    program.run()
