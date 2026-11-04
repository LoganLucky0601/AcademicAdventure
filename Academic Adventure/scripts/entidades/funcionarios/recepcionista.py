import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_recepcionista = [
    pygame.image.load("assets/sprites/funcionarios/recepcionista/top1.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/top2.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/top3.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/top4.png")
]

spr_baixo_recepcionista = [
    pygame.image.load("assets/sprites/funcionarios/recepcionista/bottom1.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/bottom2.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/bottom3.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/bottom4.png")
]

spr_esquerda_recepcionista = [
    pygame.image.load("assets/sprites/funcionarios/recepcionista/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/left2.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/left3.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/left4.png")
]

spr_direita_recepcionista = [
    pygame.image.load("assets/sprites/funcionarios/recepcionista/right1.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/right2.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/right3.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/right4.png")
]

spr_idle_recepcionista = [
    pygame.image.load("assets/sprites/funcionarios/recepcionista/idle_bottom.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/idle_top.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/idle_left.png"),
    pygame.image.load("assets/sprites/funcionarios/recepcionista/idle_right.png"),
]

# Crie uma instância do NPC usando a classe NPC
recepcionista = NPC(
    245,  # npc_x
    805,  # npc_y
    0,  # velocidade
    245,  # limite_esquerda
    999999,  # limite_direita
    {
        "direita": spr_direita_recepcionista,
        "esquerda": spr_esquerda_recepcionista,
        "cima": spr_cima_recepcionista,
        "baixo": spr_baixo_recepcionista,
        "idle": spr_idle_recepcionista
    },
    "esquerda"  # direção inicial
)
spr_atual_recepcionista = recepcionista.animacoes["idle"][2]

recepcionista_rect = pygame.Rect(
    recepcionista.npc_x, 
    recepcionista.npc_y, 
    spr_atual_recepcionista.get_width(), 
    spr_atual_recepcionista.get_height()
)
