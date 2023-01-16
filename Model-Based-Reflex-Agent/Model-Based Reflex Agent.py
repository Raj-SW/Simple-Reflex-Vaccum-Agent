#defining the room/environment

import random


class environment():
    def __init__(self):
      self.room=[
                [1,0,1],
                [0,2,1],
                [1,1,1],
            ]

#memory of the environment
class memory() : 
    def __init__(self) :
        self.pathMemory= [[0,0,0],
                         [0,0,0],
                        [0,0,0],]

class ModelBasedAgent(memory,environment):
    def __init__(self,environment):
        #path memory
        pathMemory= [[0,0,0],
                         [0,0,0],
                        [0,0,0],]
        PerfMeasure=0
        print("at first")
        print(environment.room)
        print(pathMemory)
        #Put the cleaner at a random location
        x=random.randint(0,len(environment.room)-1)
        y=random.randint(0,len(environment.room[0])-1)
        print("Vacuum cleaner put at",x,y)

        while(y<len(environment.room[0])):
            while(x<len(environment.room)):

                #clean spot and update memory
                    #if current spot dirty, then clean it and update in memory
                if environment.room[x][y]==1:
                    print("Location ",x,y,"is dirty. Proceeding to cleaning")
                    environment.room[x][y]=0
                    pathMemory[x][y]=1
                    PerfMeasure+=1

                #Checks for obstacles and where it can move
                elif environment.room[x][y]==2:
                    print("Location ",x,y,"has obstacle. Proceeding to move to next location")
                    pathMemory[x][y]=2
                    PerfMeasure+=1
                else:
                    PerfMeasure+=1
                    pathMemory[x][y]=1
                #add the route to its memory
                #clean the tile
                print(x,y)
                x=x+1
            y=y+1
            x=0
        print("first pass")
        print(environment.room)
        print(pathMemory)

        #check for any other missed spot by going backwards
        while(y>-1):
            y=y-1
            while(x>-1):
                x=x-1
                if(environment.room[x][y]==1):
                    print("Location ",x,y," is dirty. Proceeding to cleaning")
                    environment.room[x][y]=0
                    pathMemory[x][y]=1
                    PerfMeasure+=1
                elif(environment.room[x][y]==2):
                    print("Location ", x,y," has obstacle. Proceeding to next location")
                    pathMemory[x][y]=2
                    PerfMeasure
        print("second pass")
        print(environment.room)
        print(pathMemory)


myMemory=memory()
myEnvironment=environment()
myModelBasedAgent=ModelBasedAgent(myEnvironment)