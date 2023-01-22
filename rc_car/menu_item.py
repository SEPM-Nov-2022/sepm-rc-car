"""This file includes the functionalities of a menu item"""
import pygame


# Menu Item Class
class MenuItem:
    """Serves are a container for menu items,
    i.e. for switching between user's profile pictures"""
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        """Creates menu items, i.e. user's pictures"""
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

        # Draw menu item on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
