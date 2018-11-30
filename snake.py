import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

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
    #this is our gameLoop
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
        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
        #fill with rectangle, is faster processing
        #gameDisplay.fill(red, rect=[200,200,50,50])

        pygame.display.update()
        #higher fps means more processing power is used
        clock.tick(FPS)


    pygame.quit()
    quit()

gameLoop()