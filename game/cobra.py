import pygame
from constants import VERDE, LARGURA, ALTURA, VELOCIDADE

class Cobra:
    def __init__(self):
        self.lista = []
        self.comprimento = 5
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.velocidade_x = VELOCIDADE
        self.velocidade_y = 0
        self.morreu = False

    def mover(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

        if self.x < 0:
            self.x = LARGURA
        elif self.x >= LARGURA:
            self.x = 0
        if self.y < 0:
            self.y = ALTURA
        elif self.y >= ALTURA:
            self.y = 0

        cabeca = [self.x, self.y]
        self.lista.append(cabeca)
        if len(self.lista) > self.comprimento:
            del self.lista[0]

    def desenhar(self, tela):
        for segmento in self.lista:
            pygame.draw.rect(tela, VERDE, (segmento[0], segmento[1], 20, 20))

    def verificar_colisao(self):
        if self.lista[-1] in self.lista[:-1]:
            self.morreu = True