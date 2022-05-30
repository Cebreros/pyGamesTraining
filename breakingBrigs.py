import pygame
from pygame import image
from pygame.constants import GL_MULTISAMPLEBUFFERS, QUIT

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breaking Bricks")

#bat image loading
bat = pygame.image.load("./imags/paddle.png")
bat = bat.convert_alpha()
bat_rect = bat.get_rect()


clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

pygame.quit()

