#
# GA Assignment 2021
#

import tkinter as tk
import math
import matplotlib.pyplot as plt
import time
import random

import Items
import genetics
import g
import pdb

text_box1=0
text_box2=0
text_box3=0
text_box4=0
text_boxR1=0
text_boxR2=0
text_boxR3=0
text_boxR4=0
text_boxS1=0
text_boxS2=0
text_boxS3=0
greeting5=0
greetingT1=0
greetingT2=0
greetingT3=0
delayBox=0
#Checkbutton1=tk.IntVar()   

t0 = "";
t1 = "";
t2 = "";
t3 = "";
s0 = 0;
s1 = 0;
s2 = 0;
s3 = 0;


#critical items below
p=0      # the entire population
items=0  # an staic itemlist


# GUI Below
#dir = "D:\\BB\\University2021\\SC2021H\\TKTest\\Images\\" ### change this students !
window=0
windowX=800
windowY=600


def initialise():
    global globalRand, text_boxR1, text_boxR2, text_boxR3, text_boxR4
    global p, items 
    global t0, t1, t2, t3, s0, s1, s2, s3

    # random.seed(int(text_boxR1.get("1.0", tk.END)))
    g.POPULATION = int(text_boxR2.get("1.0", tk.END))
    g.MUTATIONPERCENT = float(text_boxR4.get("1.0", tk.END))
    g.maxGeneration = int(text_boxR3.get("1.0", tk.END));  
    
    g.generation = 0
    g.mutations= 0
    

    items = Items.ItemList()
    items.setItems()
    p = genetics.Population(items)
    g.best = p.calcScore()
    showStats()
    showBest()

def showStats():
    global text_boxS1
    textA = "Generation = " + str(g.generation)
    textB = "Mutations  = " + str(g.mutations)
    text_boxS1.delete('1.0',tk.END)       # Delete from position 0 till end 
    text_boxS1.insert(tk.END, textA+"\n"+textB) 

def run1Generation(p):
    global globalRand
    p.breed()
    g.best = p.calcScore();
    g.generation = g.generation +1
   

def runAll():
    global p, delayBox, window, Checkbutton1
    while (g.generation < g.maxGeneration):
        run1Generation(p);
        showStats();
        showBest();
        window.update_idletasks()
        delaySecs=float(delayBox.get("1.0", tk.END))
        if (delaySecs >= 0.01): time.sleep(delaySecs)
        # time.sleep(0.9)

def run1Gen():
    global p
    run1Generation(p);
    showStats();
    showBest();

def debug():
    print("debug here") # students feel free to add or change this


    
    

def showBest():
    global p, NUM_OF_ITEMS, text_box1, text_box2, text_box3, greetingT1, greetingT2, greetingT3
    global t0, t1, t2, t3, s0, s1, s2, s3
    t0 = "";
    t1 = "";
    t2 = "";
    t3 = "";
    s0 = 0;
    s1 = 0;
    s2 = 0;
    s3 = 0;
    best = p.pop[g.best]

    #// students put your code in here ******************************     
    #//                                call addToTruck to update the display 
    truck0 = best.getTruck(0)
    truck1 = best.getTruck(1)
    truck2 = best.getTruck(2)
    truck3 = best.getTruck(3)

    t0 = ""
    for gene in truck0:
        item = gene.item
        t0 += f"{item.name} ({item.size},{item.importance})\n"


    t1 = ""
    size1 = 0
    for gene in truck1:
        item = gene.item
        size1 += item.size 
        t1 += f"{item.name} ({item.size},{item.importance})\n"
    t1 += f"Sum = {size1}"

    t2 = ""
    size2 = 0
    for gene in truck2:
        item = gene.item
        size2 += item.size
        t2 += f"{item.name} ({item.size},{item.importance})\n"
    t2 += f"Sum = {size2}"

    t3 = ""
    size3 = 0
    for gene in truck3:
        item = gene.item
        size3 += item.size
        t3 += f"{item.name} ({item.size},{item.importance})\n"
    t3 += f"Sum = {size3}"
    #TO DO: add sum to trucks
    txt="Score="  + str(g.bestScore) + " ("+str(g.best)+")"
    greeting5.configure(text = txt);

    #text_box1  t1;
    text_box1.delete('1.0',tk.END)       # Delete from position 0 till end 
    text_box1.insert(tk.END, t1) 

    text_box2.delete('1.0',tk.END)       
    text_box2.insert(tk.END, t2)     

    text_box3.delete('1.0',tk.END)       
    text_box3.insert(tk.END, t3) 

    text_box4.delete('1.0',tk.END)       
    text_box4.insert(tk.END, t0) 

    #textBox8.Text = t0;     

    ss1 = "Truck 1 (" + str(g.TRUCK_CAPACITY) + ")";
    ss2 = "Truck 2 (" + str(g.TRUCK_CAPACITY) + ")";
    ss3 = "Truck 3 (" + str(g.TRUCK_CAPACITY) + ")";
    
    greetingT1.configure(text = ss1)
    greetingT2.configure(text = ss2)
    greetingT3.configure(text = ss3)





