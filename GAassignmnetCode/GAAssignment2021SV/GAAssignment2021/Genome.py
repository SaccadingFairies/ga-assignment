#
# GA Assignment 2021
#
import math
import time
import random

import Items
import g

def rnd (rng, lo, hi):  
    #if rng is a random the it returns a float between lo and hi , but never equalling Hi
    retv = (hi - lo) * rng.random() + lo;
    return retv

def rndInt (rng, lo, hi):
    # if rng is a random it returns a int between lo and hi, this is inclusive of lo and Hi val
    retv = (hi - lo+0.99) * rng.random() + lo;
    return int(retv)

class Genome(object):
    # some genome data deletd here .. students to design
    score=0       # score of this genome 
    # generation=0  # counter to know which generation this came from
    # mutations=0   # counter to know how many mutations were in this genome

    def __init__(self,rng):
        #note it populates the new genome with random numbers
        pass


        
    def calcScore(self, itemList): #ItemList lst
        # student code here    
        return self.score;
        
       
class Population:
        
    # pop=[]    # the genomes of the population

    def __init__(self,rng):
        #self.pop = [None]*g.POPULATION
        #for i in range(0,g.POPULATION):
        #    self.pop[i]= Genome(rng)
        pass

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
         # update score for the entire population
         # update        g.best
         # update        g.bestScore 
         pass
        

    
    def breed(self, rng):
        # Kill some breed from the rest 
        return 


