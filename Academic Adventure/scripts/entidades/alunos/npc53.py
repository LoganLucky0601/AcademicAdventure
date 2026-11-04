import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc53 = [
    pygame.image.load("assets/sprites/alunos/npc53/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc53/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc53/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc53/top4.png")
]

spr_baixo_npc53 = [
    pygame.image.load("assets/sprites/alunos/npc53/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc53/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc53/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc53/bottom4.png")
]

spr_esquerda_npc53 = [
    pygame.image.load("assets/sprites/alunos/npc53/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc53/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc53/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc53/left4.png")
]

spr_direita_npc53 = [
    pygame.image.load("assets/sprites/alunos/npc53/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc53/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc53/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc53/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc53 = NPC(
    1100,  # npc_x
    330,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc53,
        "esquerda": spr_esquerda_npc53,
        "cima": spr_cima_npc53,
        "baixo": spr_baixo_npc53
    },
    "cima"  # direção inicial
)

spr_atual_npc53 = npc53.animacoes["cima"][0]

npc53_rect = pygame.Rect(
    npc53.npc_x, 
    npc53.npc_y, 
    spr_atual_npc53.get_width(), 
    spr_atual_npc53.get_height()
)