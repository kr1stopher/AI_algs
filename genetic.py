import math
import random

itemInfo = [[1,5],[2,9],[3,15],[4,10],[5,20],[6,30],[7,40],[8,35],[9,50],[10,60]] #[weight(kg), price($)] of each item

#calculates the fitness of a given genome
def calcFitness (genome):
    weightLimit = 40 #weightLimit of the knapsack (kg)
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
    genome = random.choices([0,1], weights = [1,1], k = genome_size) #generate a genome (1->item included, 0->item not included)

    return [genome,calcFitness(genome)]

def mutate_genome(genome):
    for gene in genome:
        if (random.randint(0,100) <= 15): #5% chance of mutation
            gene =  abs(gene-1) #change 1<->0
            print("There was a mutation")

    return genome



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


    generation = 0
    #run the algorithm for 100 generations
    while (generation<100): #can modify later to while(i<100 and fitness<goalFitness) to stop once a certain fitness level is reached
        genome_weights = [] #the weights of each genome for selection will be their fitness score
        parents = [] #list for the parents of the next generation

        for genomes in population: #add weights to genome_weights
            genome_weights.append(genomes[1]^3)

        #select 2 pairs of parents parents
        print(genome_weights)
        for i in range(4):
            newParent = (random.choices(population, weights = genome_weights)) #add selected to parents list
            parents.append(newParent[0])
            genome_weights.pop(population.index(parents[-1])) #remove recently added parent from genome_weights
            population.remove(parents[-1]) #remove recently added parent so that it is not selected again

        population = parents #drop all the "unfit" genomes from the poopulation

        #2 pairs of parents have 4 children each, and the parents are included in the next genome (4 parents + 8 kids = 12 nex generation)
            #parents [0,1] and [2,3] breeding partners
        for index in range (2): #two sets of parents
            for i in range (2): #two sets of 2 kids each
                random.seed()
                divider = random.randint(0,9)
                print("the divider is")
                print(divider)
                kid1 = parents[index][0][0:divider] + parents[index+1][0][divider::] #kid1 will conntain 0->divider genes parent 1, divider->end genes  parent2
                kid2 = parents[index+1][0][divider::] + parents[index][0][divider::]#kid2 will conntain 0->divider genes parent 2, divider->end genes  parent1
                #random mutations
                kid1 = mutate_genome(kid1)
                kid2 = mutate_genome(kid2)
                population.append([kid1,calcFitness(kid1)]) #add new children to population
                population.append([kid1,calcFitness(kid1)])


        #mutate random mutations
        willMutate = random.randint(0,100) <= 5  #5% chance of mutation

        #calculate new fitness score
            #if fitness = 0 replace with new genome

        generation+=1
        print("the population is")
        for genome in population:
            print(genome)
        print("the generation is ")
        print(generation)

    best = []
    for genomes in population:
        if len(best) == 0:
            best.append(genomes)
        elif best[0][1] < genomes[1]:
            best[0] = genomes
    return best





alg_tests = []
for i in range(20):
    alg_tests.append(genetic_alg())

best = []
average = 0
print(alg_tests[0])
for genomes in alg_tests:
    average += genomes[0][1]
    print(best)
    if len(best) == 0:
        best.append(genomes[0])
    elif best[0][1] < genomes[0][1]:
        best = genomes
average /=  len(alg_tests)

print("The best case found was ")
print(best)
print("The average result was ")
print(average)
