import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc68 = [
    pygame.image.load("assets/sprites/alunos/npc68/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc68/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc68/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc68/top4.png")
]

spr_baixo_npc68 = [
    pygame.image.load("assets/sprites/alunos/npc68/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc68/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc68/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc68/bottom4.png")
]

spr_esquerda_npc68 = [
    pygame.image.load("assets/sprites/alunos/npc68/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc68/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc68/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc68/left4.png")
]

spr_direita_npc68 = [
    pygame.image.load("assets/sprites/alunos/npc68/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc68/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc68/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc68/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc68 = NPC(
    485,  # npc_x
    655,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc68,
        "esquerda": spr_esquerda_npc68,
        "cima": spr_cima_npc68,
        "baixo": spr_baixo_npc68
    },
    "cima"  # direção inicial
)

spr_atual_npc68 = npc68.animacoes["cima"][0]

npc68_rect = pygame.Rect(
    npc68.npc_x, 
    npc68.npc_y, 
    spr_atual_npc68.get_width(), 
    spr_atual_npc68.get_height()
)