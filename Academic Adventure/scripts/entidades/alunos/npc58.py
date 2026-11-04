import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc58 = [
    pygame.image.load("assets/sprites/alunos/npc58/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc58/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc58/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc58/top4.png")
]

spr_baixo_npc58 = [
    pygame.image.load("assets/sprites/alunos/npc58/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc58/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc58/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc58/bottom4.png")
]

spr_esquerda_npc58 = [
    pygame.image.load("assets/sprites/alunos/npc58/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc58/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc58/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc58/left4.png")
]

spr_direita_npc58 = [
    pygame.image.load("assets/sprites/alunos/npc58/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc58/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc58/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc58/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc58 = NPC(
    895,  # npc_x
    460,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc58,
        "esquerda": spr_esquerda_npc58,
        "cima": spr_cima_npc58,
        "baixo": spr_baixo_npc58
    },
    "cima"  # direção inicial
)

spr_atual_npc58 = npc58.animacoes["cima"][0]

npc58_rect = pygame.Rect(
    npc58.npc_x, 
    npc58.npc_y, 
    spr_atual_npc58.get_width(), 
    spr_atual_npc58.get_height()
)