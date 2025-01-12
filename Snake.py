#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pygame
import sys
import random


# In[33]:


colors = ["blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "gray", "brown", "cyan", "magenta"]
color_background = input("Choose the color of the background: red,blue,green,yellow,orange,purple,pink,black,white,gray,brown,cyan,magenta,random,psycho: ")
if color_background== 'random':
    color_background= (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
elif color_background== 'psycho':
    psycho=color_background
    color_background= (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color=color_background
else:
    psycho='none'

if psycho=='psycho':
    color_snake='psycho'
    psycho_snake=color_snake
    color_snake= (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
else:
    color_snake = input("Choose the color of the snake: red,blue,green,yellow,orange,purple,pink,black,white,gray,brown,cyan,magenta,random: ")
    if color_snake== 'random':
        color_snake= (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        psycho='none'



# In[32]:


pygame.init()

SW,SH = 800, 800

BLOCK_SIZE= 50
FONT = pygame.font.SysFont("arial", BLOCK_SIZE*2)

screen= pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake!")
clock= pygame.time.Clock()


class Snake:
    def __init__(self):
        self.x, self.y= 50, 100
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False
        

    def update(self):
        global apple
        for square in self.body:
            if self.head.x == square.x and self.head == square.y:
                self.dead= True
            if self.head.x not in range(0, SW) or self.head.y not in range(0,SH):
                self.dead=True

        if self.dead:
            self.x, self.y= 50, 100
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple=Apple()
        
        self.body.append(self.head)
        for i in range(0, len(self.body)-1):
            self.body[i].x, self.body[i].y= self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)



class Apple:
    def __init__(self):
        self.x= int(random.randint(0, SW)/BLOCK_SIZE)*BLOCK_SIZE
        self.y= int(random.randint(0,SH)/BLOCK_SIZE)*BLOCK_SIZE
        self.rect= pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        

    def update(self):
        pygame.draw.rect(screen, 'red', self.rect)

        


def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0,SH, BLOCK_SIZE):
            rect = pygame.Rect(x,y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, '#3c3c3b', rect, 1)

score= FONT.render('1',True, 'yellow')
score_rect=score.get_rect(center=(50,50))

drawGrid()

snake= Snake()
apple=Apple()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type== pygame.KEYDOWN:
            if psycho=='psycho':
                color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                color_snake = tuple(255 - c for c in color)  # Inverte ogni componente del colore
            else:
                pass
            if event.key == pygame.K_DOWN:
                snake.ydir=1
                snake.xdir=0
            elif event.key == pygame.K_UP:
                snake.ydir=-1
                snake.xdir= 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir= 0
                snake.xdir=-1
                

            
    snake.update()
    screen.fill(color)
    drawGrid()

    apple.update()
    score= FONT.render(f'{len(snake.body)-1}', True, 'yellow')
    

    
    pygame.draw.rect(screen, color_snake, snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, color_snake, square)

    screen.blit(score, score_rect)
    
    if snake.head.x == apple.x and snake.head.y==apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple=Apple()
    pygame.display.update()
    clock.tick(10)


