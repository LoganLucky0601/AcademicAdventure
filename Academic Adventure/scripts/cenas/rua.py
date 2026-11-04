import pygame
from scripts.entidades import *

# scene 3: Rua
rua = pygame.image.load("assets/img/scenes/rua/rua.jpg")
cercaleft = pygame.image.load("assets/img/scenes/rua/cercaleft.png")
cercaright = pygame.image.load("assets/img/scenes/rua/cercaright.png")

LARGURA = 750  # Exemplo de largura
ALTURA = 100   # Exemplo de altura

cercaleft = pygame.transform.scale(cercaleft, (LARGURA, ALTURA))
cercaright = pygame.transform.scale(cercaright, (LARGURA, ALTURA))

hitboxes_rua = [
 # JARDINS
    pygame.Rect(0, 0, 620, 665),  # jardim esquerdo
    pygame.Rect(1180, 0, 740, 665),  # jardim direita
# PAREDES CENTRAIS
    pygame.Rect(620, 0, 200, 325),  # parede central esquerda
    pygame.Rect(990, 0, 200, 325), # parede central direita
    
# PILASTRAS
    pygame.Rect(820, 305, 45, 90),  # pilastra esquerda
    pygame.Rect(947, 305, 45, 90),  # pilastra direita
    
# LIMITES DA CENA
    pygame.Rect(0, 700, 1, 1080),  # limite esquerdo
    pygame.Rect(1920, 700, 1, 1080),  # limite direita
    pygame.Rect(0, 860, 1920, 1)  # limite inferior
]

# PORTA DE ENTRADA DO SENAC (VARIÁVEL INTERATIVA)
entrada_senac = pygame.Rect(865, 250, 76, 70)
entrando_senac_x = 75
entrando_senac_y = 792

# LISTAS DOS NPCS E AUTOMÓVEIS DA CENA RUA
npcs_rua = [npc1, npc2, npc4, npc5, npc6, npc7, npc8, npc9, 
            npc10, npc11, npc16, npc15, npc17, npc18, npc19, npc20, 
            npc21, npc22, npc23]

# alunos: npc1
'''npc5
npc8
npc9
npc10
npc11
npc17
npc22'''


carros_rua = [carro0, carro1, carro2, carro3, 
              carro4, carro5, carro6, 
              carro7, carro8, carro9, 
              carro10, carro11, carro12, 
              carro13, carro14, carro15,
              carro16, carro17, carro18,
              carro19, carro20, moto1,
              ]




mesa_antonio = pygame.image.load("assets/img/scenes/rua/mesa_antonio.png")
mesa_antonio = pygame.transform.scale(mesa_antonio, (90, 90))
antonio = pygame.image.load("assets/sprites/andantes/antonio/antonio.png")




