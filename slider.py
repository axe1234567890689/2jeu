import pygame


class Slider:
    def __init__(self, pos, size, colora, colorb, colorc, min, max, slider_size_bonus, nb):
        self.pos = pos
        self.size = size
        self.colora = colora
        self.colorb = colorb
        self.colorc = colorc
        self.min = min
        self.max = max
        self.nb = nb
        self.value = max
        self.prop = 1
        self.slider_size_bonus = slider_size_bonus
        self.rayon1 = size[1] / 2
        self.pos_rect = [pos[0] + self.rayon1, pos[1], size[0] - size[1], size[1]]

    def draw(self, screen):
        pygame.draw.rect(screen, self.colora, [self.pos_rect[0], self.pos[1], (self.size[0] - self.size[1]) * self.prop, self.size[1]])
        pygame.draw.rect(screen, self.colorb, [self.pos_rect[0] + (self.size[0] - self.size[1]) * self.prop, self.pos[1], (self.size[0] - self.size[1]) * (-self.prop + 1), self.size[1]])
        pygame.draw.circle(screen, self.colora, [self.pos_rect[0], self.pos[1] + self.rayon1], self.rayon1)
        pygame.draw.circle(screen, self.colorb, [self.pos_rect[2] + self.pos_rect[0], self.pos[1] + self.rayon1], self.rayon1)
        pygame.draw.circle(screen, self.colorc, [self.pos_rect[0] + (self.size[0] - self.size[1]) * self.prop, self.pos[1] + self.rayon1], self.rayon1 + self.slider_size_bonus)

    def click(self, pos):
        touche = False
        if self.pos[0] < pos[0] < self.pos[0] + self.size[0] and self.pos[1] < pos[1] < self.pos[1] + self.size[1]:
            touche = True
        return touche

    def calcule(self, x):
        x -= self.pos[0]
        if x < 0:
            self.prop = 0
        elif x > self.size[0]:
            self.prop = 1
        else:
            self.prop = x / self.size[0]
        self.value = (self.max - self.min) * self.prop + self.min

    def set_value(self, value):
        self.value = value
        self.prop = self.value / (self.max - self.min)

    def set_prop(self, prop):
        self.prop = prop
        self.value = (self.max - self.min) * self.prop + self.min
