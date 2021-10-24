import math
import random

itemInfo = [[1,5],[2,9],[3,15],[4,10],[5,20],[6,30],[7,40],[8,35],[9,50],[10,60]] #[weight(kg), price($)] of each item

#calculates the fitness of a given genome
def calcFitness (genome):
    fitness = 0
    weight = 0
    for index in range(len(genome)):
        fitness += genome[index]*itemInfo[index][1]
        weight += genome[index]*itemInfo[index][0]
    if weight>weightLimit: #if total weight exceeds weight limit, fitness score is 0
        fitness = 0

    return fitness


#returns a genome and it's fitnes score (total value of knapsack)
def generate_genome():
    genome_size = 10 #size of possible elements stored in knapsack
    weightLimit = 40 #weightLimit of the knapsack (kg)
    genome = random.choices([0,1], weights = [1,1], k = genome_size)
    fitness = 0 #fitness score will be sum of value of included items
    weight = 0 #weight is the sum of the weight of included items

    return [genome,calcFitness(genome)]


#genetic alg
def genetic_alg ():
    population = [] # population = [[xi,f(xi)]....[xn,f(xn)]] where xi is genome i and f(xi) is the fitness of that genome
    population_size = 12 #population size

    #generate population of desired size
    for i in range(population_size):
        population.append(generate_genome())
        while (population[-1][1] == 0): #if the fitness score is 0 (knapsack over weight limit, replace with new genome)
            population[-1] = generate_genome()
        print(population[-1])


    i = 0
    #run the algorithm for 100 generations
    while (i<100): #can modify later to while(i<100 and fitness<goalFitness) to stop once a certain fitness level is reached
        genome_weightst = [] #the weights of each genome for selection will be their fitness score
        parents = [] #list for the parents of the next generation

        for genomes in population:
            genome_weightst.append(items[1])

        #select 2 pairs of parents parents
        for i in range(4):
            parents.append(random.choices(population, weights = genome_weights)) #add selected to parents list
            population.remove(parents[-1]) #remove recently added parent so that it is not selected again

        population = parents #drop all the "unfit" genomes from the poopulation
        #2 pairs of parents have 4 children each, and the parents are included in the next genome (4 parents + 8 kids = 12 nex generation)
            #parents [0,1] and [2,3] breeding partners

            for index in range (2): #two sets of parents
                for i in range (2): #two sets of 2 kids each
                    random.seed()
                    divider = random.randint(0,9)
                    kid1 = parents[index][0][0:divider] + parents[index+1][0][divider::] #kid1 will conntain 0->divider genes parent 1, divider->end genes  parent2
                    kid2 = parents[index+1][0][divider::] + parents[index][0][divider::]#kid2 will conntain 0->divider genes parent 2, divider->end genes  parent1
                    population.append([kid1,calcFitness(kid1)]) #add new children to population
                    population.append([kid1,calcFitness(kid1)])





        #mutate random mutations


        #calculate new fitness score
            #if fitness = 0 replace with new genome

        i += 1





genetic_alg()
