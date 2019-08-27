#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:42:05 2019

@author: Thiago da Silva Teixeira
"""

import sys
import os
import time
import pygame
import random
import numpy as np
from itertools import permutations

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)
yellow   = ( 255, 255,   0)

fundo = (35,32,39)

yin = (240, 217, 181)
yang = (181, 136, 99)

def showTable(tabuleiro):
    for c in tabuleiro:
        for l in c:
            print(l+' ',end='')
        print('')
    print('----')

def showCase(caso):
    tabuleiro = [['0' for i in range(8)] for j in range(8)]
    i = 0
    for j in caso:
        tabuleiro[i][j] = 'Q'
        i += 1
    showTable(tabuleiro)

def validarSolucao(queens):
    # mostrar no terminal
    #tabuleiro = [['0' for i in range(8)] for j in range(8)]
    #for q in queens: tabuleiro[q[0]][q[1]] = 'Q'
    #showTable(tabuleiro)

    for q1 in queens:
        for q2 in queens:
            if q1[0] == q2[0] and q1[1] == q2[1]: continue
            if q1[0]-q1[1] == q2[0]-q2[1] or q1[0]+q1[1] == q2[0]+q2[1]:
                return False

    return True

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def showText(string, x, y, small=False):
    if small:
        text = fontSmall.render(string, True, white, fundo)
    else:
        text = font.render(string, True, white, fundo)

    textRect = text.get_rect()
    textRect.center = (x, y )
    screen.blit(text, textRect)


pygame.init()
pygame.display.set_caption('8 Rainhas')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()
pygame.display.update()

queenSprite = get_image('queen.png')

font = pygame.font.Font('freesansbold.ttf', 32)
fontSmall = pygame.font.Font('freesansbold.ttf', 10)

list = [i for i in range(8)]
#random.shuffle(list)

offX = 50
offY = 50

encontrados = []

queens = np.array([[0,0] for i in range(8)])

for caso in permutations(list):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #showCase(caso)
        # [[i,caso[i]]
        for i in range(8):
            queens[i][0] = i
            queens[i][1] = caso[i]

        screen.fill(fundo)
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    pygame.draw.rect(screen, yin, ((i+1)*offX,(j+1)*offY,50,50))
                else:
                    pygame.draw.rect(screen, yang, ((i+1)*offX,(j+1)*offY,50,50))

        for q in queens:
            screen.blit(queenSprite, ((q[0]+1)*offX,(q[1]+1)*offY))

        showText(str(caso), 625, 65)

        step = 0
        for i in range(4):
            showText('('+str(caso[i])+','+str(i)+')', 575, 100+step)
            step += 35

        step = 0
        for i in range(4,8):
            showText('('+str(caso[i])+','+str(i)+')', 675, 100+step)
            step += 35

        step = 0
        coluna = 0
        for e in encontrados:
            showText(str(e), 500+coluna, 230+step, True)
            step += 10
            if step >= 310:
                step = 0
                coluna += 100

        if validarSolucao(queens):
            encontrados.append(caso)
            #print(caso)
            print("Achou:",caso)

            showText("Caso encontrado", 250, 500)

            pygame.display.flip()
            time.sleep(1)
            #done = True


        pygame.display.flip()
        #clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(30)
time.sleep(200)

pygame.quit()
