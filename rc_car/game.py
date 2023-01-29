"""This file includes the key functionalities of the race car game."""

import os
from typing import Tuple

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.math import Vector2

from .audio_effect import AudioEffect
from .car import Car
from .constants import (ASSET_BACKGROUND, ASSET_BATTERY, ASSET_CAR, ASSET_DIR,
                        ASSET_DRIVER, BATTERY_HEIGHT, BATTERY_WIDTH, BATTERY_X,
                        BATTERY_Y, CAR_GAME_CAPTION, DRIVER_SIZE, DRIVER_X,
                        DRIVER_Y, HEIGHT, MAP_MAX_X, MAP_MAX_Y, MAP_MIN_X,
                        MAP_MIN_Y, MENU_BACKGROUND_COLOUR, MENU_BG_LEFT,
                        MENU_BG_TOP, MENU_FONT, MENU_FONT_SIZE, MENU_HEADLINE,
                        MENU_HEIGHT, MENU_ITEM_IMAGE_SIZE, MENU_WIDTH, MENU_X,
                        MENU_Y, PPU, TICKS, USER_1, USER_2, USER_3, USER_4,
                        WIDTH)
from .logger import generate_logger
from .menu_item import MenuItem
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

        self.driver_image = self._load_image(
            ASSET_DRIVER, (DRIVER_SIZE, DRIVER_SIZE))
        self.battery_bar = pygame.Surface((BATTERY_WIDTH, BATTERY_HEIGHT))
        self.car = Car(Vector2(23, 19), self.play_audio, self.check_walls)
        self.remote = Remote(self.notify)
        self.remote.connect_to(self.car)

        # Load menu images (user profile pics)
        self.driver_buttons = []
        for i, icon_filename in enumerate([USER_1, USER_2, USER_3, USER_4]):
            button = self._load_image(icon_filename, (MENU_ITEM_IMAGE_SIZE,
                                      MENU_ITEM_IMAGE_SIZE)).convert_alpha()
            self.driver_buttons.append(
                MenuItem(615, 150 + i * 100, button, icon_filename))

    def run(self):
        """main loop"""
        can_drive = True
        exit_game = False
        game_paused = False
        clock = pygame.time.Clock()
        while not exit_game:
            if can_drive and not game_paused:
                can_drive = self.remote.command(
                    pygame.key.get_pressed(), clock.get_time() / 1000)
            self._draw(game_paused)
            clock.tick(TICKS)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        game_paused = not game_paused
                if event.type == pygame.QUIT:
                    exit_game = True

            if game_paused:
                for driver_button in self.driver_buttons:
                    if driver_button.is_selected():
                        self.driver_image = self._load_image(
                            driver_button.filename, (DRIVER_SIZE, DRIVER_SIZE))
                        game_paused = False

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

    def _draw(self, game_paused):
        """updates the screen"""
        self._draw_background()
        self._draw_car()
        self._draw_driver()
        self._draw_battery()
        if game_paused:
            self._draw_menu()
        pygame.display.flip()

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

    def _draw_menu(self) -> None:
        # Add menu background
        pygame.draw.rect(self.screen, MENU_BACKGROUND_COLOUR,
                         pygame.Rect(MENU_BG_LEFT, MENU_BG_TOP,
                                     MENU_WIDTH, MENU_HEIGHT))
        # Draw menu headline
        font = pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE)
        self._draw_text(MENU_HEADLINE, font, MENU_X, MENU_Y)
        # Draw user profile pictures
        for driver_button in self.driver_buttons:
            driver_button.draw(self.screen)

    def _draw_text(self, text: str, font: Font,
                   x_pos: int, y_pos: int) -> None:
        img = font.render(text, True,  (0, 0, 0))
        self.screen.blit(img, (x_pos, y_pos))

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

    def _load_image(self, asset: str, size: Tuple[int, int]) -> Surface:
        image_path = self._from_asset_dir(asset)
        return pygame.transform.scale(pygame.image.load(image_path), size)

    def _from_asset_dir(self, asset_name: str):
        base_dir = os.path.dirname(
            os.path.abspath(__file__))
        return os.path.join(f'{base_dir}/{ASSET_DIR}', asset_name)
