"""This file includes the functionalities of a menu item"""
import pygame


# Menu Item Class
class MenuItem:
    """Serves are a container for menu items,
    i.e. for switching between user's profile pictures"""
    def __init__(self, pos_x:int, pos_y:int,
                 image:pygame.Surface, filename:str):
        width = image.get_width()
        height = image.get_height()
        scale = 1
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.clicked = False
        self._filename = filename

    def draw(self, surface):
        """Creates menu items, i.e. user's pictures"""
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def is_selected(self):
        """Detects mouse selection"""
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    @property
    def filename(self):
        """returns the icon's filename"""
        return self._filename
