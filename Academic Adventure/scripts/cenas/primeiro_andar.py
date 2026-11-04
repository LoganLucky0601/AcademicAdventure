import pygame

# Scene 5
primeiro_andar = pygame.image.load("assets/img/scenes/primeiro/primeiro_andar.jpg")

#HITBOXES
hitboxes_primeiro_andar = [
    pygame.Rect(49, 683, 1920, 1),    # bottom
    pygame.Rect(1860, 245, 1, 1080),  # right
    pygame.Rect(45, 245, 1, 1080),    # left
    pygame.Rect(51, 285, 260, 1),     # top1
    pygame.Rect(376, 285, 200, 1),    # top2
    pygame.Rect(637, 285, 200, 1),    # top3
    pygame.Rect(896, 285, 215, 1),    # top4
    pygame.Rect(1174, 285, 215, 1),   # top5
    pygame.Rect(1400, 285, 437, 1),   # top6
    pygame.Rect(1372, 240, 27, 140),  # parede esquerda da escada
    pygame.Rect(1631, 240, 27, 140),  # parede direita da escada
    pygame.Rect(1402, 373, 67, 1),     # borda escada
    pygame.Rect(1560, 373, 73, 1),     # borda da escada 2° andar
    
    #Sofás
    pygame.Rect(147, 311, 80, 5),     # sofá1
    pygame.Rect(428, 311, 80, 5),     # sofá2
    pygame.Rect(700, 314, 80, 5),     # sofá3
    pygame.Rect(966, 311, 80, 5),     # sofá4
    
    #Plantas
    pygame.Rect(381, 298, 25, 20),    # planta1
    pygame.Rect(651, 298, 25, 20),    # planta2
    pygame.Rect(916, 298, 25, 20),    # planta3
    pygame.Rect(1204, 298, 25, 20),    # planta4   
    
    # Objetos decorativos
    pygame.Rect(1668, 409, 188, 1),          # objeto decorativo
]

# OBJETOS INTERATIVOS
#Entradas sala de informática 1
entrada_sala_informatica = pygame.Rect(850, 300, 30, 1)     # entrada1
entrada_sala_informatica_x = 1360
entrada_sala_informatica_y = 220

#Entradas sala de informática 2
entrada_sala_informatica2 = pygame.Rect(1125, 300, 30, 1)     # entrada2
entrada_sala_informatica2_x = 480
entrada_sala_informatica2_y = 290

#Entradas sala de aprendizagem 1
entrada_sala_aprendizagem = pygame.Rect(330, 300, 30, 1)     # entrada1
entrada_sala_aprendizagem_x = 1300
entrada_sala_aprendizagem_y = 220

#Entradas sala de aprendizagem 2
entrada_sala_aprendizagem2 = pygame.Rect(590, 300, 30, 1)     # entrada2
entrada_sala_aprendizagem2_x = 1300
entrada_sala_aprendizagem2_y = 220

# Descida para o térreo
descer_escada_1andar = pygame.Rect(1465, 320, 1, 5)
descer_escada_1andar_x = 395
descer_escada_1andar_y = 110

# Descida para o térreo
subir_segundo_andar = pygame.Rect(1580, 325, 1, 10)
subir_segundo_andar_x = 1390
subir_segundo_andar_y = 330


primeiro_txt = pygame.image.load("assets/img/scenes/primeiro/primeiro_txt.png")