import sys, time, random
import pygame
from pygame.locals import *

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
def setup_Board():
    x = int(input("How many columns? "))
    y = int(input("How many rows? "))
    variables = int(input("How many numbers to fill? "))
    
    board = [[random.randint(0,variables) for j in range(0,x)] for i in range(0,y)]


    for line in board:
        print line
