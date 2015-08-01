__author__ = 'Orthanc Minas'

import pygame, os, sys
from pygame.locals import *

screen_size = (500, 500)

class Start(object):
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
        pygame.display.set_caption("Company Symulator")
        self.surface = pygame.display.set_mode(screen_size, flag)
        self.gamestate = 1  # 1 - run, 0 - exit
        self.loop()

    def game_exit(self):
        exit()

    def loop(self):
        while self.gamestate==1:
           for event in pygame.event.get():
               if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                   self.gamestate=0
        self.game_exit()

if __name__ == '__main__':
   Start()