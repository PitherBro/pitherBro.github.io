#!/bin/python3

import os,sys,json, random, math
from pathlib import Path


root = Path(os.path.dirname( __file__ ))

'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''

#base off deser style ECO, option to buy land for diff biomes.

global landAvaialable_WorldWide
global landSellPrice_PerSqaureFoot
global landLocal_ChunkGoal


class product():
    def __init__(self, params=dict({
        "name":"water",
        "sellMulti": .15
        }) ) -> None:
        super().__init__()
        self.name = params["name"]
        self.quantity = params["sellMulti"]
        self.sellValue = 1
        self.landSpace = 100 #in sqfeet
        self. sellMulti = .15
        self.sellMutiMinRange = .85
        self.sellMutiMaxRange = .98
        
    def calcTotalValue(self,):
        return self.quantity*(self.sellMulti*self.sellValue)
    def randomizeSellMultiplier(self,):
        # math.sqrt(random(self.sellMutiMinRange,self.sellMutiMaxRange))
        self.sellMulti = ((random.random()+ self.sellMutiMinRange) -  self.sellMutiMaxRange)*100 #random.randint()
    def toJson(self,):
        contents = self.__dict__.copy()
        return json.dumps(contents, indent=2)

class factory():
    def __init__(self,p=product()) -> None:
        super().__init__()
        self.prodCost = p
    def genProduct(self,):
        p = product()
        self.p.name = "water"
        self.p.randomizeSellMultiplier()
        self.p.quantity =10
        self.p.calcTotalValue()
        p = product(json.loads(self.p.toJson()))
        
        return p
    pass
class farm(factory):
    def __init__(self) -> None:
        super().__init__()
    pass
class mine(factory):
    def __init__(self) -> None:
        super().__init__()

def adjustGameSettings():
    landAvaialable_WorldWide = 1_000_000_000_000
    landSellPrice_PerSqaureFoot = 12
    landLocal_ChunkGoal = 10_000
    pass
if __name__ == "__main__":

    adjustGameSettings()

    

    print(p.toJson())
    print(sys.argv)    
    print(sys.path)
    pass
