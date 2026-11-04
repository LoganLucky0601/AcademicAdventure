import pygame

auditorio_fundo = pygame.image.load('assets/img/scenes/auditorio/auditorio_fundo.jpg')
bandeiras = pygame.image.load('assets/img/scenes/auditorio/bandeiras.png')

hitboxes_auditorio = [
    
    # PAREDES
    pygame.Rect(290, 130, 1, 1080), # ESQUERDA
    pygame.Rect(1675, 130, 1, 1080), # DIREITA
    pygame.Rect(290, 155, 1920, 1), # CIMA
    pygame.Rect(290, 900, 1920, 1), # BAIXO
    
    # CONJUNTO DE CADEIRAS
    pygame.Rect(340, 175, 460, 160),
    pygame.Rect(325, 543, 460, 160),
    pygame.Rect(1165, 170, 475, 540),
    
    #MESA
    pygame.Rect(930, 175, 90, 90),
    
    # BANCADA
    pygame.Rect(660, 775, 65, 80),
    
    #BANDEIRA
    pygame.Rect(450, 875, 25, 13),
    
    # NPC
    pygame.Rect(965, 845, 50, 35),
    
    
    ]

dialogo_finalizacao = pygame.Rect(935, 800, 110, 75),

finalizacao = False

entrou_auditorio = False