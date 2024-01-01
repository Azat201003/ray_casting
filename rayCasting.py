from setting import *
import math
from map import Map
import pygame


def RayCasting(i, degSee, sc):
    for j in range(longRays):
        jx = math.cos((i * (degRays / countRays) + degSee) - (degRays / 2)) * j * 2 + pos[0]
        jy = math.sin((i * (degRays / countRays) + degSee) - (degRays / 2)) * j * 2 + pos[1]
        
        jjx = jx // sizeX
        jjy = jy // sizeY
        try:
            if Map[int(jjy)][int(jjx)] == 1:
                c = (min(255 / max(j / 2, 0.001) * light, 150), min(255 / max(j / 20, 0.001) * light, 255), min(255 / max(j / 2, 0.001) * light, 150))
                radius = j * math.cos((i * (degRays / countRays) + degSee) - (degRays / 2) - degSee)
                pygame.draw.rect(sc, c, (i * (w / countRays), h / 2 - ((height / 2) / (radius/20)), (w / countRays), height / (radius/20)))
                return
        except IndexError:
            pass
        
    jx = math.cos((i * (degRays / countRays)) - (degRays / 2) + degSee) * longRays * wMap + pos[0]
    jy = math.sin((i * (degRays / countRays)) - (degRays / 2) + degSee) * longRays * hMap + pos[1]

        
