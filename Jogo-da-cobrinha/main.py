import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_a, K_d, K_w, K_s, K_LEFT, K_DOWN, K_RIGHT, K_UP
from sys import exit
from pygame.locals import *
from random import randint
from constants import LARGURA, ALTURA, PRETO, BRANCO, VELOCIDADE, tela, relogio, fonte_menu
from game.cobra import Cobra
from game.maca import Maca
from screens.menu import exibir_menu
from screens.pause import exibir_pause
from screens.game_over import reiniciar_jogo
from screens.game_over import exibir_game_over


pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Cobrinha')

def main():
    cobra, maca, pontos = reiniciar_jogo()
    estado = 'menu'

    while True:
        if estado == 'menu':
            botao_iniciar, botao_sair = exibir_menu()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if botao_iniciar.collidepoint(event.pos):
                        cobra, maca, pontos = reiniciar_jogo() 
                        estado = 'jogando'
                    if botao_sair.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        elif estado == 'pause':
            botao_continuar, botao_menu, botao_sair = exibir_pause()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if botao_continuar.collidepoint(event.pos):
                        estado = 'jogando'
                    if botao_menu.collidepoint(event.pos):
                        estado = 'menu'
                    if botao_sair.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        elif estado == 'jogando':
            relogio.tick(30)
            tela.fill(PRETO)

            try:
                imagem_pausa = pygame.image.load('assets/icons8-pausa-circular-50.png')
                imagem_pausa = pygame.transform.scale(imagem_pausa, (35, 35))  
            except pygame.error:
                print("Imagem de pausa não encontrada.")

            tela.blit(imagem_pausa, (LARGURA -60, 10))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if pygame.Rect(LARGURA - 120, 10, 100, 40).collidepoint(event.pos):
                        estado = 'pause'
                if event.type == KEYDOWN:
                    if (event.key == K_a or event.key == K_LEFT) and cobra.velocidade_x == 0:
                        cobra.velocidade_x = -VELOCIDADE
                        cobra.velocidade_y = 0
                    if (event.key == K_d or event.key == K_RIGHT) and cobra.velocidade_x == 0:
                        cobra.velocidade_x = VELOCIDADE
                        cobra.velocidade_y = 0
                    if (event.key == K_w or event.key == K_UP) and cobra.velocidade_y == 0:
                        cobra.velocidade_y = -VELOCIDADE
                        cobra.velocidade_x = 0
                    if (event.key == K_s or event.key == K_DOWN) and cobra.velocidade_y == 0:
                        cobra.velocidade_y = VELOCIDADE
                        cobra.velocidade_x = 0

            cobra.mover()
            cobra.verificar_colisao()

            if cobra.morreu:
                estado = 'game_over'

            if pygame.Rect(cobra.x, cobra.y, 20, 20).colliderect(pygame.Rect(maca.x, maca.y, 20, 20)):
                maca.nova_posicao()
                cobra.comprimento += 1
                pontos += 1

            maca.desenhar(tela)
            cobra.desenhar(tela)

            texto_pontos = fonte_menu.render(f'Pontos: {pontos}', True, BRANCO)
            tela.blit(texto_pontos, (10, 10))

            pygame.display.update()

        elif estado == 'game_over':
            botao_reiniciar, botao_menu = exibir_game_over(pontos)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if botao_reiniciar.collidepoint(event.pos):
                        cobra, maca, pontos = reiniciar_jogo()
                        estado = 'jogando'
                    if botao_menu.collidepoint(event.pos):
                        estado = 'menu'

if __name__ == "__main__":
    main()