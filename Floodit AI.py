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
    variables = int(input("How many numbers to fill? "))
    
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
    flood_Fill(board,0,0,move,board[0][0])
    return newBoard

def flood_Fill(board,row,col,move,curVal):
    
    if move == curVal or board[row][col] != curVal: 
        return
    board[row][col] = move
    if row> 0:
        flood_Fill(board,curVal,move,row-1,col)
    if row < len(board[0])-1:
        flood_Fill(board,curVal,move,row+1,col)
    if col > 0:
        flood_Fill(board,curVal,move,row,col-1)
    if col < len(board)-1:
        flood_Fill(board,curVal,move,row,col+1)
        
    newBoard = deepcopy(board)
    
    return newBoard
