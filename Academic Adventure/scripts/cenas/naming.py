import pygame

# Crachá de inserção de nome
tela_naming = pygame.image.load("assets/img/interface/tela_naming.png")

# Carregar a imagem do triângulo
seta_verde = pygame.image.load("assets/img/interface/seta_verde.png")
seta_vermelha = pygame.image.load("assets/img/interface/seta.png")
# Posição do triângulo
seta_vermelha_position = (560, 365)
# Variável de controle
seta_vermelha_visible = True
# Controle de tempo para o piscar
blink_interval = 500  # Em milissegundos
last_blink_time = pygame.time.get_ticks()
