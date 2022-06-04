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
    pygame.display.update()

pygame.quit()

