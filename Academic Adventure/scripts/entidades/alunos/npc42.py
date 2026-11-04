import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc42 = [
    pygame.image.load("assets/sprites/alunos/npc42/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc42/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc42/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc42/top4.png")
]

spr_baixo_npc42 = [
    pygame.image.load("assets/sprites/alunos/npc42/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc42/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc42/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc42/bottom4.png")
]

spr_esquerda_npc42 = [
    pygame.image.load("assets/sprites/alunos/npc42/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc42/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc42/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc42/left4.png")
]

spr_direita_npc42 = [
    pygame.image.load("assets/sprites/alunos/npc42/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc42/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc42/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc42/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc42 = NPC(
    895,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc42,
        "esquerda": spr_esquerda_npc42,
        "cima": spr_cima_npc42,
        "baixo": spr_baixo_npc42
    },
    "cima"  # direção inicial
)

spr_atual_npc42 = npc42.animacoes["cima"][0]

npc42_rect = pygame.Rect(
    npc42.npc_x, 
    npc42.npc_y, 
    spr_atual_npc42.get_width(), 
    spr_atual_npc42.get_height()
)