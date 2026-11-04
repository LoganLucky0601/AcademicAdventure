import pygame
from scripts.font import *
from scripts.settings import screen

pygame.init()

# Cena menu
tela_introducao = pygame.image.load("assets/img/scenes/introducao/tela_introducao.jpeg")

# Press enter
key_position = (35, 750)
# Variável de controle
is_key_visible = True
# Controle de tempo para o piscar
blink_interval = 500  # Em milissegundos
last_blink_time = pygame.time.get_ticks()

# Seta amarela de diálogo
seta_amarela  = pygame.image.load("assets/img/interface/seta_amarela.png")
pointer_position = (1780, 1000)
# Variável de controle
is_pointer_visible = True
# Controle de tempo para o piscar
blink_interval_seta = 500  # Em milissegundos
last_blink_time_seta = pygame.time.get_ticks()

