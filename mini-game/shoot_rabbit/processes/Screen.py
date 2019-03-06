# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import math

class Screen(object):

    def __init__(self):
        pygame.init()
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.grass = pygame.image.load("resources/images/grass.png")
        self.player = pygame.image.load("resources/images/dude.png")
        self.castle = pygame.image.load("resources/images/castle.png")
        self.arrow = pygame.image.load("resources/images/bullet.png")
        self.position = pygame.mouse.get_pos()
        self.playerpos = [100, 100]
        self.keys = [False, False, False, False]
        self.acc = [0, 0]
        self.arrows = []


    def draw_grass(self):
        for x in range(int(self.width/self.grass.get_width()+1)):
            for y in range(int(self.height/self.grass.get_height()+1)):
                self.screen.blit(self.grass, (x * 100, y * 100))

    def draw_castle(self):
        self.screen.blit(self.castle, (0, 30))
        self.screen.blit(self.castle, (0, 135))
        self.screen.blit(self.castle, (0, 240))
        self.screen.blit(self.castle, (0, 345))

    def draw_player(self):
        self.screen.blit(self.player, self.playerpos)

    def key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                self.keys[0] = True
            elif event.key == K_a:
                self.keys[1] = True
            elif event.key == K_s:
                self.keys[2] = True
            elif event.key == K_d:
                self.keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                self.keys[0] = False
            elif event.key == K_a:
                self.keys[1] = False
            elif event.key == K_s:
                self.keys[2] = False
            elif event.key == K_d:
                self.keys[3] = False
        return self.keys

    def move_player(self, keys):
        if keys[0]:
            self.playerpos[1] -= 5
        elif keys[2]:
            self.playerpos[1] += 5
        if keys[1]:
            self.playerpos[0] -= 5
        elif keys[3]:
            self.playerpos[0] += 5
        return self.playerpos

    def rotate_player(self):
        angle = math.atan2(self.position[1] - (self.playerpos[1] + 32), self.position[0] - (self.playerpos[0] + 26))
        playerrot = pygame.transform.rotate(self.player, 360 - angle * 57.9)
        playerpos1 = (self.playerpos[0]-playerrot.get_rect().width/2, self.playerpos[1]-playerrot.get_rect().height/2)
        self.screen.blit(playerrot, playerpos1)
        return playerpos1

    def shoot_arrow(self, event, playerpos1):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.acc[1] += 1
            self.arrows.append([math.atan2(self.position[1]-(playerpos1[1]+32),self.position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

    def draw_arrow(self):
        for bullet in self.arrows:
            index = 0
            velx = math.cos(bullet[0]) * 10
            vely = math.cos(bullet[0]) * 10
            bullet[1] += velx
            bullet[2] += vely
            if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                self.arrows.pop(index)
            index += 1
            for projectile in self.arrows:
                arrow1 = pygame.transform.rotate(self.arrow, 360-projectile[0]*57.29)
                self.screen.blit(arrow1, (projectile[1], projectile[2]))

    def run(self):
        while True:
            self.screen.fill(0)

            self.draw_grass()
            self.draw_castle()
            playerpos1 = self.rotate_player()
            self.draw_arrow()

            pygame.display.flip()

            for event in pygame.event.get():
                keys = self.key_event(event)
                self.move_player(keys)
                self.shoot_arrow(event, playerpos1)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
