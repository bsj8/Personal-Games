import pygame
from support import import_images

class Pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,path):
        super().__init__()
        self.pipe_images=import_images(path)
        self.image=self.pipe_images[0]
        self.rect=self.image.get_rect(bottomleft=(x,y))

    def update(self,x_shift):
        self.rect.x+=x_shift
        if(self.rect.x<-50):
            self.kill()