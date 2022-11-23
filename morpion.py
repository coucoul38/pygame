import pygame
import pygame.time
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
displayHeight = 600
displayWidth = 600
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))

#GRID
img_grid = pygame.image.load("img/grid.png")

rect00 = pygame.Rect(0,0, 200, 200) #x, y, width, height
rect01 = pygame.Rect(200,0, 200, 200) 
rect02 = pygame.Rect(400,0, 200, 200) 

rect10 = pygame.Rect(0,200, 200, 200) #x, y, width, height
rect11 = pygame.Rect(200,200, 200, 200) 
rect12 = pygame.Rect(400,200, 200, 200) 

rect20 = pygame.Rect(0,400, 200, 200) #x, y, width, height
rect21 = pygame.Rect(200,400, 200, 200) 
rect22 = pygame.Rect(400,400, 200, 200) 

pygame.display.set_caption("The Battle Cats")

def isOverRect(rect, pos):
    # function takes a tuple of (x, y) coords and a pygame.Rect object
    # returns True if the given rect overlaps the given coords
    # else it returns False
    return True if rect.collidepoint(pos[0], pos[1]) else False



tabA=[]
def createGrid():
    global tabA
    #on crée x colonnes
    for i in range(3):
        #on crée une ligne de longueur x
        tabB=[]
        for o in range(3):
            #on met un nombre aléatoire dans chaque case de la ligne (0=morte, 1=vivante)
            tabB.append(0)
        #on insère la ligne dans le tableau, créant une colonne
        tabA.append(tabB)

#Run until the player quits
createGrid()
running = True
bot = False
while running:
    # run the game at a constant 60fps
    clock.tick(60)
    for playerNum in range(1,3):
        #Did the user clicked the close button ?
        if bot == True and playerNum ==2:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running=False
                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        running=False
                if events.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos
                    if isOverRect(rect00, mousePos):
                        tabA[0][0]=playerNum
                #display grid
        
    screen.fill(backgroundColor)
    screen.blit(img_grid, (0,0))
    pygame.display.update()
pygame.quit()