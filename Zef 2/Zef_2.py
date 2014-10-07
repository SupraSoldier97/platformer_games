import pygame, sys, pymunk
from pygame.locals import *

#Initialize Game
pygame.init()

#Settings
FPS = 120
fpsClock = pygame.time.Clock()
pygame.mixer.music.load('theme.ogg')
pygame.mixer.music.play(-1, 0.0)


#Display
displaysurf = pygame.display.set_mode((600, 400), 0, 32)
displaysurf_2 = pygame.display.set_mode((640, 480), 0, 8)
pygame.display.set_caption('Zef 2: The Lost Ones')

#Colors
white = (255, 255, 255)
green = (0 , 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

#Images
background = pygame.image.load('background.png').convert()
hero_img = pygame.image.load('roto.png').convert()
walking_img = pygame.image.load('walking.png').convert()

#Player
rotox = 65
rotoy = 303
jump_1 = pygame.mixer.Sound("jump_1.wav")


#Main Game Loop
while True:

    displaysurf_2.fill((0, 0, 0))
    displaysurf_2.blit(background, (0, 0))
    pygame.display.flip()

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]


    displaysurf.blit(hero_img, (rotox, rotoy))
    displaysurf.set_colorkey(black)

    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()

    space = pymunk.Space()
    space.gravity = 0, -1000

    body = pymunk.Body(100, 1667)
    body.position = 50, 100

    poly = pymunk.Poly.create_box(body)
    space.add(body, poly)
#User Input          
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rotox -= 2
    if keys[pygame.K_RIGHT]:
        rotox += 2
    if keys[pygame.K_DOWN]:
        rotoy += 2
    if keys[pygame.K_UP]:
        rotoy -= 2
    if keys[pygame.K_SPACE]:
        rotoy -= 10
        jump_1.play()
    
        


    pygame.display.update()
    

    

    fpsClock.tick(FPS)



