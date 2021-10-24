import math
import random

itemInfo = [[1,5],[2,9],[3,15],[4,10],[5,20],[6,30],[7,40],[8,35],[9,50],[10,60]] #[weight(kg), price($)] of each item

#returns a genome and it's fitnes score (total value of knapsack)
def generate_genome():
    genome_size = 10 #size of possible elements stored in knapsack
    weightLimit = 40 #weightLimit of the knapsack (kg)
    genome = random.choices([0,1], weights = [1,1], k = genome_size)
    fitness = 0 #fitness score will be sum of value of included items
    weight = 0 #weight is the sum of the weight of included items

    #calculate the fitness score (total item value) of each knapsack
    for index in range(len(genome)):
        fitness += genome[index]*itemInfo[index][1]
        weight += genome[index]*itemInfo[index][0]
    print(weight)
    if weight>weightLimit: #if total weight exceeds weight limit, fitness score is 0
        fitness = 0

    return [genome,fitness]


#genetic alg
def genetic_alg ():
    population = [] # population = [[xi,f(xi)]....[xn,f(xn)]] where xi is genome i and f(xi) is the fitness of that genome
    population_size = 10 #population size

    for i in range(population_size): #generate population of desired size
        population.append(generate_genome())
        print(population[-1])




genetic_alg()
