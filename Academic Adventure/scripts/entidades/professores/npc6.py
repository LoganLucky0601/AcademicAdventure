import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc6 = [
    pygame.image.load("assets/sprites/professores/npc6/top1.png"),
    pygame.image.load("assets/sprites/professores/npc6/top2.png"),
    pygame.image.load("assets/sprites/professores/npc6/top3.png"),
    pygame.image.load("assets/sprites/professores/npc6/top4.png")
]

spr_baixo_npc6 = [
    pygame.image.load("assets/sprites/professores/npc6/bottom1.png"),
    pygame.image.load("assets/sprites/professores/npc6/bottom2.png"),
    pygame.image.load("assets/sprites/professores/npc6/bottom3.png"),
    pygame.image.load("assets/sprites/professores/npc6/bottom4.png")
]

spr_esquerda_npc6 = [
    pygame.image.load("assets/sprites/professores/npc6/left1.png"),
    pygame.image.load("assets/sprites/professores/npc6/left2.png"),
    pygame.image.load("assets/sprites/professores/npc6/left3.png"),
    pygame.image.load("assets/sprites/professores/npc6/left4.png")
]

spr_direita_npc6 = [
    pygame.image.load("assets/sprites/professores/npc6/right1.png"),
    pygame.image.load("assets/sprites/professores/npc6/right2.png"),
    pygame.image.load("assets/sprites/professores/npc6/right3.png"),
    pygame.image.load("assets/sprites/professores/npc6/right4.png")
]

# Crie uma instância do NPC usando a classe Npc
npc6 = NPC(
    -600,  # npc_x
    670,  # npc_y
    1,  # velocidade
    99999999,  # limite_esquerda
    845,  # limite_direita
    {
        "cima": spr_cima_npc6,
        "baixo": spr_baixo_npc6,
        "esquerda": spr_esquerda_npc6,
        "direita": spr_direita_npc6
    },
    "direita"  # direção inicial
)

spr_atual_npc6 = npc6.animacoes["direita"][0]

npc6_rect = pygame.Rect(
    npc6.npc_x,
    npc6.npc_y,
    spr_atual_npc6.get_width(),
    spr_atual_npc6.get_height()
)