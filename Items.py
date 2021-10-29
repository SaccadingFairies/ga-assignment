#
# GA Assignment 2021
#
import math
import time
import random
import pdb
import pprint


class Item(object):
    name=""; #// max of say 10 chars 
    longName=""; #// any length if blank defaults to short name
    size=9999; #// 1 - 100 how it fits
    importance=3333; #//1=Urgent 2=Important 3=Low
    truck=0; #// which truck its in 0=no truck

    def __init__(self, nameQ, longNameQ, sizeQ, importanceQ):
        self.name = nameQ
        self.longName =longNameQ
        self.size =sizeQ
        self.importance =importanceQ
        self.truck = 0

    def __repr__(self):    
        return(f"name:{self.name}, size:{self.size}, importance:{self.importance}")
class ItemList(object):
    
    lst=[]; # the actual list of items 

    def __init__(self):
        self.lst= [None] * 30
    
    def setItems(self):
        self.lst[0]=Item("Bandages","",6,1);
        self.lst[1]=Item("BandagesXL","",6,1);
        self.lst[2]=Item("Bandage","Full Body 'mummy' Cast",3,1);
        self.lst[3]=Item("Oxygen","Oxygen Cylinders",12,1);
        self.lst[4]=Item("Hospital I","Tent Hospital part 1",12,1);
        self.lst[5]=Item("Hospital II","Tent Hospital part 2",17,1);
        self.lst[6]=Item("Generator","Electricity Generator",6,1);
        self.lst[7]=Item("Petrol44a","44 Gal Drum of Petrol",11,2);
        self.lst[8]=Item("Petrol44b","44 Gal Drum of Petrol",11,2);
        self.lst[9]=Item("Petrol20","20 L Gerrycan of fuel",2,2);
        self.lst[10]= Item("Condoms","",1,3);
        self.lst[11]= Item("Mercurochrome", "Disinfectant for wounds", 9, 1);
        self.lst[12]= Item("Chocolate","Large box donated by Cadbury",5,3);
        self.lst[13]= Item("Radio","Large multifreq radio+gen",11,1);
        self.lst[14] =  Item("HeliSpare","Helicopter Rotor", 8, 1);
        self.lst[15] =  Item("Box", "Grey box marked 'Top Secret'", 13, 1);
        self.lst[16] =  Item("Spuds", "Crate of Potates", 9, 2);
        self.lst[17] =  Item("Ping", "Machine That goes Ping", 12, 1);
        self.lst[18] =  Item("Difox201", "DF201 For mine resque", 10, 1);
        self.lst[19] =  Item("Trash", "Trash Disposal system", 11, 3);
        self.lst[20] =  Item("Batteries", "Mobile Phone batteries", 7, 2);
        self.lst[21] =  Item("GDP", "Government policy manual", 10, 2);
        self.lst[22] =  Item("Gillard", "For a good spin on the disaster", 8, 3);
        self.lst[23] =  Item("RB", "Rubber Bags and lime", 11, 1);
        self.lst[24] =  Item("SaltP", "Salt Pork", 4, 3);
        self.lst[25] =  Item("Water", "Water 100L", 13, 1);
        self.lst[26] =  Item("Peaches", "Tins Of Peaches", 10, 3);
        self.lst[27] =  Item("UGS", "UGS - Type 20", 11, 1);
        self.lst[28] =  Item("MS", "Coffin", 9, 2);
        self.lst[29] =  Item("Doctor", "Doctors Kit", 13, 1);

if __name__ == "__main__":
    x = ItemList()
    x.setItems()
    x.lst.sort(key=lambda y:y.size, reverse=True)
    for i in x.lst:
        print(i.size)
    pdb.set_trace()

