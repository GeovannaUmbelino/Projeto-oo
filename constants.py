import pygame

LARGURA = 700
ALTURA = 500
VELOCIDADE = 10

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
AZUL = (0, 100, 255)
CINZA = (200, 200, 200)

tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

pygame.font.init()
fonte = pygame.font.SysFont('Arial', 30, True, True) 
fonte_menu = pygame.font.SysFont('comicsansms', 26, True, True)
fonte_titulo = pygame.font.SysFont('PressStart2P-Regular.ttf', 80)
relogio = pygame.time.Clock()

    