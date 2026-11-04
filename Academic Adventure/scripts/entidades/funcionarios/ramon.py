import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_ramon = [
    pygame.image.load("assets/sprites/funcionarios/ramon/top1.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/top2.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/top3.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/top4.png")
]

spr_baixo_ramon = [
    pygame.image.load("assets/sprites/funcionarios/ramon/bottom1.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/bottom2.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/bottom3.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/bottom4.png")
]

spr_esquerda_ramon = [
    pygame.image.load("assets/sprites/funcionarios/ramon/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/left2.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/left3.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/left4.png")
]

spr_direita_ramon = [
    pygame.image.load("assets/sprites/funcionarios/ramon/right1.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/right2.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/right3.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/right4.png")
]

spr_idle_ramon = [
    pygame.image.load("assets/sprites/funcionarios/ramon/idle_bottom.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/idle_top.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/idle_left.png"),
    pygame.image.load("assets/sprites/funcionarios/ramon/idle_right.png")
]

# Crie uma instância do NPC usando a classe NPC
ramon = NPC(
    1640,  # npc_x
    195,  # npc_y
    0,  # velocidade
    245,  # limite_esquerda
    999999,  # limite_direita
    {
        "direita": spr_direita_ramon,
        "esquerda": spr_esquerda_ramon,
        "cima": spr_cima_ramon,
        "baixo": spr_baixo_ramon,
        "idle": spr_idle_ramon
    },
    "esquerda"  # direção inicial
)
spr_atual_ramon = ramon.animacoes["idle"][2]

ramon_rect = pygame.Rect(
    ramon.npc_x, 
    ramon.npc_y, 
    spr_atual_ramon.get_width(), 
    spr_atual_ramon.get_height()
)
