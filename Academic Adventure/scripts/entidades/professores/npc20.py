import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc20 = [
    pygame.image.load("assets/sprites/professores/npc20/top1.png"),
    pygame.image.load("assets/sprites/professores/npc20/top2.png"),
    pygame.image.load("assets/sprites/professores/npc20/top3.png"),
    pygame.image.load("assets/sprites/professores/npc20/top4.png")
]

spr_baixo_npc20 = [
    pygame.image.load("assets/sprites/professores/npc20/bottom4.png"),
    pygame.image.load("assets/sprites/professores/npc20/bottom2.png"),
    pygame.image.load("assets/sprites/professores/npc20/bottom3.png"),
    pygame.image.load("assets/sprites/professores/npc20/bottom4.png")
]

spr_esquerda_npc20 = [
    pygame.image.load("assets/sprites/professores/npc20/left1.png"),
    pygame.image.load("assets/sprites/professores/npc20/left2.png"),
    pygame.image.load("assets/sprites/professores/npc20/left3.png"),
    pygame.image.load("assets/sprites/professores/npc20/left4.png")
]

spr_direita_npc20 = [
    pygame.image.load("assets/sprites/professores/npc20/right1.png"),
    pygame.image.load("assets/sprites/professores/npc20/right2.png"),
    pygame.image.load("assets/sprites/professores/npc20/right3.png"),
    pygame.image.load("assets/sprites/professores/npc20/right4.png")
]

# Crie uma instância do NPC usando a classe Npc
npc20 = NPC(
    850,  # npc_x
    180,  # npc_y
    1,  # velocidade
    9999999,  # limite_direita
    -999999,  # limite_esquerda
    {
        "cima": spr_cima_npc20,
        "baixo": spr_baixo_npc20,
        "esquerda": spr_esquerda_npc20,
        "direita": spr_direita_npc20
    },
    "baixo"  # direção inicial
)

spr_atual_npc20 = npc20.animacoes["baixo"][3]

npc20_rect = pygame.Rect(
    npc20.npc_x,
    npc20.npc_y,
    spr_atual_npc20.get_width(),
    spr_atual_npc20.get_height()
)