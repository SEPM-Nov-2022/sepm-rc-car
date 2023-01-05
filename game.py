"""Game"""
import os
import pygame

from car import Car
from audio_effect import AudioEffect

ASSET_DIR = 'assets'
ASSET_CAR = 'car.png'
ASSET_HORN = 'horn.mp3'
WIDTH = 1280
HEIGHT = 720
TICKS = 60
PPU = 32

class Game:
    """models the simulation"""

    def __init__(self):
        """initialisation"""
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("RC Car")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.exit = False
        image_path = self._from_asset_dir(ASSET_CAR) # 173x82
        self.car_image = pygame.transform.scale(pygame.image.load(image_path),(50,25))
        self.car = Car(0, 0, self.play_audio)

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

    def play_audio(self, audio:AudioEffect):
        """play sound"""
        if audio == AudioEffect.HORN:
            pygame.mixer.music.load(self._from_asset_dir(ASSET_HORN))
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play()

    def _draw(self):
        """updates the screen"""
        self.screen.fill((50, 50, 50))
        rotated = pygame.transform.rotate(self.car_image, self.car.angle)
        rect = rotated.get_rect()
        self.screen.blit(rotated, self.car.position * PPU - (rect.width / 2, rect.height / 2))
        pygame.display.flip()

    def _from_asset_dir(self, asset_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(f'{base_dir}/{ASSET_DIR}', asset_name)
