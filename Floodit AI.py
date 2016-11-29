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
    maxFill = len(board) * len(board[0])
    return maxFill - len(filledTiles)


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

def findLowF(nodes):
    lowest = nodes[0]
    for node in nodes:
        if node.f < lowest.f:
            lowest = node
    return lowest

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
        current_Node = findLowF(openNodes)
        closNodes.append(current_Node)
        
        #check to stop
        if victory_Bool(current_Node.board):
            draw_Moves(current_Node)
            print "SOLVED"
            print_Board(current_Node.board)
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



finalMoves = []
def draw_Moves(node):
    if node.parent == None:
         
         print_Moves(finalMoves,node.board)
    else:
        finalMoves.append(node.move)
        draw_Moves(node.parent)

def print_Moves(moveList,board):
    moveList = finalMoves[::-1]
    for i in moveList:
        board = make_Move(i,board)
        print_Board(board)
        print ""
    print "Move list: " + str(moveList)    
def expand_Moves(node,variables):
    #returns list of all boards(nodes) made with each variable
    branches = []

    for i in range(variables+1):
        branches.append(Node(make_Move(i,node.board),node,i,node.depth+1,0))
    branches = [node for node in branches if node.board != None]
    
    return branches

def main():
    home = setup_Board(14,14,4)
    print "Starting board"
    print_Board(home)
    flood_Huerist(home,4,1000)
