import numpy as np

#2D World -> People fluctuating around central points
#Person with infection leaves infected area for dt
#People on those areas get infected with probability p
#People after t1 die

dt = 3
space = 100
npeople = 1000
ninfected = 1
p_get_infected = .6
lifetime = 50
displacement = 3

class World:
    #Infected area represented by 1, normal area represented by 0
    def __init__(self,space):
        self.x = np.zeros((space,space)).astype('int')
    def checkAreas(self):
        notzeros = np.where(self.x != 0)
        self.x[notzeros] += 1
        uninfected = np.where(self.x > 3)
        self.x[uninfected] = 0

    def writeWorld(self,filename):
        output = open(filename,'w')
        for i in range(len(self.x)):
            for j in range(len(self.x)):
                output.write('{0:d}\t{1:d}\t{2:d}\n'.format(i,j,self.x[i,j]))
        output.close()


class Person:
    def __init__(self,space):
        self.x = np.random.randint(space)
        self.y = np.random.randint(space)
        self.infected = 0
        self.infected_time = 0
    def move(self,world):
        self.motion()
        #If the area is infected the person becomes infected
        if world.x[self.x,self.y] != 0:
            if np.random.random() < p_get_infected:
                if self.infected == 0:
                    self.infected = 1
        #If the person is infected the area becomes infected or it's counter start over
        #The living time of the infected increases
        if self.infected != 0:
            world.x[self.x,self.y] = 1
            self.infected_time += 1

    def motion(self):
        dx,dy = int((np.random.randint(displacement+1))-(displacement/2)),int((np.random.randint(displacement+1))-(displacement/2))
        self.x += dx
        self.y += dy
        if self.x >= space:
            self.x = space-1
        if self.y >= space:
            self.y = space-1
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0


class People:
    def __init__(self,npeople,world):
        self.people = []

        for i in range(npeople):
            self.people.append(Person(space))
        self.people[0].infected = 1
        self.people[0].infected_time += 1
        x,y = self.GetCoordinate(i)
        world.x[x,y] = 1

    def MovePeople(self,world):
        for i in self.people:
            i.move(world)
        self.people = [i for i in self.people if i.infected_time < lifetime]

    def GetInfected(self):
        return len([i for i in self.people if i.infected>0])

        
    def GetCoordinate(self,i):
        return self.people[i].x, self.people[i].y

    def writePeople(self,filename):
        output = open(filename,'w')
        for i in range(len(self.people)):
            x,y = self.GetCoordinate(i)
            output.write('{0:d}\t{1:d}\t{2:d}\n'.format(x,y,self.people[i].infected))
        output.close()


T = 1000
world = World(space)
population = People(npeople,world)
filename = 'world{0:04d}'
i=0
while i < T and population.GetInfected() > 0:
    population.MovePeople(world)
    world.checkAreas()
    population.writePeople(filename.format(i))
    i+=1
    print (i,end='\r')
