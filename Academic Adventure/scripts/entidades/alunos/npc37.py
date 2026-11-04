import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc37 = [
    pygame.image.load("assets/sprites/alunos/npc37/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc37/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc37/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc37/top4.png")
]

spr_baixo_npc37 = [
    pygame.image.load("assets/sprites/alunos/npc37/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc37/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc37/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc37/bottom4.png")
]

spr_esquerda_npc37 = [
    pygame.image.load("assets/sprites/alunos/npc37/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc37/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc37/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc37/left4.png")
]

spr_direita_npc37 = [
    pygame.image.load("assets/sprites/alunos/npc37/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc37/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc37/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc37/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc37 = NPC(
    895,  # npc_x
    440,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc37,
        "esquerda": spr_esquerda_npc37,
        "cima": spr_cima_npc37,
        "baixo": spr_baixo_npc37
    },
    "cima"  # direção inicial
)

spr_atual_npc37 = npc37.animacoes["cima"][0]

npc37_rect = pygame.Rect(
    npc37.npc_x, 
    npc37.npc_y, 
    spr_atual_npc37.get_width(), 
    spr_atual_npc37.get_height()
)