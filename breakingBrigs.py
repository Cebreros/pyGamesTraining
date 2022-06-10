from pickle import TRUE
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breaking Bricks")

#bat image loading
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100

#ball image loading
ball = pygame.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200, 200)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed #speed in x and y direction
ball_rect.topleft = ball_start


#brick image loading
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width()  // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX,brickY))


clock = pygame.time.Clock()
game_over = False
x = 0
while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for b in bricks:
        #display all the brick in the screen
        screen.blit(brick, b)

    #Display bat in the scree.
    screen.blit(bat, bat_rect)

    #Display ball in the scree.
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

    #move the bat with the arrows
    pressed = pygame.key.get_pressed()    
    if pressed[K_LEFT]:
        x += -0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt    
    bat_rect[0] = x 
    
    #move the ball if space bar is pressed
    if pressed[K_SPACE]:
        ball_served = True

    #ball come back when is hit it by the bat    
    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and \
        ball_rect[1] + ball_rect.height >= bat_rect[1] and\
            sy > 0:
            sy *= -1
            sx *= 1.05 #increase the speed of ball in x
            sy *= 1.05 #increase the speed of ball in y
            continue

    delete_brick = None
    for b in bricks:
        bx, by = b
        if  bx <= ball_rect[0] <= bx + brick_rect.width and\
            by <= ball_rect[1] <= by + brick_rect.height:
            delete_brick = b

            #change the direction of the ball when hit a brick
            if ball_rect[0] <= bx + 2:
                sx *= -1
            elif ball_rect[0] >= bx +brick_rect.width - 2:
                sx *= -1
            
            if ball_rect[1] <= by + 2:
                sy *= -1
            elif ball_rect[1] >= by + brick_rect.height -2:
                sy *= -1
            break
        

    
    if delete_brick is not None:
        bricks.remove(delete_brick)
           

    #ball hit top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1
    #ball hit botton
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        #ball_rect[1] = screen.get_height() - ball_rect.height
        #sy *= -1
        ball_served = False
        ball_rect.topleft = ball_start

    #ball hit left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1
    #ball hit right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    #moving the ball
    if ball_served:
        ball_rect[0] += sx    
        ball_rect[1] += sy    
    pygame.display.update()

pygame.quit()

