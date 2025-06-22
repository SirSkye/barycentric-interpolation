from utils import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
ANCHOR = [Point]
while running:
    # POLL EVENTs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # RENDER
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()