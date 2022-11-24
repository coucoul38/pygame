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
img_shield2 = pygame.image.load("img/shield.png").convert_alpha()
shieldCopy = img_shield2.copy()
img_shield = pygame.transform.flip(shieldCopy, True, False)

size_sword = (110,110)
img_sword = pygame.image.load("img/woodenSword.png").convert_alpha()
img_sword = pygame.transform.scale(img_sword, size_sword)
swordCopy = img_sword.copy()
img_sword2 = pygame.transform.flip(swordCopy, True, False)

playersSpeed = 10


def atk(player):
    global img_sword
    global img_sword2d
    if player == "player1":
        print("player 1 attacks")
        
        #for rotation in range(90):
        #    img_sword = pygame.transform.rotate(img_sword, rotation)
        #for rotationBack in range(90):
        #    img_sword = pygame.transform.rotate(img_sword, -rotationBack)

pygame.display.set_caption("The Battle Cats")

player1atk = False
wait = 0

#Run until the player quits
running = True
while running:
    # run the game at a constant 60fps
    clock.tick(60)
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
            #Player 1 ATTACK
            if events.key == pygame.K_e:
                atk("player1")
                player1atk=True
                wait = 60
            #Player 2 ATK
            if events.key == pygame.K_KP_4:
                print("player 2 attacks")
    
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
    if player1atk :
        screen.blit(img_sword,(player1x+80, player1y-10))
    screen.blit(img_sword2,(player2x-80, player2y-10))
    wait = wait -1
    if wait == 0 :
        player1atk=False
    pygame.display.update()
pygame.quit()