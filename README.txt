Author: Kris
Language: Python


Repository contents: 
	gentic.py 
	
	
	
	
genetic.py 
	Purpose:
		Buidling Genetic Algorithms for AI problem solving of the knapsack problem 
	Main Features:
		def calcFitness (genome): calculates fitness of a given genome 
		def generate_genome: returns 1 randomly generated genome
		def mutate_genome (genome): randomly applies mutations to the  given genome
		def genetic_alg():
			(1) creates population of genomes 
			(2) selects the most fit and breeds them for next generation 
			(3)randomly mutates new generaation 
			(4) evaluates fitness 
			(5) proceeds for set # of generations 
			
	
			
	







ChangeLog:
	10/24
		Created genetic.py
		calcFitness, generate_genome, genetic_alg functions created 
		genetic_alg incomplete and untested 
	10/25
		functions complete and operating 
		increased population size decreased generations for better results 
		Average result case nearly 200 now
		215 appears to be the best result possible 
		
	
