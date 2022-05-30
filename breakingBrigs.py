import pygame
#from pygame import image
#from pygame.constants import GL_MULTISAMPLEBUFFERS, QUIT

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breaking Bricks")

#bat image loading
bat = pygame.image.load("./images/paddle.png")
bat = bat.convert_alpha()
bat_rect = bat.get_rect()

#ball image loading
ball = pygame.image.load("./images/football.png")
ball = ball.convert_alpha()
ball_rect = ball.get_rect()

#brick image loading
brick = pygame.image.load("./images/brick.png")
brick = brick.convert_alpha()
brick_rect = brick.get_rect()

clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

pygame.quit()

