import pygame
from scripts.settings import screen  # Importa o objeto "screen" que representa a tela onde tudo será renderizado.

# Classe responsável por implementar o sistema de movimentação das entidades non-player-character (modelo).
class Modelo:
    def __init__(self, modelo_x, modelo_y, velocidade_modelo, limite_esquerda, limite_direita, animacoes, direcao):
        # Inicializa as variáveis de posição do modelo.
        self.modelo_x = modelo_x  # Posição X inicial do modelo.
        self.modelo_y = modelo_y  # Posição Y inicial do modelo.
        
        # Configuração de velocidade e limites de movimento.
        self.velocidade_modelo = velocidade_modelo  # Velocidade de movimentação do modelo.
        self.limite_esquerda = limite_esquerda  # Limite esquerdo para o movimento.
        self.limite_direita = limite_direita  # Limite direito para o movimento.
        
        # Configuração de animação.
        self.animacoes = animacoes  # Um dicionário contendo as animações do modelo (sprites para cada direção).
        self.direcao = direcao  # Direção inicial do modelo ("cima", "baixo", "esquerda" e "direita").
        self.spr_atual = self.animacoes[direcao][0]  # Sprite inicial baseado na direção inicial.

        # Define o retângulo de colisão do modelo.
        self.rect = pygame.Rect(modelo_x, modelo_y, 0, 0)  # Rect com largura e altura temporariamente definidas como 0.
        self.rect.width = self.spr_atual.get_width()  # Ajusta a largura do rect com base no sprite inicial.
        self.rect.height = self.spr_atual.get_height()  # Ajusta a altura do rect com base no sprite inicial.

        # Configura o controle da animação.
        self.contagem_tempo = 0  # Contador para controlar o tempo entre os frames da animação.
        self.indice_sprite = 0  # Índice do sprite atual na animação.
        self.velocidade_animacao = 10  # Velocidade de troca dos frames da animação (menor valor = troca mais rápida).

        # Controle de estado do modelo.
        self.ativo = True  # Define se o modelo está ativo. Se "False", ele para de se mover e ser renderizado.

    def mover_modelo(self):
        # Verifica se o modelo está ativo antes de atualizá-lo.
        if not self.ativo:
            return  # Não faz nada se o modelo estiver inativo.

        # Atualiza a posição e a animação do modelo com base na direção.
        if self.direcao == "esquerda":
            self.modelo_x -= self.velocidade_modelo  # Move o modelo para a esquerda.
            self.spr_atual = self.animacoes["esquerda"][self.indice_sprite]  # Atualiza o sprite para o movimento.
            if self.modelo_x < self.limite_esquerda:  # Se ultrapassar o limite esquerdo:
                self.direcao = "cima"  # Muda a direção para cima.

        elif self.direcao == "direita":
            self.modelo_x += 0  # Move o modelo para a direita.
            self.spr_atual = self.animacoes["direita"][self.indice_sprite]  # Atualiza o sprite para o movimento.
            if self.modelo_x > self.limite_direita:  # Se ultrapassar o limite direito:
                self.direcao = "cima"  # Muda a direção para cima.

        elif self.direcao == "cima":
            self.modelo_y -= self.velocidade_modelo  # Move o modelo para cima.
            self.spr_atual = self.animacoes["cima"][self.indice_sprite]  # Atualiza o sprite para o movimento.

        elif self.direcao == "idle":  # Caso o modelo esteja parado:
            self.spr_atual = self.animacoes["idle"][self.indice_sprite]  # Mostra o sprite de inatividade.
            self.velocidade_modelo = 0  # Define a velocidade como 0 para garantir que não se mova.

        # Controle de animação - atualiza o índice do sprite com base no tempo.
        self.contagem_tempo += 1
        if self.contagem_tempo >= self.velocidade_animacao:  # Se o contador atingir o limite da velocidade:
            self.contagem_tempo = 0  # Reseta o contador.
            # Atualiza o índice para o próximo sprite na lista, voltando ao início quando chegar no final.
            self.indice_sprite = (self.indice_sprite + 1) % len(self.animacoes[self.direcao])

        # Atualiza o retângulo do modelo para corresponder à nova posição.
        self.rect.x = self.modelo_x
        self.rect.y = self.modelo_y

# Função para verificar se um modelo entrou em uma área específica.
def verificar_entrada_modelo(modelo, entrada_rect, screen):
    # Atualiza a posição do retângulo de colisão do modelo.
    modelo.rect.x = modelo.modelo_x
    modelo.rect.y = modelo.modelo_y

    # Verifica se o retângulo do modelo colide com o retângulo de entrada.
    if modelo.ativo and modelo.rect.colliderect(entrada_rect):  # Se o modelo colidiu:
        modelo.ativo = False  # Define o modelo como inativo, impedindo que ele se mova ou seja desenhado.
        return True  # Retorna "True" indicando que o modelo entrou na área.

    # Renderiza o modelo na tela, mas apenas se ele estiver ativo.
    if modelo.ativo:
        screen.blit(modelo.spr_atual, (modelo.rect.x, modelo.rect.y))  # Desenha o sprite atual do modelo na tela.

    return False  # Retorna "False" caso o modelo não tenha colidido com a área.

# Função para desenhar um modelo na tela.
def desenhar_modelo(modelo):
    screen.blit(modelo.spr_atual, (modelo.modelo_x, modelo.modelo_y))  # Desenha o sprite atual do modelo na posição correspondente.



