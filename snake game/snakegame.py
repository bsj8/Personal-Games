from cmath import rect
from operator import truediv
from tkinter import Y
from tokenize import triple_quoted
from turtle import down, left, right, up
import pygame
import random


pygame.init()
screen= pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")
icon= pygame.image.load("snakesymbol.png")
background=pygame.image.load("grass.png")
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
up_check=True
down_check=True
left_check=True
right_check=True
running = True
playing=True

applex=random.randint(32,768)
appley=random.randint(32,568)
apple_rect=pygame.Rect(applex,appley,30,30)


snakex=370
snakey=480
x_velocity=0;
y_velocity=0;
snake_rect=[]
snake_rect.append(pygame.Rect(snakex,snakey,30,30))
snake_rect.append(pygame.Rect(snakex,snakey,30,30))

score_value=0

def show_message(info,x,y):
    font=pygame.font.Font('freesansbold.ttf',20)
    message=font.render(info,True,(255,255,255))
    screen.blit(message,(x,y))

def apple_collision(score):
    if(snake_rect[0].colliderect(apple_rect)):
        snake_rect.append(pygame.Rect(snake_rect[len(snake_rect)-1].x,snake_rect[len(snake_rect)-1].y+3,30,30))
        apple_rect.x=random.randint(32,768)
        apple_rect.y=random.randint(32,568)
        score+=1
    return score

def other_collision():
        if(snake_rect[0].x==770 or snake_rect[0].x==0):
           msg="Game over: Press Q to quit or C to play again"
           show_message(msg,180,270)
           return False 
        if(snake_rect[0].y==570 or snake_rect[0].y==0):
            msg="Game over: Press Q to quit or C to play again"
            show_message(msg,180,270)
            return False
        for x in range(len(snake_rect)):
            if(x+1<len(snake_rect)-1):
                if(snake_rect[0].x==snake_rect[x+1].x and snake_rect[0].y==snake_rect[x+1].y):
                 msg="Game over: Press Q to quit or C to play again"
                 show_message(msg,180,270)
                 return False
        return True

def show():
    pygame.draw.rect(screen,pygame.Color("red"),apple_rect)
    
    for x in range(len(snake_rect)):
        pygame.draw.rect(screen,pygame.Color("green"),snake_rect[x])

    snake_rect.pop()
    snake_rect.insert(0,pygame.Rect(snake_rect[0].x+x_velocity,snake_rect[0].y+y_velocity,30,30))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                right_check=False
                down_check=True
                up_check=True
                if(left_check):
                    x_velocity=-5;
                    y_velocity=0;
            if event.key==pygame.K_RIGHT:
                left_check=False
                down_check=True
                up_check=True
                if (right_check):
                    x_velocity=5;
                    y_velocity=0;
            if event.key==pygame.K_UP:
                down_check=False
                right_check=True
                left_check=True
                if(up_check):
                    y_velocity=-5;
                    x_velocity=0;
            if event.key==pygame.K_DOWN:
                up_check=False
                right_check=True
                left_check=True
                if(down_check):               
                    y_velocity=5;
                    x_velocity=0;
            if event.key==pygame.K_q:
                running=False;
            if event.key==pygame.K_c:
                playing=True
                up_check=True
                down_check=True
                left_check=True
                right_check=True
                snakex=370
                snakey=270
                score_value=0
                new_snake=[]
                new_snake.append(pygame.Rect(snakex,snakey,30,30))
                new_snake.append(pygame.Rect(snakex,snakey,30,30))
                snake_rect= new_snake
            
    playing=other_collision()
    if(playing):    
        screen.fill((0,0,0))
    else:
        x_velocity=0
        y_velocity=0    
    show()
    score_value=apple_collision(score_value)
    msg="Score: " + str(score_value)
    show_message(msg,10,10)
    pygame.display.update()
    clock.tick(60)