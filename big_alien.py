import alien
from alien import Alien
import pygame
from pygame.sprite import Sprite
class BigAlien(Alien, Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/big_alien.bmp')

    def check_edges(self):
        super().check_edges()

    def update(self):
        super().update()

    def blitme(self):
        super().blitme()