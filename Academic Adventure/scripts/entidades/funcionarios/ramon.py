import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_ramon = [
    pygame.image.load("assets/sprites/funcionarios/Ramon/top1.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/top2.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/top3.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/top4.png")
]

spr_baixo_ramon = [
    pygame.image.load("assets/sprites/funcionarios/Ramon/bottom1.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/bottom2.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/bottom3.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/bottom4.png")
]

spr_esquerda_ramon = [
    pygame.image.load("assets/sprites/funcionarios/Ramon/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/left2.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/left3.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/left4.png")
]

spr_direita_ramon = [
    pygame.image.load("assets/sprites/funcionarios/Ramon/right1.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/right2.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/right3.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/right4.png")
]

spr_idle_ramon = [
    pygame.image.load("assets/sprites/funcionarios/Ramon/idle_bottom.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/idle_top.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/idle_left.png"),
    pygame.image.load("assets/sprites/funcionarios/Ramon/idle_right.png")
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
