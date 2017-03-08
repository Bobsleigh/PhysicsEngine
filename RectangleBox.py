import pygame_sdl2 as pygame
from Box2D import *
from Settings import *
from math import pi, degrees

class RectangleBox(pygame.sprite.Sprite):
    def __init__(self, rect, world, static):
        super().__init__()

        self.rect = rect
        self.baseImage = pygame.Surface((rect.width, rect.height))
        self.image = pygame.Surface((rect.width, rect.height))

        pygame.draw.rect(self.baseImage, (50,50,255), (0,0, rect.width, rect.height))

        self.world = world

        # Define the ground body.
        if (static):
            bodyDef = b2BodyDef(type=b2_staticBody)
        else:
            bodyDef = b2BodyDef(type=b2_dynamicBody)

        bodyDef.position = ((rect.x + rect.width/2)/PIXEL_RATIO, -(rect.y + rect.height/2)/PIXEL_RATIO)

        # Make a body fitting this definition in the world.
        body = world.CreateBody(bodyDef)

        box = b2PolygonShape(box=((rect.width/2) / PIXEL_RATIO, (rect.height/2) / PIXEL_RATIO))

        # And create a fixture definition to hold the shape
        if (static):
            boxFixture = b2FixtureDef(shape=box)
        else:
            boxFixture = b2FixtureDef(shape=box,density=1, friction=0.3, restitution=0.6)

        # Add the ground shape to the ground body.
        body.CreateFixture(boxFixture)

        self.body = body
        self.angle = body.angle

    def update(self):

        self.rect.center = (PIXEL_RATIO * self.body.position[0], -PIXEL_RATIO * self.body.position[1])
        self.rotate(self.body.angle)

    def rotate(self,angle):
        """rotate an image while keeping its center"""
        self.image = pygame.transform.rotozoom(self.baseImage, degrees(angle), 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle = degrees(angle)
        self.image.set_colorkey((0, 0, 0))