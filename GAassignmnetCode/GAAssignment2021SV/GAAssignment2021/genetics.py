#
# GA Assignment 2021
#
import math
import time
import random
import pdb
from copy import copy
from Items import Item, ItemList
import g
from dataclasses import dataclass
import random
import sys
import time
from operator import attrgetter
from functools import total_ordering


def rnd (rng, lo, hi):  
    #if rng is a random the it returns a float between lo and hi , but never equalling Hi
    retv = (hi - lo) * rng.random() + lo;
    return retv

def rndInt (rng, lo, hi):
    # if rng is a random it returns a int between lo and hi, this is inclusive of lo and Hi val
    retv = (hi - lo+0.99) * rng.random() + lo;
    return int(retv)

@dataclass
class Gene(object):
    truck: int
    item: Item 


@total_ordering
class Genome(object):
    # some genome data deletd here .. students to design
    
    def __init__(self,rng, genes=[]):
        #note it populates the new genome with random numbers
        self.score=0       # score of this genome 
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

    @classmethod                
    def random_genes(cls, rng):
        def pick_truck():
            pick = random.randint(1, 100)
            if pick <= 70:
                return(0)
            elif pick <=80:
                return(1)
            elif pick <=90:
                return(2)
            elif pick <= 100:
                return(3)

        new_list = ItemList()
        new_list.setItems()
        new_list = copy(new_list.lst)
        new_genes = [Gene(pick_truck(), i) for i in new_list] 
        return(cls(rng, new_genes))


    


    def getTruck(self, truck):
        truck_genes = list(filter(lambda x: x.truck==truck, self.genes))
        return(truck_genes)


    def calcScore(self, itemList): #ItemList lst
        # student code here   
        importance_scores = {3:1, 2:2, 1:3} 
        importance = 0
        size1 = 0
        size2 = 0
        size3 = 0
        truck1 = self.getTruck(1)
        truck2 = self.getTruck(2)
        truck3 = self.getTruck(3)
        for gene in truck1:
            importance += importance_scores[gene.item.importance]
            size1 += gene.item.size
        
        diff_from_ideal1 = 19 - size1
        if diff_from_ideal1 < 0:
            diff_from_ideal1 -= 100

        for gene in truck2:
            importance += importance_scores[gene.item.importance]
            size2 += gene.item.size
        diff_from_ideal2 = 19 - size2
        if diff_from_ideal2 < 0:
            diff_from_ideal2 -= 100

        for gene in truck3:
            importance += importance_scores[gene.item.importance]
            size3 += gene.item.size
        diff_from_ideal3 = 19 - size3
        if diff_from_ideal2 < 0:
            diff_from_ideal2 -= 100




        total_diff = abs(diff_from_ideal1) + abs(diff_from_ideal2) + abs(diff_from_ideal3)
        score = total_diff
        self.score = score
        return(self.score)

            



       
class Population:
        
    # pop=[]    # the genomes of the population

    def __init__(self,rng, item_list):
        self.pop = [Genome(rng)]* g.POPULATION
        self.rng = rng
        self.item_list = item_list
        self.pop = list(map(lambda x:x.random_genes(item_list), self.pop))

    def idOfBest(self): # highest score
        #global POPULATION
        #retv = 0;
        #best = pop[0].score;
        #for i in range(1, g.POPULATION):
        #    if (pop[i].score > best):
        #        retv = i;
        #        best = pop[i].score;
        #return retv;
        pass
        

    def calcScore(self, itemList):
        best_score = 0 
        best_id = 0

        for count, genome in enumerate(self.pop):
            genome.calcScore(itemList)

        best = min(self.pop)
        best_id = min(range(len(self.pop)), key=self.pop.__getitem__)

        g.bestScore = best_score
        g.best = best_id
        print(f"best id:{best_id}, best_score:{best_score}")
        return(best_id)



         # update score for the entire population
         # update        g.best
         # update        g.bestScore 
    def crossover(self, genome1, genome2): 
        baby = Genome(self.rng) 
        baby.genes = [0] * 30
        for i in range(30):
            coin = rndInt(self.rng, 0, 1)
            if coin == 0:
                baby.genes[i] = genome1.genes[i]
            elif coin == 1:
                baby.genes[i] = genome2.genes[i]
            does_mutation_happen = rndInt(self.rng, 1, 100) 
            if does_mutation_happen <= g.MUTATIONPERCENT:
                baby.genes[i].truck = rndInt(self.rng, 0, 3)
                baby.mutations += 1
                g.mutations += 1
            # TO DO: change generation and mutations
        baby.generation += 1
        return(baby)


    
    def breed(self):
        # Kill some breed from the rest 
        self.calcScore(self.item_list)
        scores = sorted(self.pop, key=lambda genome: genome.score)

        winners = []
        for i in range(20):
            tournament = random.choices(scores, k=20)
            winner = min(tournament, key=attrgetter('score'))
            winners.append(winner)
      
        parents1 = winners[:10]
        parents2 = winners[10:]

        new_pop = []

        for i in range(10):
            random.shuffle(parents1)
            random.shuffle(parents2)
            for i in range(10):
                baby = self.crossover(parents1[i], parents2[i])
                new_pop.append(baby)
        self.pop = new_pop 
        self.calcScore(self.item_list)
        pdb.set_trace()


if __name__ == "__main__":
    rng = random.Random()
    item_list = ItemList()
    item_list.setItems()
    test  = Population(rng, item_list)
    pdb.set_trace()
    test.calcScore(rng)
    test.breed()