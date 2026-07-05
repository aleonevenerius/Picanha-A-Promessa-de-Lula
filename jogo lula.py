#importando a biblioteca pygame
import pygame
#importando submodulo que contem as constantes e funções que será usado
from pygame.locals import *
#importando a função, que fecha a janela
from sys import exit
#importandoa random
import random

#iniciando todas as funções e variaveis do pygame
pygame.init()

#criando e definindo a largura
largura = 1040
altura = 512
tela = pygame.display.set_mode((largura, altura))

#imagem de fundo
fundo = pygame.image.load(r'C:\Users\alexa\OneDrive\Documents\Alex\jogo lula\sprites\cenario principal completo.png')

#imagem do lula
sprite_lula = pygame.image.load(r'C:\Users\alexa\OneDrive\Documents\Alex\jogo lula\sprites\lula personage.png')

#mudando o tamanho da imagem
largura_nova = 32*7
altura_nova = 32*7
sprite_lula_redimencionada = pygame.transform.scale(sprite_lula, (largura_nova, altura_nova))

#posicão do jogador(lula)
x = 136
y = 136

#defindindo a altura e largura do retangulo
largura_lula = sprite_lula.get_width()
altura_lula = sprite_lula.get_height()

#para o frame do jogo
relogio = pygame.time.Clock()

#colocando um nome na janela
pygame.display.set_caption('Picanha: A Promessa de Lula')

# Define as posições iniciais das imagens
posicao1 = (100, 100)
posicao2 = (400, 300)

#criando o loop infinito e principal do jogo
while True:
    #controlando os frames do jogo
    relogio.tick(45)
    #limpando a tela e deixando de fundo preto
    tela.fill((0, 0, 0))
    #loop que se algum evento ocorreu
    for event in pygame.event.get():
    
        #condição para fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
             
    #movendo para a esquerda
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
         
    #movendo para a direita
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
            
    #movendo para cima
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
         
    #movendo para baixo
    if pygame.key.get_pressed()[K_s]:
        y = y + 20 
    
    #exibindo o cenario principal
    tela.blit(fundo, (0, 0))
    #exibindo o lula redimencionado
    tela.blit(sprite_lula_redimencionada, (x, y))
    # parede invisível
    parede = pygame.Rect(300, 100, 50, 200)

    # retângulo do jogador
    lula_rect = sprite_lula_redimencionada.get_rect(topleft=(x, y))

    # colisão
    if lula_rect.colliderect(parede):
        x = random.randint(220, 222)
        #atualizando a tela
    pygame.display.flip()