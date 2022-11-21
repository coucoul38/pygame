#Simple pygame program
# TUTORIAL : https://realpython.com/pygame-a-primer/

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

    #Fill the background in pink
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (250,0,0), (250, 250), 75)

    #push to display
    pygame.display.flip()

pygame.quit()