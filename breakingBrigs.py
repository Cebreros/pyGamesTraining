import pygame
#from pygame import image
#from pygame.constants import GL_MULTISAMPLEBUFFERS, QUIT

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breaking Bricks")

#bat image loading
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()

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
while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for b in bricks:
        screen.blit(brick, b)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
    pygame.display.update()

pygame.quit()

