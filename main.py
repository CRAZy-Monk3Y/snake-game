import pygame #IMPORT PYGAME
from datetime import datetime #IMPORT DATETIME FUNCTION
import time #IMPORT TIME
import random #IMPORT RANDOM FUNCTION

pygame.init() #INITIATING PYGAME

white = (255, 255, 255) #DEFINING ALL COLORS
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800 #DEFINING SCREEN DISPLAY DIMENSIONS
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))  #ENABLING DISPLAY 
pygame.display.set_caption('Snake Game by Tathagata.') #WRITING SCREEN CAPTION

clock = pygame.time.Clock() #SETTING THE CLOCK
start_time = time.time()
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25) #DEFINING THE GAME FONTS
score_font = pygame.font.SysFont("comicsansms", 35)
time_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score): #SCORE BLIT
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def times(current_time): #TIME BLIT
    value = time_font.render("Time -" + str(current_time), True, black)
    dis.blit(value, [540, 0])


def our_snake(snake_block, snake_list): #SNAKE DEFINIG
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color): #MESSAGE PROMPMPT
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 8, dis_height / 3])


def gameLoop(): #MAIN GAME LOOP
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            times(T)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        T = round((time.time() - start_time), 2)
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
