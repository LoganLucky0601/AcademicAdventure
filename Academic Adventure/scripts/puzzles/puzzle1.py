import pygame
import time
from scripts.font import *

# Mouse
class Mouse:
    def __init__(self):
        self.click = False

    def atualizar(self, event):
        # Atualiza a posição do mouse e retângulo baseado nela
        self.mouse_pos = pygame.mouse.get_pos()
        self.x, self.y = 0,0
        self.mouse = pygame.Rect(self.x, self.y, 1, 1)
        

        self.Interacao(event)

    def Interacao(self, event):
        
        # Verifica se o mouse colide com uma área e se houve clique
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self.x, self.y = self.mouse_pos
            self.mouse = pygame.Rect(self.x, self.y, 1, 1)
            print(self.x, self.y)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.click = False
            
img_fase1 = [
    'assets/puzzle1/fundo.png',
    'assets/puzzle1/item_fundo.png',
]
img_pecas = [
    'assets/puzzle1/gabinete.png',
    'assets/puzzle1/hd.png',
    'assets/puzzle1/memoria.png',
    'assets/puzzle1/monitor.png',
    'assets/puzzle1/motherboard.png',
    'assets/puzzle1/fonte.png',
    'assets/puzzle1/processador.png',
    'assets/puzzle1/gpu.png'
]

perguntas = [
    'Qual o dispositivo responsável por armazenar os dados?',
    'Dispositivo responsável pela conexão das peças',
    'Peça responsável por calcular e processar dados',
    'Processa gráficos e vídeos para exibição na tela',
    'Dispositivo responsável por fornecer energia elétrica para os componentes',
    'Exibe as informações visuais do computador para o usuário.',
    'Protege e guarda fisicamente os componentes.',
    'Responsável pelo armazenamento temporário de dados.',

]
inf_1 = [
    'Gabinete:',
    '- A "caixa" onde ficam todas as peças do computador.',
    '- Protege os componentes e ajuda a manter tudo organizado.',

    'HD:',
    '- Dispositivo de armazenamento tradicional.',
    '- É onde os arquivos e programas ficam armazenados permanentemente.',

    'Memória RAM (Memória de Acesso Aleatório):',
    '- Memória volátil, usada para agilizar a execução de tarefas.',
    '- Armazena temporariamente os dados que estão sendo executados. ',
]
inf_2 = [
    'Monitor:',
    '- Tela que exibe as informações processadas pelo computador.',
    '- Permite que o usuário visualize gráficos, textos e vídeos.',

    'Placa-mãe:',
    '- A principal placa de circuito do computador.',
    '- Ela permite a conexão e a comunicação de todos os componetes.',

    'Fonte de alimentação:',
    '- Dispositivo responsável por fornecer energia elétrica.',
    '- Fontes de boa qualidade são essenciais para a durabilidade.',
    
]
    
inf_3 = [
    'Processador (CPU):',
    '- Unidade Central de Processamento, o "cérebro" do computador.',
    '- Responsável pelo desempenho geral das tarefas, executando cálculos.',
    
    'Placa de vídeo (GPU):',
    '- Componente dedicado ao processamento das imagens e gráficos.',
    '- Essencial para jogos e vídeos de alta qualidade.',

    'HD:',
    '- Dispositivo de armazenamento tradicional.',
    '- É onde os arquivos e programas ficam armazenados permanentemente.',
]

