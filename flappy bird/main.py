from re import I
import pygame
from level import Level

pygame.init() 
screen=pygame.display.set_mode((288,512))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load('assests/sprites/icon/flappy bird icon.png'))
clock=pygame.time.Clock()
running=True  
level=Level(screen) 
pipe_timer=pygame.USEREVENT
pygame.time.set_timer(pipe_timer,1600)
game_over=False
start=False

while running: 
    space_up=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                space_up=True
                start=True
        elif event.type==pipe_timer:   
            level.create_pipes()
    screen.fill('black')
    if not game_over and start:
        level.run(space_up)
    else:
        level.display_background()
        level.display_floor() 
        level.display_score()     
        image=pygame.image.load('assests/sprites/intro/message.png')
        screen.blit(image,(55,100))
        if space_up:
            level=Level(screen)
            game_over=False
    game_over=level.check_collision()
    pygame.display.update()
    clock.tick(60)