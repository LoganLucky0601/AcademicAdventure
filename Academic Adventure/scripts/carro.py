import pygame
from scripts.settings import screen

# Classe responsável por implementar o sistema de movimentação dos Carros presentes na cena RUA.

class Carro:
    def __init__(self, carro_x, carro_y, velocidade_carro, limite_esquerda, limite_direita, animacoes, direcao):
        # Inicializa a posição do carro, velocidade, limites de movimento, animações e direção
        self.carro_x = carro_x  # Posição inicial do carro no eixo X (horizontal)
        self.carro_y = carro_y  # Posição inicial do carro no eixo Y (vertical)
        self.velocidade_carro = velocidade_carro  # Velocidade com que o carro se move
        self.limite_esquerda = limite_esquerda  # Limite mínimo no eixo X (esquerda) para o movimento do carro
        self.limite_direita = limite_direita  # Limite máximo no eixo X (direita) para o movimento do carro
        self.animacoes = animacoes  # Dicionário com animações do carro em diferentes direções
        self.direcao = direcao  # Direção inicial do movimento do carro
        self.rect = pygame.Rect(carro_x, carro_y, 0, 0)  # Inicializa o retângulo de colisão (hitbox) do carro
        self.contagem_tempo = 0  # Contador para controlar a animação do carro
        self.indice_sprite = 0  # Índice do sprite atual do carro para animação
        self.velocidade_animacao = 10  # Controla a velocidade da animação (quanto menor, mais rápido)
        self.spr_atual = self.animacoes[direcao][0]  # Sprite inicial do carro de acordo com a direção

        # Atualiza o tamanho do retângulo de colisão (hitbox) com base no tamanho do sprite inicial
        self.rect.width = self.spr_atual.get_width()  # Define a largura do retângulo de colisão
        self.rect.height = self.spr_atual.get_height()  # Define a altura do retângulo de colisão

        # Flag para controlar se o carro está ativo ou não
        self.ativo = True

    def mover_carro(self):
        # Atualiza a posição do carro com base na direção atual
        if self.direcao == "esquerda":
            self.carro_x -= self.velocidade_carro  # Move o carro para a esquerda
            self.spr_atual = self.animacoes["esquerda"][self.indice_sprite]  # Atualiza o sprite do carro para a direção esquerda
            if self.carro_x < self.limite_esquerda:  # Se o carro atingir o limite esquerdo, muda a direção para cima
                self.direcao = "cima"
        
        elif self.direcao == "direita":
            self.carro_x += self.velocidade_carro  # Move o carro para a direita
            self.spr_atual = self.animacoes["direita"][self.indice_sprite]  # Atualiza o sprite do carro para a direção direita
        
        elif self.direcao == "parado":
            self.spr_atual = self.animacoes["parado"][self.indice_sprite]  # Atualiza o sprite do carro
        
        # Atualiza a animação do carro
        self.contagem_tempo += 1  # Incrementa o contador de tempo para animação
        if self.contagem_tempo >= self.velocidade_animacao:  # Quando o contador atingir o valor de velocidade, troca o sprite
            self.contagem_tempo = 0  # Reseta o contador
            self.indice_sprite = (self.indice_sprite + 1) % len(self.animacoes[self.direcao])  # Avança para o próximo sprite na direção atual

        # Atualiza a posição do retângulo de colisão (hitbox) com base na posição do carro
        self.rect.x = self.carro_x
        self.rect.y = self.carro_y  # Atualiza a coordenada Y da hitbox com a nova posição do carro
    
def desenhar_carro(carro):
    # Função responsável por desenhar o carro na tela
    screen.blit(carro.spr_atual, (carro.carro_x, carro.carro_y))  # Desenha o sprite atual do carro na tela nas coordenadas (carro_x, carro_y)
