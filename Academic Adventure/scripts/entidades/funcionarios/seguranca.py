import pygame
import random
from scripts.cenas.terreo import *

'''A classe Load_Sprite_Npc originalmente foi criada para implementar um sistema de movimentação randômica
para determinado grupo de NPCs. A movimentação do segurança, por ser apenas linear, fez com que fosse necessário
realizar mudanças na estrutura da classe. Então foi criada a classe Load_Sprite_Npc_Seguranca.'''

# Sprites do segurança em várias direções
spr_esquerda_seguranca = [
    "assets/sprites/funcionarios/seguranca/left1.png",
    "assets/sprites/funcionarios/seguranca/left2.png",
    "assets/sprites/funcionarios/seguranca/left3.png",
    "assets/sprites/funcionarios/seguranca/left4.png"
]

spr_direita_seguranca = [
    "assets/sprites/funcionarios/seguranca/right1.png",
    "assets/sprites/funcionarios/seguranca/right2.png",
    "assets/sprites/funcionarios/seguranca/right3.png",
    "assets/sprites/funcionarios/seguranca/right4.png"
]

spr_parado_seguranca = "assets/sprites/funcionarios/seguranca/idle.png"

# Lista com os diferentes estados de animação do segurança
gp_spr = [
    spr_parado_seguranca,
    spr_direita_seguranca,
    spr_esquerda_seguranca  
]

