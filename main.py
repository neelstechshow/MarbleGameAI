import random
import math
class MarbleState:
  def __init__(self, number, turn):
    self.number = number
    self.children = []
    self.bestChild = None
    self.value = 0
    self.turn = turn
    
  
  def add_child(self, child):
    self.children.append(child)
    
  def set_best_child(self):
    if self.number == 0:
      if self.turn == 1:
        self.value = 10
      else:
        self.value = -10
        
    else:
      for i in self.children:
        i.set_best_child()
      
      if self.turn == 2:
        highest = -math.inf
        bestC = None
        for x in self.children:
          if x.value > highest:
            highest = x.value
            bestC = x
            
        self.value = highest
        self.bestChild = bestC
        
      else:
        lowest = math.inf
        bestC = None
        for x in self.children:
          if x.value < lowest:
            lowest = x.value
            bestC = x
            
        self.value = lowest
        self.bestChild = bestC
        
      

  
class Graph: 
  def __init__(self):
    self.marbles = random.randint(10, 25)
    self.root = MarbleState(self.marbles, 1)
    self.build_tree(self.root)
    self.root.set_best_child()
    
  def build_tree(self, currentNode):
    if self.root.number == 0:
      return
    
    max1 = 4
    if currentNode.number < 3:
      max1 = currentNode.number + 1
    
    if currentNode.turn == 1:
      turn = 2
    else:
      turn = 1
      
    
    for i in range(1, max1):
      child = MarbleState(currentNode.number-i, turn)
      currentNode.add_child(child)
    
    for x in currentNode.children:
      self.build_tree(x)
    
  def play_game(self):
    currentNode = self.root
    turn = 1
    inputCap = 3
    input("Just play, press enter, don't lose, your an embarresment to society \n")
    while True:
      if currentNode.number < 3:
        inputCap = currentNode.number
      while True:
        num1 = int(input((f'\n It is player 1s turn, there are {currentNode.number} marbles left, how many marbles are you picking. (CAP IS {inputCap}):  ')))
        if num1 > inputCap or num1 <= 0:
          print('\n NOPE! ENTER A VALID NUMBER, YOUR ALREADY AN EMBARRESMENT TO SOCIETY \n ')
          
        else:
          break
      for i in currentNode.children:
        if i.number == currentNode.number - num1:
          currentNode = i
          break
      
      if currentNode.number <= 0:
        print(f'\n Player 1 Has Won! \n')
        return
        
      if turn == 1:
        turn = 2
      else:
        turn = 1
        
      marblesTaken = currentNode.number - currentNode.bestChild.number  
      currentNode = currentNode.bestChild
      print(f'\n The AI has taken {marblesTaken} marbles, now there are {currentNode.number} marbles left')
      
      if currentNode.number <= 0:
        print(f'\n AI Has Won! \n')
        return
        
      
        
                
g = Graph()
g.play_game()
            
      
