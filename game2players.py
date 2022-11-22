import pygame
import pygame.time
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

#player1
player1x = 0
player1y = 0
player1yVelocity = 0
player1xVelocity = 0
player1size = 100
img_player1 = pygame.image.load("img/cat1.jpg")

#player2
player2size=100
player2x = displayWidth-player2size
player2y = displayHeight-player2size
player2yVelocity = 0
player2xVelocity = 0
img_player2 = pygame.image.load("img/cat3.jpg")

#other
img_shield2 = pygame.image.load("img/shield.png")
shieldCopy = img_shield2.copy()
img_shield = pygame.transform.flip(shieldCopy, True, False)

img_sword = pygame.image.load("img/woodenSword.png")
swordCopy = img_sword.copy()
img_sword2 = pygame.transform.flip(swordCopy, True, False)


playersSpeed = 10

pygame.display.set_caption("The Battle Cats")

def player1atk():
    print("player 1 attacks !")
    screen.blit(img_sword, (player1x, player1y))
    pygame.display.update()

def player2atk():
    print("player 2 attacks !")

#Run until the player quits
running = True
while running:
    clock.tick(60)
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
            if events.key == pygame.K_e:
                player1atk()
            if events.key == pygame.K_KP_4:
                player2atk()
    
    pressed = pygame.key.get_pressed()
    #PLAYER 1 Y
    if pressed[pygame.K_z]:
        player1yVelocity = -playersSpeed
    elif pressed[pygame.K_s]:
        player1yVelocity = playersSpeed
    else :
        player1yVelocity = 0
    # PLAYER 1 X
    if pressed[pygame.K_d]:
        player1xVelocity = playersSpeed
    elif pressed[pygame.K_q]:
        player1xVelocity = -playersSpeed
    else :
        player1xVelocity = 0

    #PLAYER 2 Y
    if pressed[pygame.K_KP_5]:
        player2yVelocity = -playersSpeed
    elif pressed[pygame.K_KP_2]:
        player2yVelocity = playersSpeed
    else :
        player2yVelocity = 0
    # PLAYER 1 X
    if pressed[pygame.K_KP_3]:
        player2xVelocity = playersSpeed
    elif pressed[pygame.K_KP_1]:
        player2xVelocity = -playersSpeed
    else :
        player2xVelocity = 0

    #Apply player 1 movement
    player1x = player1x + player1xVelocity
    player1y = player1y + player1yVelocity
    #Apply player 2 movement
    player2x = player2x + player2xVelocity
    player2y = player2y + player2yVelocity

    # BOUNDING BOX
    # Player 1
    if player1x > displayWidth - player1size:
        player1x = displayWidth - player1size
    elif player1x < 0 :
        player1x = 0
    if player1y > displayHeight - player1size:
        player1y = displayHeight - player1size
    elif player1y < 0 :
        player1y = 0
    # Player 2
    if player2x > displayWidth - player1size:
        player2x = displayWidth - player1size
    elif player2x < 0 :
        player2x = 0
    if player2y > displayHeight - player1size:
        player2y = displayHeight - player1size
    elif player2y < 0 :
        player2y = 0

    screen.fill(backgroundColor)
    screen.blit(img_player1,(player1x, player1y))
    screen.blit(img_player2,(player2x, player2y))

    pygame.display.update()
pygame.quit()