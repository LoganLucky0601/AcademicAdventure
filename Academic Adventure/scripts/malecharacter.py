import pygame

# Classe responsável por implementar o sistema de movimentação do personagem jogável.
class MaleCharacter:

    def __init__(self, x, y, velocidade, velocidade_animacao):
        # Inicialização das posições do personagem.
        self.x = x  # Coordenada inicial no eixo X (horizontal).
        self.y = y  # Coordenada inicial no eixo Y (vertical).
        self.novo_x = x  # Posição temporária usada para calcular a nova posição no eixo X.
        self.novo_y = y  # Posição temporária usada para calcular a nova posição no eixo Y.

        # Inicialização de parâmetros de movimentação.
        self.velocidade = velocidade  # Velocidade de deslocamento do personagem.
        self.velocidade_animacao = velocidade_animacao  # Frequência da troca de sprites na animação.
        self.contagem_tempo = 0  # Contador para gerenciar o tempo entre trocas de sprites.
        self.indice_sprite = 0  # Índice do sprite atual usado na animação.
        self.direcao = "idle"  # Direção atual do personagem ("idle" indica que está parado).
        self.ultima_direcao = "idle"  # Guarda a última direção antes do personagem ficar parado.

        # Carregamento dos sprites do personagem para cada direção de movimento.
        self.sprites_cima = [
            pygame.image.load("assets/sprites/mainchar/top1.png"),
            pygame.image.load("assets/sprites/mainchar/top2.png"),
            pygame.image.load("assets/sprites/mainchar/top3.png"),
            pygame.image.load("assets/sprites/mainchar/top4.png")
        ]

        self.sprites_baixo = [
            pygame.image.load("assets/sprites/mainchar/bottom1.png"),
            pygame.image.load("assets/sprites/mainchar/bottom2.png"),
            pygame.image.load("assets/sprites/mainchar/bottom3.png"),
            pygame.image.load("assets/sprites/mainchar/bottom4.png")
        ]

        self.sprites_esquerda = [
            pygame.image.load("assets/sprites/mainchar/left1.png"),
            pygame.image.load("assets/sprites/mainchar/left2.png"),
            pygame.image.load("assets/sprites/mainchar/left3.png"),
            pygame.image.load("assets/sprites/mainchar/left4.png")
        ]

        self.sprites_direita = [
            pygame.image.load("assets/sprites/mainchar/right1.png"),
            pygame.image.load("assets/sprites/mainchar/right2.png"),
            pygame.image.load("assets/sprites/mainchar/right3.png"),
            pygame.image.load("assets/sprites/mainchar/right4.png")
        ]

        # Sprite para o estado parado (idle).
        self.sprite_idle = pygame.image.load("assets/sprites/mainchar/idle.png")
        self.sprite_atual = self.sprite_idle  # O sprite inicial é o "idle".

        # Dimensões da hitbox do personagem.
        self.hitbox_largura = 50  # Largura da hitbox.
        self.hitbox_altura = 60  # Altura da hitbox.
        self.ajuste_vertical = 30  # Ajuste vertical para posicionar a hitbox corretamente.

        # Criação da hitbox inicial baseada na posição e dimensões.
        self.hitbox = pygame.Rect(
            self.novo_x + (self.sprite_atual.get_width() - self.hitbox_largura) // 2,  # Centraliza a hitbox no eixo X.
            self.novo_y + (self.sprite_atual.get_height() - self.hitbox_altura) // 2 + self.ajuste_vertical,  # Ajusta no eixo Y.
            self.hitbox_largura,  # Define a largura.
            self.hitbox_altura  # Define a altura.
        )

    def atualizar_hitbox(self):
        """
        Atualiza a posição da hitbox com base na posição atual do personagem.
        """
        self.hitbox = pygame.Rect(
            self.x + (self.sprite_atual.get_width() - self.hitbox_largura) // 2,  # Recalcula a centralização no eixo X.
            self.y + (self.sprite_atual.get_height() - self.hitbox_altura) // 2 + self.ajuste_vertical,  # Ajusta no eixo Y.
            self.hitbox_largura,  # Mantém a largura.
            self.hitbox_altura  # Mantém a altura.
        )

    def atualizar_sprite(self):
        """
        Atualiza o sprite do personagem com base na direção do movimento.
        """
        # Seleciona os sprites de animação da direção correspondente.
        if self.direcao == "direita":
            self.sprite_atual = self.sprites_direita[self.indice_sprite]
        elif self.direcao == "esquerda":
            self.sprite_atual = self.sprites_esquerda[self.indice_sprite]
        elif self.direcao == "cima":
            self.sprite_atual = self.sprites_cima[self.indice_sprite]
        elif self.direcao == "baixo":
            self.sprite_atual = self.sprites_baixo[self.indice_sprite]
        else:  # Caso o personagem esteja parado (idle).
            if self.ultima_direcao == "cima":
                self.sprite_atual = self.sprites_cima[0]
            elif self.ultima_direcao == "baixo":
                self.sprite_atual = self.sprites_baixo[0]
            elif self.ultima_direcao == "esquerda":
                self.sprite_atual = self.sprites_esquerda[0]
            elif self.ultima_direcao == "direita":
                self.sprite_atual = self.sprites_direita[0]

        # Gerencia a troca de sprites na animação enquanto o personagem se move.
        if self.direcao != "idle":
            self.contagem_tempo += 1  # Incrementa o contador de tempo.
            if self.contagem_tempo >= self.velocidade_animacao:  # Verifica se é hora de trocar o sprite.
                self.contagem_tempo = 0  # Reseta o contador.
                self.indice_sprite = (self.indice_sprite + 1) % 4  # Alterna entre os 4 sprites de animação.

        # Atualiza a última direção se o personagem estiver se movendo.
        if self.direcao != "idle":
            self.ultima_direcao = self.direcao

    def mover(self, teclas):
        """
        Atualiza a posição do personagem com base nas teclas pressionadas.
        """
        self.novo_x, self.novo_y = self.x, self.y  # Armazena as posições anteriores.

        # Detecta teclas pressionadas para ajustar a posição e direção do personagem.
        if teclas[pygame.K_UP]:  # Movimento para cima.
            self.novo_y -= self.velocidade
            self.direcao = "cima"
        elif teclas[pygame.K_DOWN]:  # Movimento para baixo.
            self.novo_y += self.velocidade
            self.direcao = "baixo"
        elif teclas[pygame.K_LEFT]:  # Movimento para a esquerda.
            self.novo_x -= self.velocidade
            self.direcao = "esquerda"
        elif teclas[pygame.K_RIGHT]:  # Movimento para a direita.
            self.novo_x += self.velocidade
            self.direcao = "direita"
        else:  # Caso nenhuma tecla seja pressionada.
            self.direcao = "idle"

        # Atualiza o sprite com base na direção.
        self.atualizar_sprite()

        # Atualiza as posições confirmando o movimento.
        self.x, self.y = self.novo_x, self.novo_y

        # Atualiza a hitbox com a nova posição.
        self.atualizar_hitbox()

    def desenhar_mainchar(self, screen):
        """
        Desenha o personagem na tela usando o sprite atual.
        """
        screen.blit(self.sprite_atual, (self.x, self.y))  # Desenha o sprite do personagem.
        # Opcional: desenha a hitbox em vermelho para debug.
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def teleportar(self, mouse_pos):
        """
        Move instantaneamente o personagem para a posição especificada.
        """
        self.x, self.y = mouse_pos  # Define novas coordenadas.
        self.atualizar_hitbox()  # Atualiza a hitbox com a nova posição.


