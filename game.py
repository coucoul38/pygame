#Simple pygame program
# TUTORIAL : https://realpython.com/pygame-a-primer/
from random import *
import pygame
pygame.init()

# Set up the drawing window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (0,0,0)
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

#creating the Rocket
xRocket = 210
yRocket = 300
widthRocket = 100
heightRocket = 91
rocketXVector = 0
rocketYVector=0

#creating the planets
xPlanet = randint(30, 130)
yPlanet = 20
widthPlanet= 100
heightPlanet = 100
xBetweenPlanets = 350
yBetweenPlanets = 125
planetSpeed = 3

#Points and other
puntos = 0
font = pygame.font.Font(None, 24) #font size
score = font.render("0 puntos", 1, (255, 0, 0))

#Images
img_planet = pygame.image.load("img/urAnus.jpg")
img_rocket = pygame.image.load("img/teamRocket.jpg")

#window title
pygame.display.set_caption("FIRST GAME")

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
            #player input
            if events.key == pygame.K_RIGHT:
                #xRocket=xRocket+4
                rocketXVector = 1
            if events.key == pygame.K_LEFT:
                #xRocket=xRocket-4
                rocketXVector=-1
            if events.key == pygame.K_UP:
                rocketYVector=-1
            if events.key == pygame.K_DOWN:
                rocketYVector=1
            
    #rocket movement
    xRocket = xRocket + rocketXVector
    yRocket = yRocket + rocketYVector
    yPlanet=yPlanet+planetSpeed

    if xRocket < -10:
        xRocket = 0
    elif xRocket > displayWidth-widthRocket:
        xRocket = displayWidth-widthRocket
    if yRocket < -10:
        yRocket = 0
    elif yRocket > displayHeight-heightRocket:
        yRocket=displayHeight-heightRocket

    #push to display
    screen.blit(img_rocket, (xRocket,yRocket))
    screen.blit(img_planet, (xPlanet,yPlanet))
    screen.blit(img_planet, (xPlanet+xBetweenPlanets, yPlanet+yBetweenPlanets))

    if yPlanet > displayHeight:
        xPlanet = randint(55, 150)
        yPlanet = 25
        puntos = puntos + 1
        score=font.render(str(puntos)+" puntos", 1, (255, 0, 0))
    pygame.display.update()
    #pygame.display.flip()

pygame.quit()