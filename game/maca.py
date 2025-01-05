import pygame
from random import randint
from constants import VERMELHO, LARGURA, ALTURA

class Maca:
    def __init__(self):
        self.nova_posicao()

    def nova_posicao(self):
        self.x = randint(40, LARGURA - 40)
        self.y = randint(50, ALTURA - 50)

    def desenhar(self, tela):
        pygame.draw.rect(tela, VERMELHO, (self.x, self.y, 20, 20))