class Load_Sprite_Npc_Seguranca:
    def __init__(self, list, lis_piso):
        '''Construtor que inicializa a classe de movimentação do segurança'''
        self.piso = lis_piso  # Lista de hitboxes do piso
        self.list = list  # Lista de sprites do NPC
        self.width = 95  # Largura do sprite
        self.height = 110  # Altura do sprite
        self.tamanho = 90  # Tamanho do NPC
        self.frame_delay = 10  # Delay entre os quadros da animação
        self.frame_count = 0  # Contador de quadros
        self.time_limite = random.randint(100, 200)  # Intervalo de tempo aleatório para mudar a direção
        self.vel = 2  # Velocidade de movimento do segurança
        self.cont = 0  # Contador de tempo para a mudança de direção
        self.ind = 0  # Índice de animação
        self.andar = True  # Indica se o NPC está se movendo
        self.andar_direita = True  # Indica se o NPC pode mover para a direita
        self.andar_esqueda = True  # Indica se o NPC pode mover para a esquerda
        self.list_mov = ['parado', 'direita', 'esquerda']  # Lista de estados de movimento
        self.direcao_atual = random.choice(self.list_mov)  # Direção inicial aleatória
        self.img = pygame.transform.scale(pygame.image.load(self.list[0]), (self.width, self.height))  # Carrega o sprite inicial
        self.pos_x, self.pos_y = 290, 650  # Define a posição inicial do segurança (fixa)
        self.rect = self.img.get_rect(topleft=[self.pos_x, self.pos_y])  # Retângulo para colisão
        self.hit_cima = pygame.Rect(self.pos_x, self.pos_y, self.tamanho, 1)  # Hitbox superior
        self.hit_baixo = pygame.Rect(self.pos_x, (self.pos_y + self.tamanho), self.tamanho, 1)  # Hitbox inferior
        self.hit_esquerda = pygame.Rect(self.pos_x, self.pos_y, 1, self.tamanho)  # Hitbox esquerda
        self.hit_direita = pygame.Rect((self.pos_x + self.tamanho), self.pos_y, 1, self.tamanho)  # Hitbox direita

    def draw(self, surface): 
        '''Desenha o NPC na tela'''
        surface.blit(self.img, self.rect)
        #pygame.draw.rect(surface, (255, 0, 0), self.hit_cima)
        #pygame.draw.rect(surface, (255, 0, 0), self.hit_baixo)
        #pygame.draw.rect(surface, (255, 0, 0), self.hit_direita)
        #pygame.draw.rect(surface, (255, 0, 0), self.hit_esquerda)

    def desenhar_seguranca(self, root):
        '''Atualiza e desenha o segurança'''
        self.update()  # Atualiza as animações
        self.draw(root)  # Desenha o NPC na tela

    def update(self):
        '''Atualiza o estado do segurança, incluindo tempo e animação'''
        self.time()  # Atualiza a direção aleatória com base no tempo
        self.up_img()  # Atualiza a imagem do sprite

    def hitbox(self):
        '''Atualiza as hitboxes do segurança para verificar colisões'''
        self.hit_cima = pygame.Rect((self.pos_x + 15), self.pos_y, (self.tamanho - 30), 1)
        self.hit_baixo = pygame.Rect((self.pos_x + 15), (self.pos_y + self.tamanho), (self.tamanho - 30), 1)
        self.hit_esquerda = pygame.Rect(self.pos_x, (self.pos_y + 15), 1, (self.tamanho - 30))
        self.hit_direita = pygame.Rect((self.pos_x + self.tamanho), (self.pos_y + 15), 1, (self.tamanho - 30))

    def colisao(self):
        '''Verifica colisões do segurança com o piso'''
        # Redefine as variáveis de direção para poder verificar colisões
        self.andar_direita = True
        self.andar_esqueda = True

        # Verifica colisões com as hitboxes do piso
        for rect in self.piso:
            if self.hit_esquerda.colliderect(rect):
                self.andar_esqueda = False  # Não pode mover para a esquerda
            if self.hit_direita.colliderect(rect):
                self.andar_direita = False  # Não pode mover para a direita

    def movimento(self):
        '''Define a movimentação do segurança, incluindo colisões e direções'''
        self.hitbox()  # Atualiza as hitboxes
        self.colisao()  # Verifica as colisões

        # Se a direção atual for "direita", move para a direita
        if self.direcao_atual == 'direita':
            if self.pos_x < 1920 and self.andar_direita:  # Limite da tela
                self.pos_x += self.vel

        # Se a direção atual for "esquerda", move para a esquerda
        if self.direcao_atual == 'esquerda':
            if self.pos_x > 0 and self.andar_esqueda:  # Limite da tela
                self.pos_x -= self.vel

    def time(self):
        '''Muda a direção do NPC após um tempo aleatório'''
        self.cont += 1
        if self.cont > self.time_limite:  # Verifica se o tempo limite foi atingido
            self.time_limite = random.randint(100, 150)  # Gera um novo tempo limite aleatório
            self.direcao_atual = random.choice(self.list_mov)  # Muda a direção aleatoriamente
            self.cont = 0  # Reseta o contador de tempo

    def up_img(self):
        '''Atualiza a imagem do sprite de acordo com a direção e a animação'''
        self.movimento()  # Atualiza o movimento do NPC
        self.frame_count += 1  # Incrementa o contador de quadros
        if self.frame_count >= self.frame_delay:  # Se atingiu o tempo para mudar de quadro
            self.frame_count = 0  # Reseta o contador de quadros
            self.ind += 1  # Avança para o próximo quadro
            if self.ind >= 4:  # Se passou do número de quadros, reseta
                self.ind = 0

        # Atualiza o sprite dependendo da direção do NPC
        if self.direcao_atual == 'parado':
            self.img = pygame.transform.scale(pygame.image.load(self.list[0]), (self.width, self.height))
            self.rect = self.img.get_rect(topleft=[self.pos_x, self.pos_y])

        elif self.direcao_atual == 'direita':
            if self.andar_direita:  # Se pode andar para a direita, usa o sprite correspondente
                self.img = pygame.transform.scale(pygame.image.load(self.list[1][self.ind]), (self.width, self.height))
                self.rect = self.img.get_rect(topleft=[self.pos_x, self.pos_y])
            else:
                self.img = pygame.transform.scale(pygame.image.load(self.list[0]), (self.width, self.height))
                self.rect = self.img.get_rect(topleft=[self.pos_x, self.pos_y])

        elif self.direcao_atual == 'esquerda':
            if self.andar_esqueda:  # Se pode andar para a esquerda, usa o sprite correspondente
                self.img = pygame.transform.scale(pygame.image.load(self.list[2][self.ind]), (self.width, self.height))
                self.rect = self.img.get_rect(topleft=[self.pos_x, self.pos_y])
            else:
                self.img = pygame.transform.scale(pygame.image.load(self.list[0]), (self.width, self.height))
                self.rect = self.img.get_rect(topleft=[self.pos_x, self.pos_y])

# Criação do NPC de segurança
seguranca_npc = Load_Sprite_Npc_Seguranca(gp_spr, hitboxes_terreo)
