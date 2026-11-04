import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc47 = [
    pygame.image.load("assets/sprites/alunos/npc47/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc47/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc47/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc47/top4.png")
]

spr_baixo_npc47 = [
    pygame.image.load("assets/sprites/alunos/npc47/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc47/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc47/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc47/bottom4.png")
]

spr_esquerda_npc47 = [
    pygame.image.load("assets/sprites/alunos/npc47/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc47/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc47/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc47/left4.png")
]

spr_direita_npc47 = [
    pygame.image.load("assets/sprites/alunos/npc47/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc47/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc47/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc47/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc47 = NPC(
    1295,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc47,
        "esquerda": spr_esquerda_npc47,
        "cima": spr_cima_npc47,
        "baixo": spr_baixo_npc47
    },
    "cima"  # direção inicial
)

spr_atual_npc47 = npc47.animacoes["cima"][0]

npc47_rect = pygame.Rect(
    npc47.npc_x, 
    npc47.npc_y, 
    spr_atual_npc47.get_width(), 
    spr_atual_npc47.get_height()
)