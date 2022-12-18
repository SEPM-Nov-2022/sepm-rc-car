"""Game"""
import os
import pygame

from car import Car

ASSET_DIR = 'assets'
ASSET_CAR = 'car.png'
WIDTH = 1280
HEIGHT = 720
TICKS = 60
PPU = 32

class Game:
    """models the simulation"""

    def __init__(self):
        """initialisation"""
        pygame.init()
        pygame.display.set_caption("RC Car")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.exit = False
        car_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(f'{car_dir}/{ASSET_DIR}', ASSET_CAR) # 173x82
        self.car_image = pygame.transform.scale(pygame.image.load(image_path),(50,25))
        self.car = Car(0, 0)

    def run(self):
        """main loop"""
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            self.car.command(pygame.key.get_pressed(), self.clock.get_time()/1000)
            self._draw()
            self.clock.tick(TICKS)

        pygame.quit()

    def _draw(self):
        """updates the screen"""
        self.screen.fill((50, 50, 50))
        rotated = pygame.transform.rotate(self.car_image, self.car.angle)
        rect = rotated.get_rect()
        self.screen.blit(rotated, self.car.position * PPU - (rect.width / 2, rect.height / 2))
        pygame.display.flip()
