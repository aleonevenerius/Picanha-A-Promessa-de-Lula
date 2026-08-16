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

# Cenário principal
cenario_principal = pygame.image.load(r"C:\Programming\Extraordinary\Games\Picanha\Sprites\cenario_principal.png")

# Sprite original do Lula
sprite_lula_original = pygame.image.load(r"C:\Programming\Extraordinary\Games\Picanha\Sprites\lula_sprite.png")
# Redimensionando o sprite do Lula
sprite_lula_redimencionada = pygame.transform.scale(sprite_lula, (largura_nova, altura_nova))


x, y = 136, 136
