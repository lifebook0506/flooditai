import sys, time, random
#import pygame
#from pygame.locals import *
from copy import deepcopy

'''pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
'''
#Barebones board display and setup. In place of a grid of colors, returns an array of integers
def setup_Board():
    x = int(input("How many columns? "))
    y = int(input("How many rows? "))
    variables = 6
    
    board = [[random.randint(0,variables) for j in range(0,x)] for i in range(0,y)]
    return board

def print_Board(board):
    for line in board:
        print line
#------------------------------------------------------
#Makes a move and returns the board along with a total number of changed tiles
#resulting from it.
def make_Move(move,board):
    newBoard = deepcopy(board)
    newBoard = flood_Fill(newBoard,0,0,move,board[0][0])
    #return newBoard
    return newBoard


def flood_Fill(board,row,col,move,curVal):
    #fills board with move returns None if move is the same as current home    
    if move == curVal or board[row][col] != curVal:
        return None
    board[row][col] = move
    
    if row> 0:
        flood_Fill(board,row-1,col,move,curVal)
    if row < len(board[0])-1:
        flood_Fill(board,row+1,col,move,curVal)
    if col > 0:
        flood_Fill(board,row,col-1,move,curVal)
    if col < len(board)-1:
        flood_Fill(board,row,col+1,move,curVal)
        
    
    return board

#Sees if board is flooded 
def victory_Bool(board):
    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[x][y] != board[0][0]:
                return False
    return True


#=============================
#NOT DONE
#=============================
#Returns how many blocks are flooded
def quantify_Flood(board):
    count = 0
    floodVal = board[0][0]
    return 0




#Node will hold floodit state to be used in the search functions
class Node:
    def __init__(self,board,parent,move,depth,cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.f = depth + cost


def flood_Solver(board,variables,limit):
    base = Node(board,None,None,0,0)

def expand_Moves(node,variables):
    #returns list of all boards(nodes) made with each variable
    branches = []

    for i in range(variables):
        branches.append(Node(make_Move(i,node.board),node,i,node.depth+1,0))
    branches = [node for node in branches if node.board != None]
    
    return branches

def main():
    home = setup_Board()
    variables = 6

    print_Board(home)
    print("Ready for move")

    homeNode = Node(home,None,None,0,0)
    moveSet = expand_Moves(homeNode,6)

    print "Branches"
    for move in moveSet:
        print_Board(move.board)
        print ""



    
