import math
import random

class knapsack:

itemInfo = [[1,5],[2,9],[3,15],[4,10],[5,20],[6,30],[7,40],[8,35],[9,50],[10,60]] #[weight(kg), price($)] of each item

#returns a genome and it's fitnes score (total value of knapsack)
def generate_genome():
    size = 10 #size of possible elements stored in knapsack
    weightLimit = 60 #weightLimit of the knapsack (kg)
    genome = random.choices([0,1], weights = [1,1]. k = size)
    fitness = 0 #fitness score will be sum of value of included items
    weight = 0 #weight is the sum of the weight of included items

    for index in range(len(genome)):
        fitness += genome[index]*itemInfo[index][0]
        weight += genome[index]*itemInfo[index][1]
    if weight>weightLimit:
        fitness = 0

    return [genome,fitness]


#genetic alg
def genetic_alg ():
    population = []
    size = 10 #population size

    for i in range(size): #generate population of desired size
        population.append(generate_genome()[0]):




gentic_alg()
