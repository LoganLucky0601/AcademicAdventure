import pygame

import pygame

class Mouse:
    def __init__(self):
        self.click = False
        self.x, self.y = 0,0
        self.a, self.b = 0,0
        
    def atualizar(self, event):
        # Atualiza a posição do mouse e retângulo baseado nela
        self.mouse_pos = pygame.mouse.get_pos()
        #self.mouse_pres_pos = pygame.mouse.get_pressed()
        
        self.mouse = pygame.Rect(self.x, self.y, 1, 1)


        

        self.Interacao(event)
        self.a, self.b = self.mouse_pos
        self.area = pygame.Rect(self.a, self.b, 1, 1)
        


    def Interacao(self, event):
        
        # Verifica se o mouse colide com uma área e se houve clique
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self.x, self.y = self.mouse_pos
            self.mouse = pygame.Rect(self.x, self.y, 1, 1)
            print(self.x, self.y)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            self.click = False
            
        
        

img_puzzel_3 = [
    'assets/puzzle3/fundo_puzzle3.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/celular_molde.png',
]
 
img_fase1 = [
    'assets/puzzle3/fase_login/fundo_sombra.png',
    'assets/puzzle3/fase_login/fundo.png',
    'assets/puzzle3/fase_login/login_txt.png',
    'assets/puzzle3/fase_login/usuario.png',
    'assets/puzzle3/fase_login/senha.png',
    'assets/puzzle3/fase_login/face_login.png',
    'assets/puzzle3/fase_login/cadastro_login.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/fundo_item.png',
    '',
    '',
]
 
img_fase2 = [
    'assets/puzzle3/fase_login/fundo_sombra.png',
    'assets/puzzle3/fase_login/fundo.png',
    'assets/puzzle3/calculadora/numeros_calc.png',
    'assets/puzzle3/calculadora/operacoes.png',
    'assets/puzzle3/calculadora/sinais_calc.png',
    'assets/puzzle3/calculadora/clear_calc.png',
    'assets/puzzle3/calculadora/igual.png',
    'assets/puzzle3/calculadora/resultado_calc.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/fundo_item.png',
    '',
    '',
    '',
    '',
    '',
]
 
img_fase3 = [
    'assets/puzzle3/fase_login/fundo_sombra.png',
    'assets/puzzle3/fase_login/fundo.png',
    'assets/puzzle3/puzzle_whats/fundo_nov.png',
    'assets/puzzle3/puzzle_whats/cabecalho.png',
    'assets/puzzle3/puzzle_whats/barra_mensagem.png',
    'assets/puzzle3/puzzle_whats/mensagens.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/fundo_item.png',
    'assets/puzzle3/fundo_item.png',
    '',
    '',
    '',
]
 
img_fase4 = ['assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png',
             'assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png',
             'assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png','assets/puzzle3/fundo_item.png']

geral_img_fases = [img_fase1, img_fase2, img_fase3,img_fase4]

list_montar_pc = [
    'Excluir fundo', 'Criar cor de fundo',
    'Exibir texto de login', 'Não exibir texto',
    'Fraude de usuário', 'Campo para nome de usuário',
    'Campo para a senha', 'Vazar a senha',
    'Exibir foto de perfil', 'Exibir playlist',
    'Desinstalar sistema', 'Botão de acessar a conta',
    '', '',
    '', '',
]
list_redes = [
    'Reset no sistema', 'Criar fundo',
    'Exibir números de 0 a 9', 'Botão de chamada',
    'Cálculos simples', 'Área de pesquisa',
    'Link de delivery', 'Operações complexas',
    'Limpar/apagar', 'Fazer post',
    'Curtir publicação', 'Botão de resposta',
    'Sugestões de amizades', 'Gerar resultado',
    '', '',
    '', '',
    '', '',
    '', '',
    '', '',
    '', ''
]
list_progamação = [
    'Gerar cor de fundo','Acessar o navegador',   
    'Vazar senha admin', 'Exibir papel de parede',   
    'Exibir cabeçalho', 'Inversão de cores',   
    'Barra para digitar texto', 'Renderizar sistema OP',   
    'Excluir downloads', 'Área de mensagens',   
    '', '',
    '', '',
    '', '',
    '', '',
    '', '',
    '', '',
    '', '',
    '', ''
]
list_parabens = [
    'sssssssssss',
    'xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzyz'
]
his_1 = [
    'Você deverá criar uma interface de LOGIN.',
    'Ela deve ser simples e direta, pedindo apenas o que é ',
    'necessário para a autenticação.',
    '',
    'Telas de login normalmente possuem:',
    'Barra para nome, barra para senha, botão de ',
    'confirmar, etc...',
    '',
    'Se adicionar algo desnecessário, o sistema ',
    'reconhecerá como uma ameaça e o processo irá se',
    'reiniciar.',
    '',
    '(Clique em algo com o mouse para continuar...)',
    '',
    
]
his_2 = [
    'Agora você vai criar uma calculadora.'
    '',
    'O foco será em cálculos mais "comuns", a interface ',
    'deve ser limpa e objetiva.',
    '',
    'Calculadoras normalmente possuem:',
    'Os números, expressões básicas (+, -, x, ÷), botão',
    'para limpar, respostas, etc...',
    '',
    '',
    ]
