import pygame
from os import walk

def import_images(path):
    container=[]
    for _,__,images in walk(path):
        for image_name in images:
            full_path=path + '/' + image_name
            surfaces=pygame.image.load(full_path).convert_alpha()
            container.append(surfaces)
    return container