inf_4 = [
    'Memória RAM (Memória de Acesso Aleatório):',
    '- Memória volátil, usada para agilizar a execução de tarefas.',
    '- Armazena temporariamente os dados que estão sendo executados. ',
    
    'Fonte de alimentação:',
    '- Dispositivo responsável por fornecer energia elétrica.',
    '- Fontes de boa qualidade são essenciais para a durabilidade.',

    'Placa de vídeo (GPU):',
    '- Componente dedicado ao processamento das imagens e gráficos.',
    '- Essencial para jogos e vídeos de alta qualidade.',
]
inf_5 = [
    'Fonte de alimentação:',
    '- Dispositivo responsável por fornecer energia elétrica.',
    '- Fontes de boa qualidade são essenciais para a durabilidade.',
    
    'Processador (CPU):',
    '- Unidade Central de Processamento, o "cérebro" do computador.',
    '- Responsável pelo desempenho geral das tarefas, executando cálculos.',

    'Gabinete:',
    '- A "caixa" onde ficam todas as peças do computador.',
    '- Protege os componentes e ajuda a manter tudo organizado.',

]
inf_6 = [
    'Monitor:',
    '- Tela que exibe as informações processadas pelo computador.',
    '- Permite que o usuário visualize gráficos, textos e vídeos.',
    
    'Placa-mãe:',
    '- A principal placa de circuito do computador.',
    '- Ela permite a conexão e a comunicação de todos os componetes.',

    'HD:',
    '- Dispositivo de armazenamento tradicional.',
    '- É onde os arquivos e programas ficam armazenados permanentemente.',

]
inf_7 = [
    'Monitor:',
    '- Tela que exibe as informações processadas pelo computador.',
    '- Permite que o usuário visualize gráficos, textos e vídeos.',
    
    'Placa de vídeo (GPU):',
    '- Componente dedicado ao processamento das imagens e gráficos.',
    '- Essencial para jogos e vídeos de alta qualidade.',

    'Gabinete:',
    '- A "caixa" onde ficam todas as peças do computador.',
    '- Protege os componentes e ajuda a manter tudo organizado.',

]
inf_8 = [
    'Processador (CPU):',
    '- Unidade Central de Processamento, o "cérebro" do computador.',
    '- Responsável pelo desempenho geral das tarefas, executando cálculos.',
    
    'Memória RAM (Memória de Acesso Aleatório):',
    '- Memória volátil, usada para agilizar a execução de tarefas.',
    '- Armazena temporariamente os dados que estão sendo executados.',

    'HD:',
    '- Dispositivo de armazenamento tradicional.',
    '- É onde os arquivos e programas ficam armazenados permanentemente.',

]

inf_geral = [
    inf_1,
    inf_2,
    inf_3,
    inf_4,
    inf_5,
    inf_6,
    inf_7,
    inf_8,
]

# Função para desenhar a animação de texto

