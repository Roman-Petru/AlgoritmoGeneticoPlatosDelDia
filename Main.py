from Population import get_initial_population

class Main:
    def run(self):
        #Run Genetic Algorithm
        print("Running Genetic Algorithm")
        solutions = []
        population = get_initial_population()
        best = get_best_individual(population)
        for gen_number in range(CONFIG.NUMBER_OF_GENERATIONS):
            population = get_population_after_selection(population)
            population = get_population_after_crossover(population)
            population = get_population_after_mutation(population)
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
