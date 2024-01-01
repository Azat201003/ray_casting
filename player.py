from setting import *
import pygame
import math
import map

class Player:
    def __init__(self) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.degSee = degSee
    
    def move(self):
        keys = pygame.key.get_pressed()
        jx = math.cos(self.degSee) * speed
        jy = math.sin(self.degSee) * speed
        if keys[pygame.K_a]:
            if map.Map[int(pos[1] / (h / hMap))][int((self.x + jy) / (w / wMap))] != 1:
                self.x += jy
            if map.Map[int((self.y + -jx) / (h / hMap))][int(pos[0] / (w / wMap))] != 1:
                self.y += -jx
        if keys[pygame.K_d]:
            if map.Map[int(pos[1] / (h / hMap))][int((self.x + -jy) / (w / wMap))] != 1:
                self.x += -jy
            if map.Map[int((self.y + jx) / (h / hMap))][int(pos[0] / (w / wMap))] != 1:
                self.y += jx
        if keys[pygame.K_w]:
            if map.Map[int(pos[1] / (h / hMap))][int((self.x + jx) / (w / wMap))] != 1:  
                self.x += jx
            if map.Map[int((self.y + jy) / (h / hMap))][int(pos[0] / (w / wMap))] != 1:
                self.y += jy
        if keys[pygame.K_s]:
            if map.Map[int(pos[1] / (h / hMap))][int((self.x + -jx) / (w / wMap))] != 1:  
                self.x += -jx
            if map.Map[int((self.y + -jy) / (h / hMap))][int(pos[0] / (w / wMap))] != 1:
                self.y += -jy
                    
        return (self.x, self.y)
    
    def deg_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.degSee -= speed2
        if keys[pygame.K_RIGHT]:
            self.degSee += speed2
        
        return self.degSee