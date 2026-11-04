import pygame
from scripts.settings import screen  # Importa o objeto "screen" que representa a tela onde tudo será renderizado.

# Classe responsável por implementar o sistema de movimentação das entidades non-player-character (NPC).
class NPC:
    def __init__(self, npc_x, npc_y, velocidade_npc, limite_esquerda, limite_direita, animacoes, direcao):
        # Inicializa as variáveis de posição do NPC.
        self.npc_x = npc_x  # Posição X inicial do NPC.
        self.npc_y = npc_y  # Posição Y inicial do NPC.
        
        # Configuração de velocidade e limites de movimento.
        self.velocidade_npc = velocidade_npc  # Velocidade de movimentação do NPC.
        self.limite_esquerda = limite_esquerda  # Limite esquerdo para o movimento.
        self.limite_direita = limite_direita  # Limite direito para o movimento.
        
        # Configuração de animação.
        self.animacoes = animacoes  # Um dicionário contendo as animações do NPC (sprites para cada direção).
        self.direcao = direcao  # Direção inicial do NPC ("cima", "baixo", "esquerda" e "direita").
        self.spr_atual = self.animacoes[direcao][0]  # Sprite inicial baseado na direção inicial.

        # Define o retângulo de colisão do NPC.
        self.rect = pygame.Rect(npc_x, npc_y, 0, 0)  # Rect com largura e altura temporariamente definidas como 0.
        self.rect.width = self.spr_atual.get_width()  # Ajusta a largura do rect com base no sprite inicial.
        self.rect.height = self.spr_atual.get_height()  # Ajusta a altura do rect com base no sprite inicial.

        # Configura o controle da animação.
        self.contagem_tempo = 0  # Contador para controlar o tempo entre os frames da animação.
        self.indice_sprite = 0  # Índice do sprite atual na animação.
        self.velocidade_animacao = 10  # Velocidade de troca dos frames da animação (menor valor = troca mais rápida).

        # Controle de estado do NPC.
        self.ativo = True  # Define se o NPC está ativo. Se "False", ele para de se mover e ser renderizado.

    def mover_npc(self):
        # Verifica se o NPC está ativo antes de atualizá-lo.
        if not self.ativo:
            return  # Não faz nada se o NPC estiver inativo.

        # Atualiza a posição e a animação do NPC com base na direção.
        if self.direcao == "esquerda":
            self.npc_x -= self.velocidade_npc  # Move o NPC para a esquerda.
            self.spr_atual = self.animacoes["esquerda"][self.indice_sprite]  # Atualiza o sprite para o movimento.
            if self.npc_x < self.limite_esquerda:  # Se ultrapassar o limite esquerdo:
                self.direcao = "cima"  # Muda a direção para cima.

        elif self.direcao == "direita":
            self.npc_x += self.velocidade_npc  # Move o NPC para a direita.
            self.spr_atual = self.animacoes["direita"][self.indice_sprite]  # Atualiza o sprite para o movimento.
            if self.npc_x > self.limite_direita:  # Se ultrapassar o limite direito:
                self.direcao = "cima"  # Muda a direção para cima.

        elif self.direcao == "cima":
            self.npc_y -= self.velocidade_npc  # Move o NPC para cima.
            self.spr_atual = self.animacoes["cima"][self.indice_sprite]  # Atualiza o sprite para o movimento.

        elif self.direcao == "idle":  # Caso o NPC esteja parado:
            self.spr_atual = self.animacoes["idle"][self.indice_sprite]  # Mostra o sprite de inatividade.
            self.velocidade_npc = 0  # Define a velocidade como 0 para garantir que não se mova.

        # Controle de animação - atualiza o índice do sprite com base no tempo.
        self.contagem_tempo += 1
        if self.contagem_tempo >= self.velocidade_animacao:  # Se o contador atingir o limite da velocidade:
            self.contagem_tempo = 0  # Reseta o contador.
            # Atualiza o índice para o próximo sprite na lista, voltando ao início quando chegar no final.
            self.indice_sprite = (self.indice_sprite + 1) % len(self.animacoes[self.direcao])

        # Atualiza o retângulo do NPC para corresponder à nova posição.
        self.rect.x = self.npc_x
        self.rect.y = self.npc_y

# Função para verificar se um NPC entrou em uma área específica.
def verificar_entrada_npc(npc, entrada_rect, screen):
    # Atualiza a posição do retângulo de colisão do NPC.
    npc.rect.x = npc.npc_x
    npc.rect.y = npc.npc_y

    # Verifica se o retângulo do NPC colide com o retângulo de entrada.
    if npc.ativo and npc.rect.colliderect(entrada_rect):  # Se o NPC colidiu:
        npc.ativo = False  # Define o NPC como inativo, impedindo que ele se mova ou seja desenhado.
        return True  # Retorna "True" indicando que o NPC entrou na área.

    # Renderiza o NPC na tela, mas apenas se ele estiver ativo.
    if npc.ativo:
        screen.blit(npc.spr_atual, (npc.rect.x, npc.rect.y))  # Desenha o sprite atual do NPC na tela.

    return False  # Retorna "False" caso o NPC não tenha colidido com a área.

# Função para desenhar um NPC na tela.
def desenhar_npc(npc):
    screen.blit(npc.spr_atual, (npc.npc_x, npc.npc_y))  # Desenha o sprite atual do NPC na posição correspondente.

