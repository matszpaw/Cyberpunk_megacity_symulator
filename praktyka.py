import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('run')
clock = pygame.time.Clock()

test_surface = pygame.Surface((30,30))
test_surface.fill('Red')

obrazek = pygame.image.load('ryby.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(obrazek,(0,0))

    pygame.display.update()
    clock.tick(60)