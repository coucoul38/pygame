#Simple pygame program

import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#Run until the player quits
running = True
while running:
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False