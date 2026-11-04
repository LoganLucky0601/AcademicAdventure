import pygame

segundo_andar = pygame.image.load("assets/img/scenes/segundo/segundo_andar.jpg")

#HITBOXES

hitboxes_segundo_andar = [
    #PAREDES
    pygame.Rect(96, 330, 1725, 1), # parede top
    pygame.Rect(91, 708, 1725, 1), # parede bottom
    pygame.Rect(93, 288, 1, 420), # parede left
    pygame.Rect(1820, 288, 1, 420), # parede right

    pygame.Rect(1299, 292, 28, 153), # muro esquerda à escada
    pygame.Rect(1582, 292, 28, 153), # muro direita à escada
    pygame.Rect(385, 289, 28, 153), # muro esquerda
    pygame.Rect(361, 592, 35, 115), # muro 1 da esquerda pra direita
    pygame.Rect(727, 592, 35, 115), # muro 2 da esquerda pra direita
    pygame.Rect(1057, 592, 35, 115), # muro 3 da esquerda pra direita
    pygame.Rect(1387, 592, 35, 115), # muro 4 da esquerda pra direita

    pygame.Rect(1331, 422, 80, 1), # linha escada
    pygame.Rect(1331, 422, 80, 1), # linha escada

    #ARMÁRIOS
    pygame.Rect(137, 321, 217, 56), # armário esquerda

    #CADEIRAS
    pygame.Rect(157, 435, 30, 15), # cadeira 1 # Mesa1
    pygame.Rect(301, 435, 28, 15), # cadeira 2

    pygame.Rect(147, 598, 28, 15), # cadeira 3 # Mesa2
    pygame.Rect(298, 635, 28, 15), # cadeira 4

    pygame.Rect(795, 645, 33, 19), # cadeira 5 # Mesa3
    pygame.Rect(966, 637, 33, 19), # cadeira 6

    pygame.Rect(1150, 606, 33, 19), # cadeira 7 # Mesa4
    pygame.Rect(1303, 645, 33, 19), # cadeira 8

    pygame.Rect(1457, 605, 33, 19), # cadeira 9 # Mesa5
    pygame.Rect(1608, 643, 33, 19), # cadeira 10

    # MESA
    pygame.Rect(216, 415, 65, 34), # mesa 1
    pygame.Rect(205, 615, 65, 34), # mesa 2

    pygame.Rect(865, 615, 65, 34), # mesa 3
    pygame.Rect(1205, 615, 65, 34), # mesa 4

    pygame.Rect(1513, 615, 61, 34), # mesa 5

    #PLANTAS
    pygame.Rect(97, 617, 52, 79), # plantas (extrema esquerda inferior)

    pygame.Rect(1024, 645, 25, 60), # plantas 1 (planta do meio, esquerda)
    pygame.Rect(1100, 645, 25, 60), # plantas 2 (planta do meio, direita)

    pygame.Rect(1765, 656, 56, 33), # plantas (2 de baixo) (extrema direita, inferior)
    pygame.Rect(1791, 625, 22, 25), # plantas (1 de cima) (extrema direita, inferior)

    #SOFÁS
    pygame.Rect(439, 640, 42, 22), # sofá 1 (sofá do meio, na esquerda)
    pygame.Rect(639, 640, 42, 22), # sofá 2 (sofá do meio, na direita) 
    pygame.Rect(546, 605, 42, 22), # sofá 3 (sofá do meio, no meio)

    # ÁREA DIREITA
    pygame.Rect(1613, 313, 202, 139), # cadeiras, mesa e armario da direita (1 hitbox para todos)
]

#OBJETOS INTERATIVOS
descer_escada_2andar = pygame.Rect(1366, 384, 1, 22)
descer_escada_2andar_x = 1460
descer_escada_2andar_y = 280

#PORTA DO AUDITÓRIO
entrada_auditorio = pygame.Rect(560, 356, 22, 1)
entrada_auditorio_x = 300
entrada_auditorio_y = 385

#SALA VAZIA1
entrada_sala_vazia1 = pygame.Rect(1075, 365, 22, 1)
entrada_sala_vazia1_x = 1315
entrada_sala_vazia1_y = 220

#SALA VAZIA2
entrada_sala_vazia2 = pygame.Rect(815, 365, 22, 1)
entrada_sala_vazia2_x = 1315
entrada_sala_vazia2_y = 220

entrada_sala_aprendizagem_x = 1300
entrada_sala_aprendizagem_y = 220


segundo_txt = pygame.image.load("assets/img/scenes/segundo/segundo_txt.png")
