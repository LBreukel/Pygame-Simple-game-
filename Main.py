import pygame
from color.Color import *
from player.Player import Player
from enemy.Enemy import Enemy
from vector.Vector import Vector
from settings.Settings import screen_height, screen_width


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([screen_width, screen_height])
        self.__clock = pygame.time.Clock()
        self.__player = Player(self.__screen, Vector(screen_width / 2 - 25, screen_height / 2 - 25), 50, 50)
        self.__enemies = [Enemy(self.__screen, Vector(0, 0), self.__player.get_player_center()),
                          Enemy(self.__screen, Vector(screen_width - 50, screen_height - 50), self.__player.get_player_center())
                          ]

    @staticmethod
    def __quit_program():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def __check_collision(self):
        for enemy in self.__enemies:
            if enemy.alive:
                self.__collision_detection(self.__player, enemy)
                for e in self.__enemies:
                    if e.alive and (e is not enemy):
                        self.__collision_detection(e, enemy)

    @staticmethod
    def __collision_detection(rect1, rect2):
        rect1_top = rect1.get_vector()
        rect1_bottom = Vector(rect1.get_vector().x + rect1.get_width(), rect1.get_vector().y + rect1.get_height())

        rect2_top = rect2.get_vector()
        rect2_bottom = Vector(rect2.get_vector().x + rect2.get_width(), rect2.get_vector().y + rect2.get_height())

        if ((rect1_bottom.x >= rect2_top.x >= rect1_top.x) or (rect1_bottom.x >= rect2_bottom.x >= rect1_top.x)) \
                and (
                (rect1_bottom.y >= rect2_top.y >= rect1_top.y) or (rect1_bottom.y >= rect2_bottom.y >= rect1_top.y)
        ):
            rect1.alive = False
            rect2.alive = False

    def check_enemy_lives(self):
        alive = True
        for enemy in self.__enemies:
            if enemy.alive:
                alive = False
        return alive

    def update(self):
        self.__player.update()
        for enemy in self.__enemies:
            enemy.update()
        self.__check_collision()

    def draw(self):
        self.__player.draw()
        for enemy in self.__enemies:
            enemy.draw()

    def run(self):
        run_game = True
        font = pygame.font.Font('freesansbold.ttf', 32)

        while run_game:
            self.__screen.fill(white)
            if not self.__player.alive:
                self.__screen.fill(black)
                text = font.render('Game Over', True, white)
                text_rect = text.get_rect()
                text_rect.center = (screen_width // 2, screen_height // 2)
                self.__screen.blit(text, text_rect)
            elif self.check_enemy_lives():
                self.__screen.fill(green)
                text = font.render('You win!!', True, white)
                text_rect = text.get_rect()
                text_rect.center = (screen_width // 2, screen_height // 2)
                self.__screen.blit(text, text_rect)
            else:
                self.update()
                self.draw()

            run_game = self.__quit_program()

            pygame.display.update()
            self.__clock.tick(90)
        quit()


game = Game()
game.run()
