import pygame

biblioteca_fundo = pygame.image.load("assets/img/scenes/biblioteca/biblioteca.jpg")
parede_biblioteca = pygame.image.load("assets/img/scenes/biblioteca/parede_biblioteca.png")
estante1 = pygame.image.load("assets/img/scenes/biblioteca/estante1.png")
estante2 = pygame.image.load("assets/img/scenes/biblioteca/estante2.png")
estante3 = pygame.image.load("assets/img/scenes/biblioteca/estante3.png")

# SAÍDA PARA O CORREDOR
saida_biblioteca = pygame.Rect(1430, 675, 35, 1)
saida_biblioteca_x = 260
saida_biblioteca_y = 630


hitboxes_biblioteca = [
  #PAREDES
  pygame.Rect(425, 230, 840, 1),  # top
  pygame.Rect(260, 972, 1920, 1),  # bottom
  pygame.Rect(1270, 260, 1, 415),  # right
  pygame.Rect(1500, 690, 1, 300),  # right2
  pygame.Rect(425, 260, 1, 575),  # left1
  pygame.Rect(282, 830, 142, 1),  # left2
  pygame.Rect(285, 830, 1, 150),  # left3
  
  # CONJUNTO DE MESAS
  pygame.Rect(504, 230, 211, 87),  # 1
  pygame.Rect(771, 230, 211, 87),  # 2
  pygame.Rect(503, 371, 225, 272),  # 3
  
  # MESAS E CADEIRAS MENORES
  pygame.Rect(880, 585, 144, 38),  # 1
  pygame.Rect(848, 460, 75, 15),  # 1.5
  pygame.Rect(815, 477, 144, 38),  # 2
  pygame.Rect(912, 565, 75, 15),  # 2.5
  pygame.Rect(928, 400, 160, 38),  # 3
  pygame.Rect(970, 388, 75, 15),  # 3.5
  pygame.Rect(1152, 466, 114, 110),  # 4
  
  # OBJETOS
  pygame.Rect(1243, 353, 23, 90),  # 1
  pygame.Rect(1270, 680, 111, 1),  # 2
  
  # ESTANTES
  pygame.Rect(467, 766, 804, 1),  # 1
  pygame.Rect(467, 865, 850, 105),  # 1

  
  ]