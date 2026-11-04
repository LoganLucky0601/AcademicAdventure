import pygame

corredor_fundo = pygame.image.load("assets/img/scenes/biblioteca/corredor_biblioteca.jpg")


# SAÍDA
corredor_saida = pygame.Rect(1890, 418, 1, 135)
corredor_saida_x = 5
corredor_saida_y = 190

# ENTRADA PARA A BIBLIOTECA
entrada_biblioteca = pygame.Rect(232, 802, 153, 1)
entrada_biblioteca_x = 1390
entrada_biblioteca_y = 680


hitboxes_corredor = [
  pygame.Rect(405, 685, 1900, 1), # baixo
  pygame.Rect(45, 685, 195, 1), # baixo2
  pygame.Rect(50, 305, 1275, 1), # top1
  pygame.Rect(1327, 215, 1, 87), # top1 2.4
  pygame.Rect(1328, 215, 140, 1), # top1 2.5
  pygame.Rect(1465, 305, 1000, 1), # top1 2.6
  pygame.Rect(1861, 260, 1, 150), # direita 1
  pygame.Rect(1861, 560, 1, 150), # direita 2
  pygame.Rect(45, 240, 1, 440), # esquerda
  
  # OBJETOS
  pygame.Rect(1380, 235, 83, 65), # top1 2.6
  pygame.Rect(80, 305, 215, 33), # armário
  
  ]