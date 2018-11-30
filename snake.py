import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 155, 0)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Andrew\'s Snake Game')

pygame.display.update()


#frames per second
clock = pygame.time.Clock()

block_size = 10
FPS = 30

#font object
font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList):
    for elementXY in snakeList:

        pygame.draw.rect(gameDisplay, green, [elementXY[0],elementXY[1],block_size,block_size])


def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    #put the font on our game screen
    gameDisplay.blit(screen_text,[display_width/2, display_height/2])

def gameLoop():

    gameExit = False
    gameOver = False

    #first location head of the snake
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    #we do not want the randomly generated apples to appear from 800-810, which will not appear on the screen
    #with '- block_size range is reduced to 0 -790, where the block will fill with 790-800
    #round function will reduce or in crease the block to a multiple of 10, needed for overlapping when snake eats an apple
    randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
    

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #event is local variable, event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    gameExit = True
            #event is keydown
            if event.type == pygame.KEYDOWN:
                #event is left key
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0

        #goes off screen, game over
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0
            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         lead_y_change = 0
                
            #print(event)
        lead_x += lead_x_change
        lead_y += lead_y_change


        gameDisplay.fill(white)

        #pygame.draw.rect('Surface', 'color', '[x,y,size(x,y)])
        #using my lead_x and lead_y variable allows me to move our rectangle
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        snake(block_size, snakeList)
        #fill with rectangle, is faster processing
        #gameDisplay.fill(red, rect=[200,200,50,50])

        pygame.display.update()
        #higher fps means more processing power is used

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
            snakeLength +=1
        clock.tick(FPS)


    pygame.quit()
    quit()

gameLoop()