import pygame
from scripts.entidades.funcionarios.seguranca import *

# scene 4
                    # x     y    w   h
                
# scene 4
terreo = pygame.image.load("assets/img/scenes/terreo/terreo.jpg")

# HITBOXES
hitboxes_terreo = [
    #PAREDES
    pygame.Rect(1, 965, 1920, 1),  # bottom
    pygame.Rect(30, 0, 1, 187),  # left1
    pygame.Rect(30, 354, 1, 1080),  # left2
    pygame.Rect(1, 189, 30, 1),  # quina da parede 1
    pygame.Rect(1, 353, 30, 1),  # quina da parede 2
    pygame.Rect(1880, 0, 1, 1080),  # right
    pygame.Rect(1, 75, 1920, 1),  # top
    #pygame.Rect(867, 520, 1, 51),  # parede esquerda da supervisão/superior
    pygame.Rect(375, 600, 33, 370),  # parede esquerda da supervisão
    pygame.Rect(977, 27, 32, 335),  # central top
    pygame.Rect(972, 615, 32, 450),  # central bottom
    pygame.Rect(1532, 24, 29, 310),  # top right
    pygame.Rect(395, 27, 30, 150),  # parede1 escada
    pygame.Rect(575, 27, 25, 150),  # parede2 escada
    pygame.Rect(222, 793, 29, 150),  # bancada da recep esquerda
    pygame.Rect(222, 793, 156, 23),  # bancada da recep direita
    pygame.Rect(501, 180, 70, 1),  # linha escada

    #MESAS
    pygame.Rect(805, 157, 65, 51),  # mesa2_c4
    pygame.Rect(835, 280, 62, 51),  # mesa3_c4
    pygame.Rect(787, 685, 51, 250),  # mesa principal secretaria

    pygame.Rect(1220, 162, 65, 20),  # mesa_supervisao_c4
    pygame.Rect(1151, 675, 89, 40),  # mesa1_sala_professores_c4
    pygame.Rect(1495, 680, 75, 145),  # mesa2_sala_professores_c4
    pygame.Rect(1695, 675, 75, 50),  # mesa3_sala_professores_c4
    pygame.Rect(1697, 831, 71, 48),  # mesa4_sala_professores_c4
    pygame.Rect(1326, 875, 58, 15),  # mesa5_sala_professores_c4
    pygame.Rect(1041, 863, 81, 26),  # mesa_pc_professores_c4
    pygame.Rect(1742, 156, 90, 83),   # mesa_salati_c4
    pygame.Rect(478, 633, 80, 57),   # mesa1 secretaria

    #CADEIRAS
    pygame.Rect(885, 172, 30, 18),  # cadeira2_mesa2_c4
    pygame.Rect(787, 290, 30, 18),  # cadeira1_mesa3_c4
    pygame.Rect(914, 298, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(836, 230, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(848, 351, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(744, 158, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(814, 98, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(1705, 785, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(1707, 899, 30, 18),  # cadeira2_mesa3_c4
    pygame.Rect(1229, 115, 30, 18),  # cadeira2_mesa3_c4
    
    
    # SOfás
    pygame.Rect(600, 646, 16, 25),  # sofa da mesa1 secretaria
    pygame.Rect(695, 685, 18, 30),  # sofa1 da mesa principal secretaria
    pygame.Rect(695, 775, 18, 30),  # sofa2 da mesa principal secretaria
    pygame.Rect(695, 865, 18, 30),  # sofa3 da mesa principal secretaria
    pygame.Rect(475, 716, 30, 207), # sofás da secretaria

    pygame.Rect(1110, 695, 28, 16),  # cadeira1_mesa1_professores_c4
    pygame.Rect(1250, 705, 24, 20),  # cadeira2_mesa1_professores_c4
    pygame.Rect(1444, 710, 29, 19),  # cadeira1_mesa2_professores_c4
    pygame.Rect(1444, 780, 24, 20),  # cadeira2_mesa2_professores_c4
    pygame.Rect(1593, 768, 22, 20),  # cadeira3_mesa2_professores_c4
    pygame.Rect(1789, 680, 29, 20),  # cadeira1_mesa3_professores_c4
    pygame.Rect(1789, 841, 29, 20),  # cadeira1_mesa4_professores_c4
    pygame.Rect(1397, 887, 26, 10),  # cadeira1_mesa5_professores_c4
    pygame.Rect(1049, 904, 22, 13),   # banco_mesa_professores_c4
    pygame.Rect(854, 685, 25, 20),  # cadeira1 mesa principal
    pygame.Rect(854, 763, 25, 20),  # cadeira2 mesa principal
    pygame.Rect(854, 852, 25, 20),  # cadeira3 mesa principal

    #PLANTAS
    pygame.Rect(34, 485, 50, 160),   # plantaleft_c4
    pygame.Rect(950, 60, 25, 78),    # plantamid_c4

    #OBJETOS
    pygame.Rect(1045, 837, 35, 42),  # pc_mesa_professores_c4
    pygame.Rect(1005, 600, 620, 5),  # objetos professores
    pygame.Rect(1570, 77, 295, 20),  # objetos_sala_ti_c4
    pygame.Rect(1311, 78, 144, 35),  # objetos_supervisao_c4
    pygame.Rect(1178, 835, 76, 35),  # estante_verde_professores_c4
    pygame.Rect(1130, 852, 40, 20),  # armario_amarelo_professores_c4
    pygame.Rect(1701, 252, 170, 73),  # estante_branca_professores_c4
    pygame.Rect(929, 728, 38, 215),  # armário1 secretaria
    pygame.Rect(414, 596, 130, 20),  # armario2 secretaria
    pygame.Rect(1483, 118, 93, 104),  # armario supervisao
    pygame.Rect(715, 305, 155, 1),  #extra

    #SOFÁS
    pygame.Rect(662, 260, 42, 25), #3
    pygame.Rect(648, 156, 40, 27), #4
    
    # Npcs
    pygame.Rect(147, 94, 154, 86),  # dupla
    pygame.Rect(34, 365, 62, 90),  # npc proximo a planta
    pygame.Rect(552, 187, 74, 56),   # balão de fala
    
    pygame.Rect(845, 680, 126, 1), # linha que impede jogador na central de atdm
    
    pygame.Rect(1582, 260, 120, 1), # linha que impede o jogador de entrar na sala do ramon
    pygame.Rect(1010, 315, 113, 1), # linha que impede o jogador de entrar na sala da supervisão
    pygame.Rect(1620, 600, 144, 1) # linha que impede o jogador de entrar na sala dos professores
    
]

# ESCADA
subir_primeiro_andar_c4 = pygame.Rect(531, 101, 1, 40)
subir_primeiro_andar_x = 1450
subir_primeiro_andar_y = 300

# SAÍDA
saida_terreo = pygame.Rect(100, 960, 65, 1)
saida_terreo_x = 855
saida_terreo_y = 330

# IR PARA O CORREDOR
corredor_entrada = pygame.Rect(5, 190, 1, 165)
corredor_entrada_x = 1800
corredor_entrada_y = 380

# Imagens e hitboxes das paredes da supervisão
parede_supervisao = pygame.image.load("assets/img/scenes/terreo/parede_supervisao.png")
area_supervisao = pygame.Rect(342, 415, 550, 240)
parede_top_supervisao1 = pygame.Rect(409, 588, 470, 1)  # parede superior1 da supervisão
parede_top_supervisao2 = pygame.Rect(409, 565, 441, 1)  # parede superior2 da supervisão

# Imagens e hitboxes das paredes da sala da TI
parede_ti = pygame.image.load("assets/img/scenes/terreo/parede_ti.png")
area_ti = pygame.Rect(1068, 239, 533, 178)
parede_ti1 = pygame.Rect(1120, 372, 462, 1)  # parede superior1 da supervisão
parede_ti2 = pygame.Rect(1120, 370, 462, 1)  # parede superior2 da supervisão

# Imagens e hitboxes das paredes da sala dos professores
superior_professores = pygame.image.load("assets/img/scenes/terreo/superior_professores.png")
area_professores = pygame.Rect(936, 440, 720, 219)
superior_professores1 = pygame.Rect(1007, 592, 600, 1)  # parede superior1 da supervisão
superior_professores2 = pygame.Rect(1007, 560, 600, 1)  # parede superior2 da supervisão

# Imagens e hitboxes da parede final de cima
parede_final1 = pygame.image.load("assets/img/scenes/terreo/parede_final1.png")

# Imagens e hitboxes da parede final de baixo
area_final2 = pygame.Rect(1724, 464, 162, 182)
parede_final2 = pygame.image.load("assets/img/scenes/terreo/parede_final2.png")
parede_final2_1 = pygame.Rect(1760, 592, 600, 1)
parede_final2_2 = pygame.Rect(1760, 605, 600, 1)

parede_terreo = pygame.image.load("assets/img/scenes/terreo/parede_terreo.png")
parede_terreo2 = pygame.image.load("assets/img/scenes/terreo/parede_terreo2.png")

# Funcinários
atendente1 = pygame.image.load("assets/sprites/funcionarios/atendente1/atendente1.png")
atendente2 = pygame.image.load("assets/sprites/funcionarios/atendente2/atendente2.png")
atendente3 = pygame.image.load("assets/sprites/funcionarios/atendente3/atendente3.png")
atendente4 = pygame.image.load("assets/sprites/funcionarios/atendente4/atendente4.png")
cristiane = pygame.image.load("assets/sprites/funcionarios/supervisao/cristiane.png")
amanda = pygame.image.load("assets/sprites/funcionarios/supervisao/amanda.png")
amanda_l = pygame.image.load("assets/sprites/funcionarios/supervisao/amanda_l.png")
rafaela = pygame.image.load("assets/sprites/funcionarios/supervisao/rafaela.png")

# Hitbox de diálogo
recepcionista_dialogo = pygame.Rect(145, 800, 77, 150)
recepcionista_dialog_concluido = False
atendente_dialogo = pygame.Rect(720, 675, 63, 235)
atendente_dialog_concluido = False

# Bloqueio de progresso
bloqueio_progresso1 = pygame.Rect(35, 800, 341, 1)
bloqueio_progresso1_on = True

bloqueio_progresso2 = pygame.Rect(426, 202, 146, 1)
bloqueio_progresso2_on = True

# Cadeira azul
chair_top = pygame.image.load("assets/img/scenes/terreo/chair_top.png")

# Dicas visuais
area_pontilhada = pygame.image.load("assets/img/scenes/terreo/area_pontilhada.png")
tip1 = pygame.image.load("assets/img/scenes/terreo/tip1.png")

