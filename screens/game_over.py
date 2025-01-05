import pygame
from game.maca import Maca
from game.cobra import Cobra
from constants import VERDE, PRETO, BRANCO, VERMELHO, LARGURA, ALTURA, fonte_menu, fonte_titulo, tela


def exibir_game_over(pontos):
    tela.fill(PRETO)
    game_over = fonte_titulo.render('Game Over', True, VERMELHO)
    texto_pontos = fonte_menu.render(f'Pontos: {pontos}', True, BRANCO)
    reiniciar = fonte_menu.render('Reiniciar', True, PRETO)
    menu = fonte_menu.render('Menu', True, PRETO)

    botao_reiniciar = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 - 30, 200, 50)
    botao_menu = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 + 40, 200, 50)

    pygame.draw.rect(tela, VERDE, botao_reiniciar, border_radius=10)
    pygame.draw.rect(tela, VERDE, botao_menu, border_radius=10)

    tela.blit(game_over, (LARGURA // 2 - game_over.get_width() // 2, ALTURA // 4))
    tela.blit(texto_pontos, (LARGURA // 2 - texto_pontos.get_width() // 2, ALTURA // 2 - 75))
    tela.blit(reiniciar, (LARGURA // 2 - reiniciar.get_width() // 2, ALTURA // 2 - 23))
    tela.blit(menu, (LARGURA // 2 - menu.get_width() // 2, ALTURA // 2 + 43))

    pygame.display.update()
    return botao_reiniciar, botao_menu

# Função para reiniciar o jogo
def reiniciar_jogo():
    return Cobra(), Maca(), 0