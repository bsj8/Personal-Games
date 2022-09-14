from re import S
from turtle import left
import pygame
from support import import_images
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        options=['yellowbird','bluebird','redbird']
        fullpath='assests/sprites/' + random.choice(options)
        self.frames=import_images(fullpath)
        self.frame_index=1
        self.frame_speed=0.15
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect(center = (x,y))
        self.gravity_speed=0.2
        self.player_speed=-5
        self.direction_y=0
        self.wing_sound=pygame.mixer.Sound('assests/audio/wing.wav')

    def player_gravity(self):
     if self.rect.y<436:
        self.direction_y+=self.gravity_speed
        self.rect.y+=self.direction_y
     else:
        self.rect.y=436

    def player_movement(self,space_up):
        keys=pygame.key.get_pressed()
        if space_up:
           if(self.rect.y>60):
            self.player_jump()

    def player_jump(self):
           self.direction_y=self.player_speed
           self.rect.y+=self.direction_y 
           self.wing_sound.play()

    def Animate(self):   
            self.frame_index+=self.frame_speed
            if self.frame_index > len(self.frames):
                self.frame_index=0

            self.image=self.frames[int(self.frame_index)]
    
    def update(self,jump_check):
        self.player_gravity()
        self.player_movement(jump_check)
        self.Animate()


     
    
