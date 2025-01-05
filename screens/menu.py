import pygame
from pygame.locals import *
from constants import VERDE, PRETO, LARGURA, ALTURA, tela, fonte_menu

def exibir_menu():
    imagem_fundo = pygame.image.load('assets/144.png')
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
    
    tela.blit(imagem_fundo, (0, 0)) 
    
    
    iniciar = fonte_menu.render('PLAY', True, PRETO)
    sair = fonte_menu.render('EXIT', True, PRETO)

    botao_iniciar = pygame.Rect(LARGURA // 2 - 80, ALTURA // 2 - 5, 150, 40)
    botao_sair = pygame.Rect(LARGURA // 2 - 80, ALTURA // 2 + 70, 150, 40)

    pygame.draw.rect(tela, VERDE, botao_iniciar, border_radius=10)
    pygame.draw.rect(tela, VERDE, botao_sair, border_radius=10)

    
    tela.blit(iniciar, (LARGURA // 2 - iniciar.get_width() // 2, ALTURA // 2 - 4))
    tela.blit(sair, (LARGURA // 2 - sair.get_width() // 2, ALTURA // 2 + 71))

    pygame.display.update()
    return botao_iniciar, botao_sair