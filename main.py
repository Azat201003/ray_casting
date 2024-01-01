import pygame
from setting import *
import rayCasting
from map import Map
import player
import math

P = player.Player()

pygame.init()

sc = pygame.display.set_mode((w, h))


while True:
    # sc.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()  
    pygame.draw.rect(sc, (200, 100, 50), (0, h/2, w, h/2))
    pygame.draw.rect(sc, (20, 10, 200), (0, 0, w, h/2))
    
    pos[1] = P.move()[1]
    pos[0] = P.move()[0]
    degSee = P.deg_move()
                
    for i in range(countRays):
        rayCasting.RayCasting(i, degSee, sc)
    
    for i in range(wMap):
        for j in range(hMap):
            if Map[j][i]:
                pygame.draw.rect(sc, (100, 0, 0), (i*(wMiniMap/wMap), j*(hMiniMap/hMap), sizeX / delMimiMap, sizeY / delMimiMap), 3)
        
    pygame.draw.circle(sc, (200, 100, 100), (pos[0] / delMimiMap, pos[1] / delMimiMap), 7)
    
    jx = math.cos(degSee) * 20 + pos[0] / 4
    jy = math.sin(degSee) * 20 + pos[1] / 4
    pygame.draw.line(sc, (10, 200, 100),  (pos[0] / delMimiMap, pos[1] / delMimiMap), (jx, jy), delMimiMap)
       
    pygame.display.flip()
