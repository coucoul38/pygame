import pygame
pygame.init()


# Set up the drawing window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

#player1
player1x = 0
player1y = 0
player1size = 100
img_player1 = pygame.image.load("img/cat1.jpg")

#player2
player2size=100
player2x = displayWidth-player2size
player2y = displayHeight-player2size
img_player2 = pygame.image.load("img/cat2.jpg")


pygame.display.set_caption("The Battle Cats")

#Run until the player quits
running = True
while running:
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
    # Changing surface color
    screen.fill(backgroundColor)

    pygame.display.update()
pygame.quit()