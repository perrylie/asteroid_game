import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (self.position))

    def update_score(self):
        self.score += 1

    def get_score(self):
        return self.score
