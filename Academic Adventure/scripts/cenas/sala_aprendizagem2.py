import pygame
from scripts.entidades import * 

# Carregar imagem da cena
aprendizagem2 = pygame.image.load("assets/img/scenes/aprendizagem/sala_aprendizagem.jpg")
npc78 = pygame.image.load("assets/sprites/professores/npc78/bottom1.png")

hitboxes_apredizagem2 = [
    #Paredes
    pygame.Rect(456, 205, 1010, 1), #parede top 
    pygame.Rect(456, 820, 1010, 1), #parede bottom 
    pygame.Rect(456, 191, 1, 623), #parede left 
    pygame.Rect(1465, 191, 1, 623), #parede left 
    
    #Plantas
    pygame.Rect(1425, 730, 30, 44), #planta right 
    
    # Fileira de mesas (da esquerda para direita)
    pygame.Rect(500, 370, 60, 500), #fileira de mesa 1
    pygame.Rect(700, 370, 60, 500), #fileira de mesa 2
    pygame.Rect(905, 370, 60, 500), #fileira de mesa 3
    pygame.Rect(1104, 370, 60, 500), #fileira de mesa 4
    pygame.Rect(1315, 370, 60, 500), #fileira de mesa 5
    
    # Armários
    pygame.Rect(478, 190, 74, 43), #armário 1
    pygame.Rect(755, 190, 74, 43), #armário 2
    pygame.Rect(1108, 190, 148, 43), #armário 3
    
    # Professora
    pygame.Rect(867, 180, 50, 75),
    pygame.Rect(624, 280, 89, 23) # mesa professora
    
]

# Variáveis interativas
sair_da_sala_ap2 = pygame.Rect(1355, 228, 45, 1)
sair_da_sala_ap2_x = 555
sair_da_sala_ap2_y = 340

# Cadeiras
cadeiras_f1 = [
    # Fileira 1 (começando de cima para baixo, da esquerda para direita)
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/amarela.png"), (500, 400)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/azul.png"), (700, 400)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/vermelha.png"), (905, 400)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/verde.png"), (1105, 400)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/laranja.png"), (1310, 400))
]

cadeiras_f2 = [
    # Fileira 2 (começando de cima para baixo, da esquerda para direita)
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/vermelha.png"), (500, 515)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/verde.png"), (700, 515)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/laranja.png"), (905, 515)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/azul.png"), (1105, 515)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/amarela.png"), (1310, 515)),
]

cadeiras_f3 = [
    # Fileira 3 (começando de cima para baixo, da esquerda para direita)
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/laranja.png"), (500, 630)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/amarela.png"), (700, 630)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/verde.png"), (905, 630)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/vermelha.png"), (1105, 630)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/azul.png"), (1310, 630))
]

cadeiras_f4 = [
    # Fileira 4 (começando de cima para baixo, da esquerda para direita)
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/verde.png"), (500, 730)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/vermelha.png"), (700, 730)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/azul.png"), (905, 730)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/laranja.png"), (1105, 730)),
    (pygame.image.load("assets/img/scenes/aprendizagem/cadeiras/amarela.png"), (1315, 730)),
]

# Npcs
npcs_ap2_f1 = [npc51, npc52, npc53, npc54]

npcs_ap2_f2 = [npc55, npc56, npc57, npc58, npc59, npc60]

npcs_ap2_f3 = [npc62, npc63, npc64, npc66]

npcs_ap2_f4 = [npc68, npc69, npc65]




aprendizagem2_txt = pygame.image.load("assets/img/scenes/aprendizagem/aprendizagem2_txt.png")