class Inter_Geral:
    def __init__(self, obj1, obj2, obj3, res, per, inf):
        pygame.init()
        self.display = pygame.display.get_surface()
        self.fundo = pygame.transform.scale(pygame.image.load(img_fase1[0]), (1920, 1080))
        self.mouse = Mouse()
        self.lista_inf = inf
        self.ind_inf = per
        self.prox_fase = 1
        self.area_clicada = 0
        self.infs = ' '
        self.font = pygame.font.Font("assets/fonts/PixelifySansRegular.ttf", 40)
        self.text = self.font.render(perguntas[per], True, 'black')
        self.acertou = False
        self.resposta = res

        self.rect_1 = pygame.Rect(325, 260, 320, 261)
        self.rect_2 = pygame.Rect(800, 260, 320, 261)
        self.rect_3 = pygame.Rect(1275, 260, 320, 261)
        self.rect_4 = pygame.Rect(0,0,0,0)

        self.peca_1 = pygame.transform.scale(pygame.image.load(img_pecas[obj1]), (320, 250))
        self.peca_2 = pygame.transform.scale(pygame.image.load(img_pecas[obj2]), (320, 250))
        self.peca_3 = pygame.transform.scale(pygame.image.load(img_pecas[obj3]), (320, 250))
        

        self.area_text = pygame.transform.scale(pygame.image.load(img_fase1[1]), (1600, 270))
        
        self.text_inf_1 = self.font.render('', True, 'black')
        self.text_inf_2 = self.font.render('', True, 'black')
        self.text_inf_3 = self.font.render(' ', True, 'black')
        self.text_inf_4 = self.font.render('', True, 'black')
        self.text_inf_5 = self.font.render('', True, 'black')

        self.rect_4 = pygame.Rect(0,0,0,0)

    def desenhar(self, surface):
        
        surface.blit(self.fundo, (0,0))
        surface.blit(self.text, (300, 120))
        surface.blit(self.peca_1, (325, 260))
        surface.blit(self.peca_2, (800, 260))
        surface.blit(self.peca_3, (1275, 260))

        '''pygame.draw.rect(surface, 'red', self.rect_1)
        pygame.draw.rect(surface, 'red', self.rect_2)
        pygame.draw.rect(surface, 'red', self.rect_3)
        pygame.draw.rect(surface, 'red', self.rect_4)'''

        surface.blit(self.area_text, (150,630))
        surface.blit(self.text_inf_1, (250, 680))
        surface.blit(self.text_inf_2, (250, 680 + 60))
        surface.blit(self.text_inf_3, (250, 680 + 60 + 60))
        surface.blit(self.text_inf_4, (300, 120 + 60))

    def verificar(self, res):
        if self.resposta == res:
                self.passou()
                self.prox_fase += 1
        else:
            self.text_inf_4 = self.font.render('Não é essa peça...', True, 'red')
               
    def passou(self):
        time.sleep(0.2)
        self.rect_4 = pygame.Rect(0, 0, 1920, 1080)
        self.text_inf_4 = self.font.render('ACERTOU! - clique em algo para continuar...', True, (0, 255, 0))

    def colidiu(self, rect, x, i1, i2, i3):
        if self.mouse.mouse.colliderect(rect) and self.area_clicada != x:
            self.area_clicada = x

            self.text_inf_1 = self.font.render(self.lista_inf[self.ind_inf][i1], True, 'black')
            self.text_inf_2 = self.font.render(self.lista_inf[self.ind_inf][i2], True, 'black')
            self.text_inf_3 = self.font.render(self.lista_inf[self.ind_inf][i3], True, 'black')

            if self.mouse.mouse.colliderect(self.rect_4) and self.mouse.click:
                self.prox_fase += 1

            self.verificar(x)


    def events(self, event):
        self.mouse.atualizar(event)
        self.colidiu(self.rect_1, 1, 0,1,2)
        self.colidiu(self.rect_2, 2, 3,4,5)
        self.colidiu(self.rect_3, 3, 6,7,8)
        if self.mouse.mouse.colliderect(self.rect_4) and self.mouse.click:
            self.prox_fase += 1
        elif self.prox_fase > 3:
            self.acertou = True

    def executar(self, root, event):
        self.events(event)
        self.desenhar(root)


# Inicializar a variável de controle do puzzle
dialogo1_concluido = False
puzzle1_ativo = False  # Indica se o puzzle está ativo ou não
puzzle1_concluido = False


fase1 = Inter_Geral(0,1,2, 2, 0, inf_geral) #resposta certa opção 2º - hd
fase2 = Inter_Geral(3,4,5, 2, 1, inf_geral) #resposta certa opção 3º - placa de video
fase3 = Inter_Geral(6,7,1, 1, 2, inf_geral) #resposta certa opção 1º - processador
fase4 = Inter_Geral(2,5,7, 3, 3, inf_geral) #resposta certa opção 2º - hd
fase5 = Inter_Geral(5,6,0, 1, 4, inf_geral) #resposta certa opção 3º - placa de video
fase6 = Inter_Geral(3,4,1, 1, 5, inf_geral) #resposta certa opção 1º - processador
fase7 = Inter_Geral(3,7,0, 3, 6, inf_geral) #resposta certa opção 2º - hd
fase8 = Inter_Geral(6,2,1, 2, 7, inf_geral) #resposta certa opção 3º - placa de video

def puzzle1_executar(root, event):
    if not fase1.acertou:
        fase1.executar(root, event)
    elif not fase2.acertou:
        fase2.executar(root, event)
    elif not fase3.acertou:
        fase3.executar(root, event)
    elif not fase4.acertou:
        fase4.executar(root, event)
    elif not fase5.acertou:
        fase5.executar(root, event)
    elif not fase6.acertou:
        fase6.executar(root, event)
    elif not fase7.acertou:
        fase7.executar(root, event)
    elif not fase8.acertou:
        fase8.executar(root, event)
        root.fill((0,0,0,0))
