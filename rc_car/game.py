"""This file includes the key functionalities of the race car game."""

import os
from typing import Tuple

import pygame
from pygame.math import Vector2

from .button import Button
from .audio_effect import AudioEffect
from .car import Car
from .constants import (ASSET_BACKGROUND, ASSET_BATTERY, ASSET_CAR, ASSET_DIR,
                        ASSET_DRIVER, BATTERY_HEIGHT, BATTERY_WIDTH, BATTERY_X,
                        BATTERY_Y, CAR_GAME_CAPTION, DRIVER_SIZE, DRIVER_X,
                        DRIVER_Y, HEIGHT, MAP_MAX_X, MAP_MAX_Y, MAP_MIN_X,
                        MAP_MIN_Y, PPU, TICKS, WIDTH)
from .logger import generate_logger
from .remote import Remote

log = generate_logger(name='Race car game')


class Game:
    """models the simulation"""

    def __init__(self):
        """initialisation"""
        pygame.init()
        pygame.mixer.set_num_channels(2)
        pygame.mixer.init()
        pygame.display.set_caption(CAR_GAME_CAPTION)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.exit = False

        self.driver_image = self._load_image(
            ASSET_DRIVER, (DRIVER_SIZE, DRIVER_SIZE))
        self.battery_bar = pygame.Surface((BATTERY_WIDTH, BATTERY_HEIGHT))
        self.car = Car(Vector2(23, 19), self.play_audio, self.check_walls)
        self.remote = Remote(self.notify)
        self.remote.connect_to(self.car)

        # load button images
        self.user_1 = self._load_image('user_1.png', (50, 50)).convert_alpha()
        self.user_2 = self._load_image('user_2.png', (50, 50)).convert_alpha()
        self.user_3 = self._load_image('user_3.png', (50, 50)).convert_alpha()
        self.user_4 = self._load_image('user_4.png', (50, 50)).convert_alpha()

        # create button instances
        self.resume_button = Button(304, 125, self.user_1, 1)
        self.options_button = Button(297, 250, self.user_2, 1)
        self.quit_button = Button(336, 375, self.user_3, 1)
        self.video_button = Button(226, 75, self.user_4, 1)

        # game variables
        self.game_paused = False

        # define fonts
        self.font = pygame.font.SysFont("arialblack", 40)

        # define colours
        self.TEXT_COL = (255, 255, 255)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def run(self):
        """main loop"""
        can_drive = True
        while not self.exit:
            # check if game is paused
            if self.game_paused:
                # draw pause screen buttons
                if self.resume_button.draw(self.screen):
                    self.game_paused = False
                if self.options_button.draw(self.screen):
                    self.game_paused = False
                if self.quit_button.draw(self.screen):
                    self.exit = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.game_paused = True
                if event.type == pygame.QUIT:
                    self.exit = True
            if can_drive:
                can_drive = self.remote.command(
                    pygame.key.get_pressed(), self.clock.get_time() / 1000)
            self._draw()
            self.clock.tick(TICKS)

        pygame.quit()

    def play_audio(self, audio: AudioEffect):
        """play sound"""
        sound = pygame.mixer.Sound(self._from_asset_dir(audio.value.path))
        pygame.mixer.Channel(audio.value.channel).play(sound)
        log.info('Playing sound %s', audio.value.path)

    def notify(self, message: str):
        """prints a notification. To add some text in the screen"""
        log.info(message)

    def check_walls(self, next_position):
        """check if the position is allowed"""
        return MAP_MIN_X <= next_position.x <= MAP_MAX_X \
            and MAP_MIN_Y <= next_position.y <= MAP_MAX_Y

    def _draw(self):
        """updates the screen"""
        self._draw_background()
        self._draw_car()
        self._draw_driver()
        self._draw_battery()
        self._draw_buttons()
        pygame.display.flip()

    def _draw_buttons(self):
        self.screen.blit(self.user_1, (9,9))

    def _draw_background(self):
        """Insert map as background"""
        background = self._load_image(ASSET_BACKGROUND, (1280, 720))
        log.debug('Inserted the map as background')
        self.screen.blit(background, (0, 0))

    def _draw_car(self):
        car_image = self._load_image(ASSET_CAR, (50, 25))
        car_led = pygame.Surface(car_image.get_size()).convert_alpha()
        car_led.fill(self.car.color)
        car_image.blit(car_led, (0, 0), special_flags=pygame.BLEND_MULT)
        rotated = pygame.transform.rotate(car_image, self.car.angle)
        rect = rotated.get_rect()
        self.screen.blit(rotated, self.car.position * PPU -
                         (rect.width / 2, rect.height / 2))

    def _draw_driver(self):
        # driver's image
        self.screen.blit(self.driver_image, Vector2(DRIVER_X, DRIVER_Y))

    def _draw_battery(self):
        """draw the battery bar and icon"""
        level = self.car.get_battery_level()
        (battery_rect_bg, battery_image_bg) = self._create_battery_bar_bg()
        (battery_rect, battery_image) = self._create_battery_bar(level)
        self.screen.blit(battery_image_bg, battery_rect_bg,
                         (0, 0, battery_rect_bg.w, battery_rect_bg.h))
        self.screen.blit(battery_image, battery_rect,
                         (0, 0, battery_rect.w / 100 * level, battery_rect.h))
        # icon
        image_path = self._from_asset_dir(ASSET_BATTERY)
        battery_image = pygame.transform.scale(
            pygame.image.load(image_path), (16, 12))
        self.screen.blit(battery_image, Vector2(BATTERY_X - 25, BATTERY_Y + 5))

    def _create_battery_bar_bg(self):
        """creates the battery bar"""
        battery_image = pygame.Surface((BATTERY_WIDTH + 2, BATTERY_HEIGHT + 2))
        black = pygame.Color(0, 0, 0)
        for image_x in range(battery_image.get_width()):
            for image_y in range(battery_image.get_height()):
                battery_image.set_at((image_x, image_y), black)
        self.battery_bar = pygame.Surface(
            (BATTERY_WIDTH + 2, BATTERY_HEIGHT + 2))
        battery_rect = self.battery_bar.get_rect(
            topleft=(BATTERY_X - 1, BATTERY_Y - 1))
        return battery_rect, battery_image

    def _create_battery_bar(self, level: float):
        """creates the battery bar"""
        battery_image = pygame.Surface((BATTERY_WIDTH, BATTERY_HEIGHT))
        color = pygame.Color(0, 0xff, 0) if level > 30 \
            else pygame.Color(0xff, 0xff, 0) if level > 10 \
            else pygame.Color(0xff, 0, 0)
        for image_x in range(battery_image.get_width()):
            for image_y in range(battery_image.get_height()):
                battery_image.set_at((image_x, image_y), color)
        battery_rect = self.battery_bar.get_rect(
            topleft=(BATTERY_X, BATTERY_Y))
        return battery_rect, battery_image

    def _load_image(self, asset: str, size: Tuple[int, int]):
        image_path = self._from_asset_dir(asset)
        return pygame.transform.scale(pygame.image.load(image_path), size)

    def _from_asset_dir(self, asset_name: str):
        base_dir = os.path.dirname(
            os.path.abspath(__file__))
        return os.path.join(f'{base_dir}/{ASSET_DIR}', asset_name)
