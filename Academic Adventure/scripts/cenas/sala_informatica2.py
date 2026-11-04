import pygame

# scene 6: Sala de Informática
sala_informatica2 = pygame.image.load("assets/img/scenes/informatica/sala_informatica2.jpg")
parede_sala_informatica2 = pygame.image.load("assets/img/scenes/informatica/parede_sala_informatica2.png")

# HITBOXES
hitboxes_informatica2 = [
    pygame.Rect(345, 245, 1260, 1),   # parede superior
    pygame.Rect(320, 1045, 1261, 1),   # parede inferior
    pygame.Rect(1574, 151, 1, 1000),   # parede direita
    pygame.Rect(360, 151, 1, 1000),   # parede esquerda
    
    # Mesa (esquerda para direita)
    pygame.Rect(362, 402, 90, 600),   # mesa 1
    pygame.Rect(875, 455, 185, 600),   # mesa 2 e 3
    pygame.Rect(1467, 402, 103, 600),   # mesa 4
    
    pygame.Rect(1462, 274, 40, 40),   # cadeira professor
    
    # Armário
    pygame.Rect(1533, 327, 45, 62),   # armário cinza
    
    # Fila de cadeiras
    pygame.Rect(475, 418, 33, 500),   # 1
    pygame.Rect(811, 444, 35, 452),   # 2
    pygame.Rect(1091, 480, 35, 452),   # 3
    pygame.Rect(1411, 400, 35, 500),   # 4
    
    pygame.Rect(1165, 230, 60, 80),   # 4
]

# Saída da sala de informática 2
sair_da_sala_inf2 = pygame.Rect(512, 275, 50, 1)
sair_da_sala_inf2_x = 1080
sair_da_sala_inf2_y = 310


informatica2_txt = pygame.image.load("assets/img/scenes/informatica/informatica2_txt.png")