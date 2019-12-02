import pygame
from color.Color import *
from settings.Settings import *
# ^ importing all the needed files ^


# the class that makes the player exist and move
class Player:
    def __init__(self, screen, vector, width, height):
        self.__screen = screen
        self.__vector = vector
        self.__width = width
        self.__height = height
        self.alive = True

    # updates the position of the player
    def update(self):

        if self.alive:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.__vector.x -= player_speed
                if self.__vector.x < 0:
                    self.__vector.x = 0

            if keys[pygame.K_d]:
                self.__vector.x += player_speed
                if self.__vector.x > screen_width - self.__width:
                    self.__vector.x = (screen_width - self.__width)

            if keys[pygame.K_w]:
                self.__vector.y -= player_speed
                if self.__vector.y < 0:
                    self.__vector.y = 0

            if keys[pygame.K_s]:
                self.__vector.y += player_speed
                if self.__vector.y > screen_height - self.__height:
                    self.__vector.y = (screen_height - self.__height)

    def draw(self):

        if self.alive:
            pygame.draw.rect(
                self.__screen,
                black,
                pygame.Rect(
                    (self.__vector.x, self.__vector.y, self.__width, self.__height)
                )
            )

    def get_player_center(self):
        return self.__vector

    def get_vector(self):
        return self.__vector

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
