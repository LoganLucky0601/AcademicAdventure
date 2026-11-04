import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc65 = [
    pygame.image.load("assets/sprites/alunos/npc65/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc65/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc65/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc65/top4.png")
]

spr_baixo_npc65 = [
    pygame.image.load("assets/sprites/alunos/npc65/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc65/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc65/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc65/bottom4.png")
]

spr_esquerda_npc65 = [
    pygame.image.load("assets/sprites/alunos/npc65/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc65/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc65/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc65/left4.png")
]

spr_direita_npc65 = [
    pygame.image.load("assets/sprites/alunos/npc65/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc65/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc65/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc65/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc65 = NPC(
    1300,  # npc_x
    665,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc65,
        "esquerda": spr_esquerda_npc65,
        "cima": spr_cima_npc65,
        "baixo": spr_baixo_npc65
    },
    "cima"  # direção inicial
)

spr_atual_npc65 = npc65.animacoes["cima"][0]

npc65_rect = pygame.Rect(
    npc65.npc_x, 
    npc65.npc_y, 
    spr_atual_npc65.get_width(), 
    spr_atual_npc65.get_height()
)