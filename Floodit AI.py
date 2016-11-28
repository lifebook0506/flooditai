import sys, time, random
import pygame
from pygame.locals import *
from copy import deepcopy


#=============================================
#TEST BOARD FUNCTIONS
#Barebones board display and setup. In place of a grid of colors, returns an array of integers
#=============================================
def setup_Board(x,y,variables): 
    
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
    #fills board with move     
    if move == curVal or board[row][col] != curVal:
        return
    board[row][col] = move

    if (row,col) not in filledTiles:
        filledTiles.append((row,col))
        
    if row> 0:
        flood_Fill(board,row-1,col,move,curVal)
    if row < len(board[0])-1:
        flood_Fill(board,row+1,col,move,curVal)
    if col > 0:
        flood_Fill(board,row,col-1,move,curVal)
    if col < len(board)-1:
        flood_Fill(board,row,col+1,move,curVal)
        
    return board
#global variable to be edited by flood_Fill
filledTiles = []

#========================
#very greedy and cobbled together heuristic
#counts tiles filled from base pos
#creates arbitrary move and counts tiles changed by it
def return_Heur(board):
    newBoard = deepcopy(board)
    newBoard = make_Move(100,newBoard)
    return len(filledTiles)


#Sees if board is flooded 
def victory_Bool(board):
    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[x][y] != board[0][0]:
                return False
    return True


#Node will hold floodit state to be used in the search functions
class Node:
    def __init__(self,board,parent,move,depth,cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.f = depth + cost

def findHighF(nodes):
    highest = nodes[0]
    for node in nodes:
        if node.f > highest.f:
            highest = node
    return highest


#=====================================
#Brute force dfs search
#=====================================
def flood_Solver(board,variables,depth_limit):
    base = Node(board,None,None,0,0)
    moves = []
    moves.append(base)

    while True:
        if len(moves) == 0:
            print "NO SOLUTION FOUND"
            break
            
        board = moves.pop(0)
        print_Board(board.board)
        print ""
        if victory_Bool(board.board):
            
            print "SOLVED"
            break
        if board.depth < depth_limit:
            expanded_moves = expand_Moves(board,variables)
            expanded_moves.extend(moves)
            moves = expanded_moves

#==============================
#A* search with greedy heuristic
#==============================
def flood_Huerist(board,variables,limit):
    base = Node(board,None,None,0,return_Heur(board))
    openNodes = []
    closNodes = []

    openNodes.append(base)

    while openNodes >= 0:
        if limit == 0:
            print "max turns reached"
            break
        if len(openNodes) == 0:
            break
        #find highest f value in open nodes
        current_Node = findHighF(openNodes)
        closNodes.append(current_Node)
        print ""
        print_Board(current_Node.board)
        #check to stop
        if victory_Bool(current_Node.board):
            print_Board(current_Node.board)
            print "SOLVED"
            break

        limit = limit -1
        openNodes.remove(current_Node)
        closNodes.append(current_Node)
        
        #generate new set of successors
        successors = expand_Moves(current_Node,variables)

        for successor in successors:
            if successor in closNodes:
                continue
            curScore = current_Node.depth + 1
            if successor not in openNodes:
                openNodes.append(successor)
            elif curScore >= successor.depth:
                continue

            successor.depth = curScore
            successor.f = successor.depth + return_Heur(successor.board)



def expand_Moves(node,variables):
    #returns list of all boards(nodes) made with each variable
    branches = []

    for i in range(variables+1):
        branches.append(Node(make_Move(i,node.board),node,i,node.depth+1,0))
    branches = [node for node in branches if node.board != None]
    
    return branches

def main():
    home = setup_Board(4,4,5)
    print "Base Board"
    print_Board(home)
    flood_Solver(home,5,30)



#Pretty pygame stuff. No time to finish
'''#initialization variabls

TILESIZE = 60
TURNS = 30

#Colors   R   G   B
WHITE = (255,255,255)
RED   = (255, 0,   0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
YELLOW= (255,255,  0)
ORANGE= (255,128,  0)
PURPLE= (255,  0,255)

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((640,640))
    pygame.display.set_caption('Flood-it AI')

    homeBoard = gen_Board(14,14)



def gen_Board(x,y):
    board = [[random.randint(0,variables) for j in range(0,x)] for i in range(0,y)]
    return board

def show_Board(board):
    tempSurf = pygame.Surface(DISPLAYSURF.get_size())
    tempSurf = tempSurf.convert_alpha()
    tempSurf.fill((0,0,0,0))

    for x in range(len(board[0])):
        for y in range(len(board)):
            l,t = home_Pixel(x,y)
            r,g,b = 0
            '''
