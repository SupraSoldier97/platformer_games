import pygame, sys, pymunk, os
from pygame.locals import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
#Initialize Game
pygame.init()

#Settings
FPS = 120
fpsClock = pygame.time.Clock()
pygame.mixer.music.load('theme.ogg')
pygame.mixer.music.play(-1, 0.0)


#Display
displaysurf = pygame.display.set_mode((640, 480), 0, 8)
pygame.display.set_caption('Ziffie: The Moon Hero')

#Colors
white = (255, 255, 255)
green = (0 , 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

#Images
background = pygame.image.load('background.png').convert()
hero_img = pygame.image.load('roto_2.png').convert()
walking_img = pygame.image.load('walking.png').convert()
walking_left_img = pygame.image.load('walking2.png').convert()
jumping_img = pygame.image.load('jumping.png').convert()
ledge = pygame.image.load('ledge.png').convert()
center = (0, 0)


#Player
rotox = 65
rotoy = 303
jump_1 = pygame.mixer.Sound("jump_1.wav")




#Main Game Loop
while True:

    displaysurf.fill(black)
    displaysurf.blit(background, center)
    
    pygame.display.flip()

    displaysurf.blit(hero_img, (rotox, rotoy))
    displaysurf.set_colorkey(black)




    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()

#User Input          
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rotox -= 4
        displaysurf.blit(walking_left_img, (rotox, rotoy))
    if keys[pygame.K_RIGHT]:
        rotox += 4
        displaysurf.blit(walking_img, (rotox, rotoy))
    displaysurf.set_colorkey(black)
    if keys[pygame.K_DOWN]:
        rotoy += 4
    if keys[pygame.K_UP]:
        rotoy -= 4
        displaysurf.blit(jumping_img, (rotox, rotoy))
    if keys[pygame.K_SPACE]:
        rotoy -= 10
        jump_1.play()
        displaysurf.blit(jumping_img, (rotox, rotoy))
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        rotox -= 4
        rotoy += 4
    elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        rotox += 4
        rotoy += 4
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        rotoy -= 4
        rotox += 4
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        rotoy -= 4
        rotox -= 4
    elif keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
        rotoy -= 10
        rotox += 4
        jump_1.play()
    elif keys[pygame.K_SPACE] and keys[pygame.K_LEFT]:
        rotoy -= 10
        rotox -= 4
        jump_1.play()
    
        


    pygame.display.update()
    

    

    fpsClock.tick(FPS)
