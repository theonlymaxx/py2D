##Imports and Initializations##
import pygame
pygame.init()

walkRight = [pygame.image.load('Sprites/R1.png'), pygame.image.load('Sprites/R2.png'), pygame.image.load('Sprites/R3.png'),
             pygame.image.load('Sprites/R4.png'), pygame.image.load('Sprites/R5.png'), pygame.image.load('Sprites/R6.png'), pygame.image.load('Sprites/R7.png'),
             pygame.image.load('Sprites/R8.png'), pygame.image.load('Sprites/R9.png')]
walkLeft = [pygame.image.load('Sprites/L1.png'), pygame.image.load('Sprites/L2.png'), pygame.image.load('Sprites/L3.png'), pygame.image.load('Sprites/L4.png'),
            pygame.image.load('Sprites/L5.png'), pygame.image.load('Sprites/L6.png'), pygame.image.load('Sprites/L7.png'), pygame.image.load('Sprites/L8.png'),
            pygame.image.load('Sprites/L9.png')]
bg = pygame.image.load('Sprites/RForeground.jpg')
char = pygame.image.load('Sprites/standing.png')

##Game and Character Variables##
windowWidth = 852
windowHeight = 480
x: int = 0
width: int = 64
height: int = 64
y: int = windowHeight - height
velocity: int = 5
leftKey = pygame.K_a
rightKey = pygame.K_d
upKey = pygame.K_w
downKey = pygame.K_s
jumpKey = pygame.K_SPACE
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
clock = pygame.time.Clock()

##Create Window##
win = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("Test Game")


##Window Settings and Updates##
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount +1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


##Start of Main Loop##
run = True
while run:
    clock.tick(60)
    print(round(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()



##Key Actions##
    if keys[leftKey] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[rightKey] and x < windowWidth-width:
        x += velocity
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

##Jump Code If Needed##
    if not isJump:
        if keys[jumpKey]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()