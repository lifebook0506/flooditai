import sys, time, random
import pygame
from pygame.locals import *
from copy import deepcopy

#initialization variabls

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
'''
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

def return_Heur(move,board):
    newBoard = deepcopy(board)
    newBoard = make_Move(move,newBoard)
    h = flood_Count(newBoard,0,0,newBoard[0][0],move,[])
    return len(h)

def flood_Fill(board,row,col,move,curVal):
    #fills board with move returns None if move is the same as current home    
    if move == curVal or board[row][col] != curVal:
        return
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

def flood_Count(board,row,col,move,curVal,filledTiles):
    board = deepcopy(board)
    if move == curVal:
        if (row,col) in filledTiles:
            return
        else:
            filledTiles.append((row,col))
    elif board[row][col] != curVal:
        return
    board[row][col] = move
    if (row,col) not in filledTiles:
        filledTiles.append((row,col))
    
    if row> 0:
        flood_Count(board,row-1,col,move,curVal,filledTiles)
    if row < len(board[0])-1:
        flood_Count(board,row+1,col,move,curVal,filledTiles)
    if col > 0:
        flood_Count(board,row,col-1,move,curVal,filledTiles)
    elif col < len(board)-1:
        flood_Count(board,row,col+1,move,curVal,filledTiles)

    return filledTiles

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


#======dfs search
        
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


    
