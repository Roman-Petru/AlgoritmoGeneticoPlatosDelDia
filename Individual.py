from Recipes import recipes, prices, total_ingredients


def get_best_individual(population):
    # Initialize the best individual to the first individual in the population
    best_individual = population[0]

    # Iterate through the population to find the individual with the highest fitness
    for individual in population:
        if individual.fitness() > best_individual.fitness():
            best_individual = individual

    return best_individual


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    def fitness(self):
        number_of_each_recipe = self.number_of_dishes()

        total_profit = 0
        used_ingredients = {
            'arroz': 0,
            'pescado': 0,
            'pollo': 0,
            'papa': 0,
        }

        for i, quantity in enumerate(number_of_each_recipe):
            if i < len(recipes):
                recipe_name = list(recipes.keys())[i]
                price = prices[recipe_name]
                total_profit += price * quantity

                recipe_ingredients = recipes[recipe_name]
                for ingredient, recipe_quantity in recipe_ingredients.items():
                    if ingredient in used_ingredients:
                        used_ingredients[ingredient] += int(recipe_quantity) * quantity

        if all(used_ingredients[ingredient] <= total_ingredients.get(ingredient, 0) for ingredient in
               used_ingredients):  # Restriction function
            total_profit = 0

        return total_profit

    def print(self):
        print("Fitness value: ", self.fitness())

    def number_of_dishes(self):
        genes = [self.chromosome[i:i + 3] for i in range(0, len(self.chromosome), 3)]
        return [binary_to_decimal(gene) for gene in genes]


def binary_to_decimal(gene):
    reversed_gene = gene[::-1]
    decimal_value = 0
    for i, bit in enumerate(reversed_gene):
        decimal_value += bit * (2 ** i)
    return decimal_value
