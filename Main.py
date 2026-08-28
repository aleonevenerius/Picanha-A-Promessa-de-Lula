# Importando a bilbioteca Pygame
import pygame
# importando submódulo cujas as funções e constantes serão usadas.
from pygame.locals import *
# Importando a biblioteca cujas as funções de saída serão substanciais para este programa.
from sys import exit
# Importando biblioteca Random
import random

# Iniciando Pygame
pygame.init()

# Definindo as dimensões da janela conforme as dimensões do cenário principal
largura, altura = 1040, 512
tela = pygame.display.set_mode((largura, altura))

# Nome da janela
pygame.display.set_caption("A Picanha: A Promessa de Lula")

# Cenário principal
cenario_principal = pygame.image.load(r"C:\Programming\Extraordinary\Games\Picanha\Sprites\cenario_principal.png")

# Sprite original do Lula e picanha
sprite_lula_original = pygame.image.load(r"C:\Programming\Extraordinary\Games\Picanha\Sprites\lula_sprite.png")
sprite_picanha_original = pygame.image.load(r"C:\Programming\Extraordinary\Games\Picanha\Sprites\Picanha.png")

# Redimensionando o sprite do Lula
altura_lula, largura_lula = 32*7, 32*7
sprite_lula = pygame.transform.scale(sprite_lula_original, (largura_lula, altura_lula))

# Redimensionando o sprite da picanha
altura_picanha, largura_picanha = altura_lula, largura_lula
sprite_picanha = pygame.transform.scale(sprite_picanha_original, (largura_picanha, altura_picanha))

# Posição Lula
x, y = 136, 136
# Posição picanha
x_picanha, y_picanha = x+15, y+15 # Destartes, a picanha estará sempre adjacente ao Lula com adicional de 15 a sua posição original desse.

# Definindo dimensões do retângulo relativo ao Lula
largura_lula, altura_lula = sprite_lula.get_width(), sprite_lula.get_height()
# Definindo dimensões do retângulo relativo à picanha
largura_picanha, altura_picanha = sprite_lula.get_width(), sprite_lula.get_height()

# Frame do jogo
clock = pygame.time.Clock()
tecla = pygame

while True:
    # Controlar frame
    clock.tick(45)
    # Limpar tela
    tela.fill((0,0,0))
    # Verificar eventos
    for event in pygame.event.get():
        # Fechar janela
        if event.type == QUIT:
            pygame.quit()
            exit()
        #-----------------------Movimento----------------------
        
        # Esquerda
        if pygame.key.get_pressed()[K_a]:
            x -= 20
        # Direita
        elif pygame.key.get_pressed()[K_d]:
            x += 20
        # Descer
        elif pygame.key.get_pressed()[K_s]:
            y += 20
        # Subir
        elif pygame.key.get_pressed()[K_w]:
            y -= 20
            
        # ----------------------Habilidades----------------------
        # Jogar picanha
        elif pygame.key.get_pressed()[K_p]:
            x_picanha, y_picanha = x, y # Picanha logrará a mesma posição de Lula
            x_picanha += 5 # Eixo 'x' relativo à picanha será incrementado valor 5
            print(f'Picanha:{x_picanha}') # Teste
            print(f'Lula:{x}') # Teste
            
          
    # Exibir cenário principal
    tela.blit(cenario_principal, (0,0))
    # Exibir Lula
    tela.blit(sprite_lula, (x,y))
    tela.blit(sprite_picanha, (x_picanha, y_picanha))
    # Retângulo Lula
    #lulaR = sprite_lula.get_rect(topleft=(x,y))
    
    # Atualizar tela
    pygame.display.flip()    