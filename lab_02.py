# Genetic algoritm : 


# solving knapsak problem using genetic algo : 




weights = [2, 3, 4, 5]
values = [3, 4, 5, 8]
capacity = 8
population_size = 6
generations = 5
mutation_rate = 0.1



# finding the fitness of the population 
import random 
def fitness(pop):
    total_weight = 0 
    total_val = 0 
    for p, w , v in zip(pop, weights, values): 
        if p: 
            total_weight+= w 
            total_val+= v
    
    if total_weight<=capacity :
        return total_val 
    return 0 


# now selection , crossover, mutation function respectively   : 


def selection(pop) : 
    # i will select them whose probale fitness is much higher 
    fit = [fitness(ind) for ind in pop]
    total_fitness = sum(fit) 


    if total_fitness == 0 : 
        return random.sample(pop,2) # here I can choose 2 random parent or individual 
    
    prob= [fit/total_fitness for fit in fit] 
    return random.choices(pop,weights=prob , k=2)



# now crossover :

def crossover(p1,p2):

    point = random.randint(1,len(p1)-1)
    c1 = p1[:point]+p2[point:]
    c2 = p1[:point]+p2[point:]
    return c1,c2 

def mutation(pop):
    for i in range(len(pop)): 
        if random.random()<mutation_rate : 
             pop[i]= 1-pop[i] 
    return pop



# creating population  :

population  = [[random.randint(0,1) for _ in range(len(weights))] for _ in range(population_size)]
# here population size is the test_case 


# main function that will choose the best generations 

for gen in range(generations ): #gen =0,1,2,3,4 
    # finding fitness and making it decending order : 
    population.sort(key=fitness, reverse=True) 
    best_ind = population[0]
    print(f"Genereation {gen+1} : Probable best option : {best_ind} | value : {fitness(best_ind)}")


    new_gen = [population[0], population[1]] 
    #getting best 2 generation by default so that i can get max all the time

    # now populating the new_gen like the population before 
    while len(new_gen)<population_size :

        # selecting two possible parent
        p1,p2 = selection(population)

        # now crossing over them :
        c1,c2= crossover(p1,p2) 

        new_gen.append(mutation(c1))
        if len(new_gen)<population_size : 
            new_gen.append(mutation(c2))
    population = new_gen



