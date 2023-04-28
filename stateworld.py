#!/usr/bin/python3
import random
import time 

# implementing the gridworld example
# from chapter 3 in Barto
# The grid is 5 x 5 in the book pg 71
# cartesian-like coordinates starting at (1.1) in bottom left
# but its confusing its [y,x] so the first element 
# controls the horizontal

# need to implement logic for some kind of bellman-like
# equations. Need to assign state-action pairs an estimated return
# the way I want to do that in this lab is to have the program
# randomly pick a direction and see what the reward is and then
# update the value at that action for that state before changing
# sate and then repeating the process. It could even have a parameter
# for n turns to look ahead for each move



def initGrid():
    grid = []
    rows = 5
    cols = 5
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(Cell(i, j))
        grid.append(row)
    return grid

def printGrid(grid):
    for rows in grid:
        for cell in rows:
            print(f"({cell.x}, {cell.y})", end=", ")
        print()


# so I think it will be something like 
# grid[3][3].updateValue('n', 0.99)

class Cell:
    def __init__(self, x, y):
        self.value = 0
        self.x = x
        self.y = y
        self.position = [x,y]
    

    def printCell(self):
        print(f"cell ({self.x}, {self.y})")
        print(f"{self.value}")

    
# max(a, key=a.get)
# how to get the key of the highest value


class Agent:
    #step1 takeAction:
        #update choice
        #update state
    #step2 getReward:
        #calculate reward
        #update state if necessary
        #update Cell object at 

    def __init__(self, grid):
        self.state = [3,3]
        self.nextState = []
        self.actions = ['n', 'e', 'w', 's'] # North, East, West, or South
        self.choice = ''
        self.reward = 0
        self.grid = grid
    
    #Step 1: take action
    def takeAction(self):
        self.makeChoice()  # updates choice variable
        self.makeMove()  # updates nextState variable
        # print(self.choice)
        # print(self.state)

    # takeAction's internal steps:
    def makeChoice(self):
        random.seed(time.time())
        self.choice = random.choice(self.actions) # policy is to choose a random direction
    
    def makeMove(self):
        if self.choice == 'e':
                self.nextState = [self.state[0] + 1, self.state[1]]
        elif self.choice == 'n':
                self.nextState = [self.state[0], self.state[1] + 1]
        elif self.choice == 's':
                self.nextState = [self.state[0], self.state[1] - 1]
        elif self.choice == 'w':
                self.nextState = [self.state[0] - 1, self.state[1]]

    #Step2 get reward
    def getReward(self):
        if self.nextState[0] < 0:
            self.nextState[0]+=1
            self.reward-=1

        elif self.nextState[1] < 0:
            self.nextState[1]+=1
            self.reward-=1

        elif self.nextState[0] > 4:
            self.nextState[0]-=1
            self.reward-=1

        elif self.nextState[1] > 4:
            self.nextState[1]-=1
            self.reward-=1

        elif self.nextState == [0,2]:
            self.nextState = [2,2]
            self.reward += 10
#            print("Square A, jup to [2,2]")
 #           print(self.nextState)

        elif self.nextState == [0,4]:
            self.nextState = [3,4]
            self.reward += 5
  #          print("Square B, jup to [3,4]")
   #         print(self.nextState)
        
        #update reward:
        #self.state = [yb,xb]

        x = self.nextState[0]
        y = self.nextState[1]

        myReturn = (0.9 * self.grid[x][y].value) + self.reward
        
        x = self.state[0]
        y = self.state[1]


        #print(self.state, self.reward, ' ', myReturn)
        self.state = self.nextState
        self.grid[x][y].value += myReturn * (0.01) 
        self.reward = 0







g0 = initGrid()
printGrid(g0)
t0 = Agent(g0)

for i in range(10000):
    t0.takeAction()
    t0.getReward()

for rows in g0:
    for cell in rows:
        cell.printCell()


