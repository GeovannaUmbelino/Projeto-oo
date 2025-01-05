import pygame
from constants import VERDE, PRETO, BRANCO, LARGURA, ALTURA,fonte_menu, fonte_titulo, tela
def exibir_pause():
    tela.fill(PRETO)
    titulo = fonte_titulo.render('Pause', True, BRANCO)
    continuar = fonte_menu.render('Continuar', True, PRETO)
    menu = fonte_menu.render('Menu', True, PRETO)
    sair = fonte_menu.render('Exit', True, PRETO)

    botao_continuar = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 - 50, 200, 50)
    botao_menu = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 + 20, 200, 50)
    botao_sair = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 + 83, 200, 50)

    pygame.draw.rect(tela, VERDE, botao_continuar, border_radius=10)
    pygame.draw.rect(tela, VERDE, botao_menu, border_radius=10)
    pygame.draw.rect(tela, VERDE, botao_sair, border_radius=10)

    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ALTURA // 4))
    tela.blit(continuar, (LARGURA // 2 - continuar.get_width() // 2, ALTURA // 2 - 45))
    tela.blit(menu, (LARGURA // 2 - menu.get_width() // 2, ALTURA // 2 + 23))
    tela.blit(sair, (LARGURA // 2 - sair.get_width() // 2, ALTURA // 2 + 86))

    pygame.display.update()
    return botao_continuar, botao_menu, botao_sair