his_3 = [
    'Para finalizar...',
    'Crie uma interface de "bate papo".',
    '',
    'O foco será em poder fazer ligações, enviar e ',
    'receber mensagens.',
    '(São ferramentas importantes quando se precisa de ',
    'uma ajuda).',
    '',
    'Bate papos normalmente possuem:',
    'Cabeçalho (com foto e opção de chamadas), barra',
    'de digitar, área de leitura das mensagens.',
    '',
    ]

his_4 = [
    '                                                   PARABÉNS',
    'Agora você possui 3 novos conhecimentos para sua ',
    'formação profissional.',
    '',
    'Esses desafios foram apenas pequenas introduções',
    'às áreas essenciais do universo da tecnologia.  ',
    'Áreas como:',
    '',
    'Hardware (a parte física do computador);',
    'Redes (conexão de 2 ou mais computadores);',
    'Programação (criação de programas e sistemas)',
    '',
    'Esses são apenas os primeiros passos.',
    'Continue aprendendo!',
    ] 

lista_geral_historias = [his_1, his_2, his_3, his_4]

list_geral = [
    list_montar_pc,
    list_redes,
    list_progamação,
    list_parabens
]

class Inter_Geral:
    def __init__(self):
        pygame.init()
        self.rodando = True
        self.display = pygame.display.get_surface()
        self.fundo = pygame.transform.scale(pygame.image.load(img_puzzel_3[0]), (1920, 1080))
        self.mouse = Mouse()
        self.font = pygame.font.Font('assets/fonts/PixelifySansRegular.ttf', 45)
        self.font_3 = pygame.font.Font('assets/fonts/PixelifySansRegular.ttf', 40)
        self.font_lin = pygame.font.Font('assets/fonts/PixelifySansRegular.ttf', 25)
        self.list = list_geral
        self.historia = lista_geral_historias
        self.cont_frase = 0
        self.cont_tentativas = 0
        self.movendo = 0
        self.escolhido = 0
        self.lugar_lin = [(411,217), (411,246), (411,275), (411,305), (411,335), (411,365), (411,394), (411,424), (411,454), (421,484), (421,514), (421,544)]
        self.sub_text = pygame.Rect(0, 0, 10, 10)
        self.x, self.y = 0, 0
        self.m, self.n = 0,0
        self.prox_lin = 0
        self.list_player = []
        self.ind_x = [218,249,278,307, 338, 368, 398, 427, 450]
        self.aviso = self.font.render('', True, 'white')
        self.resposta = 0
        self.text_res = ''

        self.trans = 0
        self.fase_atual = 0
        self.play = 0
        self.vai = pygame.Rect(0, 0, 1920, 1080)
        self.tel = 0
        self.acertou = False
        self.cont_time = 0  #em milessegundos
        self.cont_pisc = 0  #em milessegundos
        self.cont_passar = 0
        self.ativar_alerta = False
        
        self.fase_1_res = ['b','a','b','a','a','b']
        self.fase_2_res = ['b','a','a','b','a','b','b']
        self.fase_3_res = ['a','b','a','a','b']
        self.cont_cel = 1

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.bilhete = pygame.transform.scale(pygame.image.load(img_puzzel_3[1]), (1270, 800))
        self.exp = pygame.transform.scale(pygame.image.load(img_puzzel_3[2]), (370, 624))
        self.alerta = pygame.transform.scale(pygame.image.load('assets/puzzle3/alerta1.png'), (300, 331))
        
        self.tr = 0
        self.dir_tr = 2
        
        
        self.op_1 = pygame.transform.scale(pygame.image.load(img_puzzel_3[1]), (600, 100))
        self.op_2 = pygame.transform.scale(pygame.image.load(img_puzzel_3[1]), (600, 100))
        

        self.hit1 = pygame.Rect(263, 800, 600, 100)
        self.hit2 = pygame.Rect(1045, 800, 600, 100)

        self.linhas = []

        self.rects = [
        pygame.Rect(370,(223 - 20), 1050, 60),
        pygame.Rect(370,(252 - 20), 1050, 60),
        pygame.Rect(370,(281 - 20), 1050, 60),
        pygame.Rect(370,(311 - 20), 1050, 60),
        pygame.Rect(370,(341 - 20), 1050, 60),
        pygame.Rect(370,(371 - 20), 1050, 60),
        pygame.Rect(370,(401 - 20), 1050, 60),
        pygame.Rect(370,(431 - 20), 1050, 60),
        pygame.Rect(370,(461 - 20), 1050, 60),
        pygame.Rect(380,(491 - 20), 1050, 60),
        pygame.Rect(380,(521 - 20), 1050, 60),
        pygame.Rect(380,(551 - 20), 1050, 60),
        pygame.Rect(0,0, 0, 0)
        ]
    #----------------------------------------
    
    def executar(self, root, event):
        self.mouse.atualizar(event)
        self.desenhar(root)
        self.contexto(root, self.fase_atual)
        self.parte_um()
        self.parte_dois(root)

      

    def expectativa(self, root):
        self.rect_exp = pygame.Rect(0, 0, 0, 0)
        self.list_mobile(self.fase_atual)
        self.draw_cel(root, self.cel_inter, self.pos_geral[self.fase_atual], self.cont_cel)
        root.blit(self.exp, ((1720 + self.tr),75))
        self.mov_exp(35)
        pygame.draw.rect(root, 'BLUE', self.rect_exp)
    
    def mov_exp(self, x):
        if self.mouse.mouse.colliderect(self.rect_exp) and self.tel == 0 :
            
            if self.dir_tr == 1:
                self.dir_tr = 2
                self.tel = 1
            else:
                if self.dir_tr == 2:
                    self.dir_tr = 1
                    self.tel = 1
            self.tel = 0
      
        if self.dir_tr == 1 and self.tr < -150:
            self.tr = self.tr + x
        elif self.dir_tr == 2 and self.tr > -600:
            self.tr = self.tr - x


    def draw_cel(self, root, rect_list, pos, count):
        for i in range(count):  # Itera pelos primeiros `count` elementos
            root.blit(rect_list[i], pos[i])

    #pygame.transform.scale(pygame.image.load(img_puzzel_3[2]), (370, 624))
    def list_mobile(self, atual):
        self.tam_1 = [(366,624),(341, 601),(140, 61),(200, 71),(200, 71),(64, 64),(135,34),(135,500),(500,500),(500,500)]
        self.tam_2 = [(366,624),(341, 601),(199, 276),(65, 264),(192, 340),(65, 65),(65,65),(24,32),(500,500),(500,500),(400,400),(400,400),(400,400)]
        self.tam_3 = [(366,624),(341, 601),(366,624),(278, 32),(275, 29),(290, 230),(65,65),(24,32),(500,500),(500,500),(400,400)]
        self.tam_geral = [self.tam_1, self.tam_2, self.tam_3]

        self.pos_1 = [((1720 + self.tr), 80),((1734 + self.tr), 90),((1842 + self.tr),267),((1810 + self.tr),337),((1810 + self.tr),417),((1878 + self.tr),197), ((1840 + self.tr),527),(400,400)]
        self.pos_2 = [((1720 + self.tr), 80),((1734 + self.tr), 90),((1770 + self.tr),320),((1975 + self.tr),258),((1773 + self.tr),255),((1771 + self.tr),256),((1970 + self.tr),530),((1985 + self.tr),215),(400,400),(400,400),(400,400)]
        self.pos_3 = [((1720 + self.tr), 80),((1734 + self.tr), 90),((1720 + self.tr), 80),((1763 + self.tr),179),((1768 + self.tr),580),((1758 + self.tr),227),((1771 + self.tr),257),((1771 + self.tr),257),((1771 + self.tr),257)]
        self.pos_geral = [self.pos_1, self.pos_2, self.pos_3]
        
        self.cel_inter = [
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][0]), (self.tam_geral[atual][0])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][1]), (self.tam_geral[atual][1])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][2]), (self.tam_geral[atual][2])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][3]), (self.tam_geral[atual][3])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][4]), (self.tam_geral[atual][4])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][5]), (self.tam_geral[atual][5])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][6]), (self.tam_geral[atual][6])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][7]), (self.tam_geral[atual][7])),
        pygame.transform.scale(pygame.image.load(geral_img_fases[atual][8]), (self.tam_geral[atual][8]))
        ]
        '''
        1 - assets/Login_Puzzle/fundo_sombra.png,
        2 - assets/Login_Puzzle/Fundo.png,
        3 - assets/Login_Puzzle/Login_Palavra.png,
        4 - assets/Login_Puzzle/Usuário.png,
        5 - assets/Login_Puzzle/Senha.png,
        6 - assets/Login_Puzzle/Group 1.png,

        1 - assets/Login_Puzzle/fundo_sombra.png',
        2 - assets/Login_Puzzle/Fundo.png,
        3 - assets/Calculadora/Números_199x276.png,
        4 - assets/Calculadora/OperaçõeSimples_65x264.png,
        5 - assets/Calculadora/Sinais_199x399.png,
        6 - assets/Calculadora/Clear_65x65.png,
        7 - assets/Calculadora/Igual_65x65.png,
        8 - assets/Calculadora/resultado.png

        1 - assets/Login_Puzzle/fundo_sombra.png,
        2 - assets/Login_Puzzle/Fundo.png,
        3 - assets/WHATSAPP DOIS/Fundo_nov.png   -  400x633,
        4 - assets/WHATSAPP DOIS/CABEÇALHO_282X32,09.png,
        5 - assets/WHATSAPP DOIS/BARRADEMENSAGEM_303X30.png,
        6 - assets/WHATSAPP DOIS/MENSAGENS_320X244.png,

        '''
        
    def desenhar(self, root):
        root.blit(self.fundo, (0,0))
        root.blit(self.aviso, (self.m,self.n))
        pygame.draw.rect(root, 'red', self.sub_text)



    def contexto(self, root, fase):
        root.blit(self.bilhete, (self.trans, 120))
        for i, text in enumerate(self.historia[fase]):
            text = self.font.render(text, True, 'black')
            root.blit(text, (self.trans + 40, (168 + (i * 48))))

    def intera(self, x):
        if self.fase_atual > 2 and self.mouse.click:
            self.rodando = False
        elif self.mouse.click:
            self.play = x

    def mov_contexto(self, x):
        if self.trans > -1500:
            self.trans = self.trans - x

    def piscar(self, root):
        self.sinalizar = pygame.Rect(415 ,self.ind_x[self.prox_lin], 5, 25)
        self.cont_pisc += 1
        if self.cont_pisc % 3 == 0:
            pygame.draw.rect(root, 'white', self.sinalizar)

    def parte_um(self):
        if self.play == 0:
            self.geral_frase_dois()
            self.trans = 328
            self.cont_time += 1
            self.text_op3 = self.font_3.render('', True, 'black')


            if self.cont_time > 5:
                self.intera(1)

    def arrastar(self, root, resposta):
        self.botoes = pygame.mouse.get_pressed()
        if self.botoes[0]:
            if self.mouse.area.colliderect(self.hit1) and not self.movendo == 1:
                self.resposta = 1   
            elif self.mouse.area.colliderect(self.hit2) and not self.movendo == 1:
                self.resposta = 2   
            self.movendo = 1
            self.olhar()
            self.voar(root)
            
        elif not self.botoes[0]:
            self.movendo = 0
            self.analise(root, resposta)
            self.parado(root)
            self.resposta = 0
            self.text_op3 = ''
            self.aviso = self.font.render(f'Arraste a opção até a frente da linha {self.cont_cel}', True, 'white')
            self.m, self.n = 507, 695

    def analise(self, root , resposta):
        if self.mouse.area.colliderect(self.rects[self.prox_lin]) and not self.resposta == 0:
            self.text_res = self.text_op3
            self.linhas.append(f'{self.text_res};')
            self.mouse.x, self.mouse.y = 0,0
            if self.resposta == 1:
                self.list_player.append('a')
                self.colidiu(resposta, root)
            elif self.resposta == 2:
                self.list_player.append('b')
                self.colidiu(resposta, root)
            
            


    def voar(self, root):
        if not self.resposta == 0:
            self.op_3 = pygame.transform.scale(pygame.image.load(img_puzzel_3[1]), (670, 100))
            self.text_render = self.font.render(self.text_op3, True, 'black')
            root.blit(self.op_3, (self.mouse.a, self.mouse.b))
            root.blit(self.text_render, (self.mouse.a + 17, self.mouse.b + 12))  

    def parado(self, root):
        root.blit(self.op_1, (263, 800))
        root.blit(self.op_2, (1045, 800))
        self.hi1 = pygame.Rect(263, 800, 500, 100)
        self.hi2 = pygame.Rect(1045, 800, 500, 100)
        root.blit(self.text_op1, (263 + 17, 800 + 12)) 
        root.blit(self.text_op2, (1045 + 17, 800 + 12)) 

    def olhar(self):
        if self.resposta == 1:
            self.text_op3 = self.list[self.fase_atual][(self.cont_frase)]
        elif self.resposta == 2:
            self.text_op3 = self.list[self.fase_atual][(self.cont_frase + 1)]


    def comp_novo(self, resposta, root):
        if self.list_player[self.prox_lin] == resposta[self.prox_lin]:
            self.cont_cel = min(self.cont_cel + 1, len(self.cel_inter))
        else:
            self.ativar_alerta = True
        
    def colidiu(self, resposta, root):
        self.comp_novo(resposta, root)
        self.x, self.y = 0,0
        self.text_op3 = ''
        self.cont_frase += 2
        self.prox_lin += 1
        self.cont_tentativas += 1


    def geral_frase_um(self):
            self.text_op1 = self.font_3.render(self.list[self.fase_atual][self.cont_frase] , True, 'black')
            self.text_op2 = self.font_3.render(self.list[self.fase_atual][(self.cont_frase + 1)] , True, 'black')
    def geral_frase_dois(self):
            self.text_op1 = self.font_3.render('' , True, 'black')
            self.text_op2 = self.font_3.render('', True, 'black')

    def draw_dois(self, root, x):
        for i, text in enumerate(self.linhas):
            text = self.font_lin.render(text, True, 'green')
            root.blit(text, self.lugar_lin[i])

        if self.ativar_alerta:
            if self.cont_time < 40:
                self.cont_time += 1
                if self.cont_time % 4 == 0:  # Mostrar a imagem em iterações pares
                    root.blit(self.alerta, (810, 230))
                    self.aviso = self.font.render('SyntaxError: invalid syntax', True, 'red')      
            else:
                self.linhas.clear()
                self.list_player.clear()
                self.cont_cel = 1
                self.cont_tentativas = 0
                self.cont_frase = 0
                self.prox_lin = 0
                self.mouse.click = False
                self.ativar_alerta = False
                self.cont_time = 0


    def comp(self, root, total, resposta):
       
        if self.cont_tentativas >= total:
            if self.list_player == resposta:
                self.aviso = self.font.render('Sistema concluido!', True, 'blue')
                self.m, self.n = 785,700
                self.acertou = True
                
                
            else:
                self.aviso = self.font.render('SyntaxError: invalid syntax', True, 'red')
                self.m, self.n = 707,700
                self.acertou = False
                
              
            self.cont_passar += 1
            self.verificar()

        else:
            self.cont_passar = 0
            self.geral_frase_um()
            self.aviso = self.font.render('', True, 'blue')
            self.arrastar(root, resposta)

    def verificar(self):
        if self.mouse.click and self.cont_passar > 5:
            self.linhas.clear()
            self.list_player.clear()
            self.cont_cel = 1
            self.cont_tentativas = 0
            self.cont_frase = 0
            self.prox_lin = 0
            self.mouse.click = False
            if self.acertou:
                self.play = 0
                self.fase_atual += 1
                self.cont_time = 0
                self.trans = 0
        
    def parte_dois(self, root):
        if self.play == 1:
            self.mov_contexto(150)
            self.expectativa(root)
            self.draw_dois(root, 3)
            self.piscar(root)
            if self.fase_atual == 0:    
                self.comp(root, 6, self.fase_1_res)
            else:
                if self.fase_atual == 1:    
                    self.comp(root, 7, self.fase_2_res)
                else:
                    if self.fase_atual == 2:    
                        self.comp(root, 5, self.fase_3_res)
     

root = pygame.display.set_mode([1920,1080]) #1900,1000 ORIGINAL
puzzle3 = Inter_Geral()
 
# Inicializar a variável de controle do puzzle
dialogo3_concluido = False
puzzle3_ativo = False  # Indica se o puzzle está ativo ou não
puzzle3_concluido = False