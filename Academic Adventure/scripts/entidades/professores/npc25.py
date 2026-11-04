import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc25 = [
    pygame.image.load("assets/sprites/professores/npc25/top1.png"),
    pygame.image.load("assets/sprites/professores/npc25/top2.png"),
    pygame.image.load("assets/sprites/professores/npc25/top3.png"),
    pygame.image.load("assets/sprites/professores/npc25/top4.png")
]

spr_baixo_npc25 = [
    pygame.image.load("assets/sprites/professores/npc25/bottom1.png"),
    pygame.image.load("assets/sprites/professores/npc25/bottom2.png"),
    pygame.image.load("assets/sprites/professores/npc25/bottom3.png"),
    pygame.image.load("assets/sprites/professores/npc25/bottom4.png")
]

spr_esquerda_npc25 = [
    pygame.image.load("assets/sprites/professores/npc25/left1.png"),
    pygame.image.load("assets/sprites/professores/npc25/left2.png"),
    pygame.image.load("assets/sprites/professores/npc25/left3.png"),
    pygame.image.load("assets/sprites/professores/npc25/left4.png")
]

spr_direita_npc25 = [
    pygame.image.load("assets/sprites/professores/npc25/right1.png"),
    pygame.image.load("assets/sprites/professores/npc25/right2.png"),
    pygame.image.load("assets/sprites/professores/npc25/right3.png"),
    pygame.image.load("assets/sprites/professores/npc25/right4.png")
]

# Crie uma instância do NPC usando a classe Npc
npc25 = NPC(
    1175,  # npc_x
    580,  # npc_y
    1,  # velocidade
    99999,  # limite_direita
    865,  # limite_esquerda
    {
        "cima": spr_cima_npc25,
        "baixo": spr_baixo_npc25,
        "esquerda": spr_esquerda_npc25,
        "direita": spr_direita_npc25
    },
    "cima"  # direção inicial
)

spr_atual_npc25 = npc25.animacoes["cima"][0]

# Definindo a hitbox do NPC
hitbox_largura_npc25 = 80
hitbox_altura_npc25 = 90  # Diminuir a altura para que não inclua a cabeça nem os pés
ajuste_vertical_npc25 = 5

# Criar o Rect do NPC
npc25_rect = pygame.Rect(
    (spr_atual_npc25.get_width() - hitbox_largura_npc25) // 2,  # Centralizar na horizontal
    (spr_atual_npc25.get_height() - hitbox_altura_npc25) // 2 + ajuste_vertical_npc25,  # Centralizar na vertical com ajuste
    hitbox_largura_npc25,
    hitbox_altura_npc25
)
