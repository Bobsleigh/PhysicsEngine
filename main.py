from Box2D import *
from Settings import *
from RectangleBox import *
import pygame_sdl2 as pygame

world = b2World(gravity=(0,-10), doSleep=True)

groundBoxSprite = RectangleBox(pygame.Rect(0, SCREEN_HEIGHT, SCREEN_WIDTH, 20), world, True)
boxSprite = RectangleBox(pygame.Rect(SCREEN_WIDTH/2, 10, 20, 20), world, False)
box2 = RectangleBox(pygame.Rect(SCREEN_WIDTH/2+10, groundBoxSprite.rect.y-5, 20, 20), world, False)

# Prepare for simulation. Typically we use a time step of 1/60 of a
# second (60Hz) and 6 velocity/2 position iterations. This provides a
# high quality simulation in most game scenarios.
timeStep = 1.0 / 60
vel_iters, pos_iters = 6, 2

# Init Pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.font.init()

# Screen
screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("PyBox2D demo")

spriteGroup = pygame.sprite.Group()
spriteGroup.add(groundBoxSprite)
spriteGroup.add(boxSprite, box2)

clock = pygame.time.Clock()

# This is our little game loop.
while(True):
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    world.Step(timeStep, vel_iters, pos_iters)

    # Clear applied body forces. We didn't apply any forces, but you should
    # know about this function.
    world.ClearForces()

    # Now print the position and angle of the body.
    # print(body.position, body.angle)

    spriteGroup.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            spriteGroup.add(RectangleBox(pygame.Rect(event.pos[0], event.pos[1], 20, 20), world, False))

    screen.fill((255,255,255))
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()
    clock.tick(60)


