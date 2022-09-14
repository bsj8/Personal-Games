import pygame
from player import Player
from pipes import Pipes
from support import import_images
from random import randint

class Level():
    def __init__(self,display_surface,):
        
        self.display_surface=display_surface
        self.x_shift=-2
        self.game_over=False
        self.point_sound=pygame.mixer.Sound('assests/audio/point.wav')

        self.score=0
        self.numbers=import_images('assests/sprites/numbers')
        
        self.backgrounds=import_images('assests/sprites/background')
        self.background=self.backgrounds[randint(0,1)]

        self.floor1=pygame.image.load('assests/sprites/floor/base.png').convert_alpha()
        self.floor1_rect=self.floor1.get_rect(topleft=(0,460))
        self.floor2=pygame.image.load('assests/sprites/floor/base.png').convert_alpha()
        self.floor2_rect=self.floor2.get_rect(topleft=(288,460))

        self.player=pygame.sprite.GroupSingle()
        self.player.add(Player(144,256))

        self.pipes=pygame.sprite.Group()

    def check_collision(self):
        player=self.player.sprite
        if player.rect.colliderect(self.floor1_rect) or player.rect.colliderect(self.floor2_rect):
             return True
        for sprites in self.pipes:
            if sprites.rect.colliderect(player.rect):
                return True
            if sprites.rect.right==player.rect.left or sprites.rect.right==player.rect.left-1:
              self.score+=1
              self.point_sound.play()


    def create_pipes(self):
        self.pipe_xpos=288 + randint(100,200)
        self.pipe_ypos1=randint(50,300)
        self.pipe_ypos2=self.pipe_ypos1 + 430
        self.pipes.add(Pipes(self.pipe_xpos,self.pipe_ypos2,'assests/sprites/pipes'))
        self.pipes.add(Pipes(self.pipe_xpos,self.pipe_ypos1,'assests/sprites/pipes reversed'))
       
    def display_background(self):
        self.display_surface.blit(self.background,(0,0))

    def display_score(self):
        range=[]
        range.append
        score_pos=135
        if self.score==0:
            range.append(0)
        if self.score>0:
            for n in str(int(self.score/2)):
                if n!='.' and  (not n in range):
                    range.append(int(n))
                    
        for i in range:
            self.display_surface.blit(self.numbers[i],(score_pos,10))
            score_pos+=30


    def display_floor(self):
        if  self.game_over:
            self.x_shift=0
        self.display_surface.blit(self.floor1,self.floor1_rect)
        self.display_surface.blit(self.floor2,self.floor2_rect)
        self.floor1_rect.x+=self.x_shift
        self.floor2_rect.x+=self.x_shift
        if(self.floor2_rect.topleft==(0,460)):
             self.floor1_rect.topleft=(288,460)   
        if(self.floor1_rect.topleft==(0,460)):
            self.floor2_rect.topleft=(288,460)

    def run(self,space_up):
            self.display_background()
            self.pipes.draw(self.display_surface)
            self.player.draw(self.display_surface)
            self.display_floor()
            #if not self.game_over:
            self.pipes.update(self.x_shift)
            self.player.update(space_up)
            self.display_score()
            
          
     
        