def main():
    global window, text_boxR1, text_boxR2, text_boxR3, text_boxR4, text_boxS1, greeting5, text_boxS2, text_boxS3
    global text_box1, text_box2, text_box3, text_box4, greetingT1, greetingT2, greetingT3, delayBox, Checkbutton1

    window=tk.Tk()

    geom=str(windowX)+"x"+str(windowY)
    window.geometry(geom) # "800x600"
    window.title("GA 2021")

    TOP_CTRL=10
    tyy=25  

    # main control buttons  
    startGAb = tk.Button(window, text="Initialise", bg="cyan", fg="black", relief="raised", command=initialise)
    startGAb.place(x = 5, y = TOP_CTRL+tyy*0, width=100, height=20) 
    stopGAb = tk.Button(window, text="Run All", bg="cyan", fg="black", relief="raised", command=runAll)
    stopGAb.place(x = 5, y = TOP_CTRL+tyy*1, width=100, height=20) 
    pauseGAb = tk.Button(window, text="Run 1 gen", bg="cyan", fg="black", relief="raised", command=run1Gen)
    pauseGAb.place(x = 5, y = TOP_CTRL+tyy*2, width=100, height=20) 
    continueGAb = tk.Button(window, text="Debug", bg="cyan", fg="black", relief="raised", command=debug)
    continueGAb.place(x = 5, y = TOP_CTRL+tyy*3, width=100, height=20) 

    #contents of trucks
    text_box1 = tk.Text(window, height=14, width=30)
    text_box1.place(x=5, y=350)    
    text_box2 = tk.Text(window, height=14, width=30)
    text_box2.place(x=260, y=350)    
    text_box3 = tk.Text(window, height=14, width=30)
    text_box3.place(x=260*2, y=350)

    # leftovers 
    text_box4 = tk.Text(window, height=18, width=30)
    text_box4.place(x=260*2, y=5)

    #Contents of trucks
    greetingT1 = tk.Label(window, text="Truck 1", bg="cyan", fg="black")
    greetingT1.place(x = 5, y = 350-25 , width=90, height=20)     
    greetingT2 = tk.Label(window, text="Truck 2", bg="cyan", fg="black")
    greetingT2.place(x = 260, y = 350-25 , width=90, height=20)
    greetingT3 = tk.Label(window, text="Truck 3", bg="cyan", fg="black")
    greetingT3.place(x = 260*2, y = 350-25 , width=90, height=20) 

    baseY2=200
    # labels for Random seed, population, generations, Mutation percent
    greeting1 = tk.Label(window, text="Random Seed", bg="cyan", fg="black")
    greeting1.place(x = 5, y = baseY2 , width=100, height=20) 
    greeting2 = tk.Label(window, text="Population", bg="cyan", fg="black")
    greeting2.place(x = 5, y = baseY2+1*25 , width=100, height=20) 
    greeting3 = tk.Label(window, text="Generations", bg="cyan", fg="black")
    greeting3.place(x = 5, y = baseY2+2*25 , width=100, height=20) 
    greeting4 = tk.Label(window, text="Mutation Percent", bg="cyan", fg="black")
    greeting4.place(x = 5, y = baseY2+3*25 , width=100, height=20) 

    # Input boxes for Random seed, population, generations, Mutation percent
    text_boxR1 = tk.Text(window, height=1, width=10) #Random Seed
    text_boxR1.place(x=110, y=baseY2)
    text_boxR1.insert(tk.END, "101") #tk.END
    text_boxR2 = tk.Text(window, height=1, width=10) #Population
    text_boxR2.place(x=110, y=baseY2+1*25) 
    text_boxR2.insert(tk.END, str(g.POPULATION)) 
    text_boxR3 = tk.Text(window, height=1, width=10) #Generations
    text_boxR3.place(x=110, y=baseY2+2*25) 
    text_boxR3.insert(tk.END, str(g.maxGeneration)) 
    text_boxR4 = tk.Text(window, height=1, width=10) #Mutation Percent
    text_boxR4.place(x=110, y=baseY2+3*25) 
    text_boxR4.insert(tk.END, str(g.MUTATIONPERCENT)) 

    # generation and mutation count 
    text_boxS1 = tk.Text(window, height=2, width=20) #stats
    text_boxS1.place(x=210, y=baseY2)
    text_boxS1.insert(tk.END, "..\n..")

    # Best Score and individual number
    greeting5 = tk.Label(window, text="...", bg="cyan", fg="black")
    greeting5.place(x = 210, y = baseY2+2*25 , width=140, height=20)

    # Ms delay
    greeting4 = tk.Label(window, text="Delay in seconds", bg="cyan", fg="black")
    greeting4.place(x = 210, y = baseY2+3*25 , width=100, height=20) 
  

    delayBox = tk.Text(window, height=1, width=10)
    delayBox.place(x = 315, y = baseY2+3*25 , width=90, height=20)
    delayBox.insert(tk.END,"0.01")

    #text_box.delete('1.0',tk.END)       # Delete from position 0 till end 

    window.mainloop()

if __name__ == "__main__":
    main()


