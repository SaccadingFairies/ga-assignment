#
# GA Assignment 2021
#
import math
import time
import random
import pdb
from copy import copy, deepcopy
from typing import overload
from Items import Item, ItemList
import g
from dataclasses import dataclass
import random
import sys
import time
from operator import attrgetter
from functools import total_ordering
from pprint import pprint

@dataclass
class Gene(object):
    truck: int
    item: Item 



# @total_ordering
class Genome(object):
    # some genome data deletd here .. students to design
    
    def __init__(self, genes=[]):
        #note it populates the new genome with random numbers
        self.score=9999999      # score of this genome 
        self.generation=0  # counter to know which generation this came from
        self.mutations=0   # counter to know how many mutations were in this genome
        self.genes = genes

    def __repr__(self):
        return(f"score:{self.score}, generation:{self.generation}, mutations:{self.mutations}")
    
    def __lt__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.score < other.score

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.score == other.score
    
    def __le__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return (self.score == other.score) or (self.score < other.score)
    
    
    def __gt__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.score > other.score

    def __ge__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return (self.score == other.score) or (self.score > other.score)
   
    @classmethod              
    def random_genes(cls):
        def pick_truck():
            pick = random.randint(1, 100)
            if pick <= 70:
                return(0)
            else:
                return(random.randint(1, 3))

        new_list = ItemList()
        new_list.setItems()
        new_list = copy(new_list.lst)

        new_genes = [Gene(pick_truck(), i) for i in new_list] 
        new_genome = cls(new_genes)
        score = new_genome.calcScore()
        
            
        return(new_genome)

    def getTruck(self, truck):
        truck_genes = list(filter(lambda x: x.truck==truck, self.genes))
        return(truck_genes)

    def getTruckSizes(self):
        truck_sizes = []
        for i in range(1, 4):
            truck_size = 0
            truck = self.getTruck(i) 
            for gene in truck:
                truck_size += gene.item.size
            truck_sizes.append(truck_size)
        return(truck_sizes)
        pdb.set_trace()

    def calcScore(self): #ItemList lst
        # student code here   
        importance_weights = {1:3, 2:2, 3:1} 
        petrol_count = 0
        hospital_count = 0
       
        truck1 = self.getTruck(1)
        truck2 = self.getTruck(2)
        truck3 = self.getTruck(3)

        diffs_from_ideal = []
        importance_scores = []
        for i in range(1,4):
            truck = self.getTruck(i)
            importance = 0
            size = 0
            for gene in truck:
                name = gene.item.name
                importance += importance_weights[gene.item.importance]
                size += gene.item.size

                # give first petrol added a little boost
                if name[:6] == "Petrol":
                    petrol_count += 1
                    if petrol_count == 1:
                        importance += 5

                #only give points for hospital items if both are in a truck
                if name[:8] == "Hospital":
                    hospital_count += 1
                    if hospital_count == 1: 
                        importance -= 1
                        continue
                    elif hospital_count == 2:
                        importance += 8 

                

            importance_scores.append(importance)
            diff_from_ideal = 19 - size
            if diff_from_ideal < 0:
                diff_from_ideal -=  g.overloaded_penalty
            diffs_from_ideal.append(diff_from_ideal)


        score = sum([importance_scores[i] - abs(diffs_from_ideal[i]) for i in range(3)])
        self.score = score

            



       
class Population:
        
    # pop=[]    # the genomes of the population

    def __init__(self, item_list):
        self.pop = [Genome()]* g.POPULATION
        self.item_list = item_list
        self.pop = list(map(lambda x:x.random_genes(), self.pop))

    def calcScore(self):
     
        for genome in self.pop:
            genome.calcScore()

        best = max(self.pop)
        best_id = max(range(len(self.pop)), key=self.pop.__getitem__)

        g.bestScore = best.score
        g.best = best_id
        print(f"best id:{best_id}, best_score:{best.score}")
        return(best_id)



         # update score for the entire population
         # update        g.best
         # update        g.bestScore 
    def crossover(self, genome1, genome2): 
        baby = Genome() 
        baby.genes = [0] * 30
        for i in range(30):
            coin = random.randint(0, 1)
            if coin == 0:
                baby.genes[i] = deepcopy(genome1.genes[i])
            elif coin == 1:
                baby.genes[i] = deepcopy(genome2.genes[i])
        does_mutation_happen = random.randint(1, 100) 
        if does_mutation_happen <= g.MUTATIONPERCENT:
            baby.genes[random.randint(0,29)].truck = random.randint(0, 3)
            baby.mutations += 1
            g.mutations += 1
        baby.generation += 1
        baby.calcScore()
        return(baby)


    
    def breed(self):
        # Kill some breed from the rest 
        x = deepcopy(self.pop) 
        self.calcScore()

        scores = sorted(copy(self.pop), reverse=True)
        quarter = len(scores) // 4
        top_quarter = scores[:quarter] 
        
        new_pop = []

        for i in range(g.POPULATION):
            parents = random.sample(top_quarter, 2)
            baby = self.crossover(parents[0], parents[1])
            truck_sizes = baby.getTruckSizes()
            new_pop.append(baby)

        self.pop = new_pop
        self.pop[0] = scores[0] # Keeping best
        self.calcScore()
        print(f"max(x):{max(x)}")
        print(f"max(self.pop):{max(self.pop)}")
        g.generation += 1


if __name__ == "__main__":
    item_list = ItemList()
    item_list.setItems()
    test = Population(item_list)
    for i in range(200):
        test.breed()
        print(f"mutations:{g.mutations}")
        print(f"g.best_score {g.bestScore}")
        print(f"g.bestid {g.best}")
        test.pop[0].getTruckSizes()

    # test = [Genome(rng) for i in range(10)]
    # for i in test:
    #     test.random_genes()

    

    # for i in range(10):
    #     test.calcScore()
    #     print(f"test2.score:{test.score}")

   