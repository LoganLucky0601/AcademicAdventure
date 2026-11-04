import pygame

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
            
img_puzzle_2 = [
    'assets/puzzle2/fundo_puzzle2.png',
    'assets/puzzle2/switch.png',
    'assets/puzzle2/item1.png',

]
pos_x_f1 = [320, 420, 520, 625, 0]
pos_y_f1 = [515, 515, 515, 515, 0]

pos_x_f2 = [520, 320, 320, 625, 0]
pos_y_f2 = [515, 515, 595, 515, 0]

pos_x_f3 = [625, 320, 520, 420, 0]
pos_y_f3 = [515, 515, 595, 515, 0]

pos_x_f4 = [420, 625, 625, 520, 320, 0]
pos_y_f4 = [595, 515, 595, 595, 595, 0]

gp_pos = [
    pos_x_f1,
    pos_y_f1, 

    pos_x_f2,
    pos_y_f2,

    pos_x_f3,
    pos_y_f3,

    pos_x_f4,
    pos_y_f4, 
    ]

his = [
    'Este é um switch...',
    'No lado esquerdo, luzes vermelhas brilharão em uma sequência.',
    '',
    'Quando as luzes verdes aparecerem, repita a sequência no lado',
    'direito.',
    '',
    '                                 (Clique com o mouse para continuar)',
]


class Inter_Geral:
    def __init__(self, gp_pos):
        pygame.init()
        self.rodando = True
        self.display = pygame.display.get_surface()
        self.fundo = pygame.transform.scale(pygame.image.load(img_puzzle_2[0]), (1920, 1080))
        self.mouse = Mouse()
        self.gp_pos = gp_pos
        self.prox_fase = False
        self.reptir_fase = False
        self.area_clicada = 0
        self.fase_atual = 1
        self.play = 0
        self.cont_x = 0
        self.errou = 'Errou! Repita a sequência'
        self.cont_y = 0
        self.font = pygame.font.Font("assets/fonts/PixelifySansRegular.ttf", 60)
        self.font2 = pygame.font.Font("assets/fonts/PixelifySansRegular.ttf", 50)
        self.cont_tentativas = 0
        self.text_fase_atual = self.font.render(f'Nivel: {self.fase_atual}', True, 'white')
        self.text_exp_1 = self.font.render('', True, (189,83,107))
        self.text_exp_2 = self.font.render('', True, (75,0,130))
        self.msg = self.font.render('', True, (10,0,10))
        self.m = 0
        self.n = 0
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.cont_time = 0
        self.his = his
        
        self.list_player = []
        self.fase_1_res = ['a','b','c','d']
        self.fase_2_res = ['c','a','e','d']
        self.fase_3_res = ['d','a','g','b']
        self.fase_4_res = ['f','d','h','g','e']

        self.swith = pygame.transform.scale(pygame.image.load(img_puzzle_2[1]), (1920, 1080))
        self.bilhete = pygame.transform.scale(pygame.image.load(img_puzzle_2[2]), (1695, 470))

        self.rect_fundo = pygame.Rect(0, 0, 0, 0)

        self.rect_1 = pygame.Rect(300, 410, 1270, 360)
        self.rect_2 = pygame.Rect(0, 0, 0, 0)
        self.win = pygame.Rect(300,350,1300,400)
        self.cor = 'red'

        self.dec_1 = pygame.Rect(0,0,0,0)
        
        self.hit_1 = pygame.Rect((320 + 840), 515, 75, 50)
        self.hit_2 = pygame.Rect((420 + 840), 515, 75, 50)
        self.hit_3 = pygame.Rect((520 + 840), 515, 75, 50)
        self.hit_4 = pygame.Rect((625 + 840), 515, 75, 50)
        
        self.hit_5 = pygame.Rect((320 + 840), 595, 75, 50)
        self.hit_6 = pygame.Rect((420 + 840), 595, 75, 50)
        self.hit_7 = pygame.Rect((520 + 840), 595, 75, 50)
        self.hit_8 = pygame.Rect((625 + 840), 595, 75, 50)


    #PARTE 1 - BRILHAR A COMBINAÇÃO
    def tele(self, fx, fy, limite):
        if self.play == 1:
            self.rect_2 = pygame.Rect(self.gp_pos[fx][self.cont_x], self.gp_pos[fy][self.cont_y], 75, 50)
            self.cont_x += 1
            self.cont_y += 1
            self.msg = self.font.render('', True, (10,0,10))

            if self.cont_x > limite:
                self.cont_x = 0
                self.cont_y = 0
                self.play = 2
    
    def draw_fase(self):
        if self.play == 1:
            self.cor = 'red'
            self.dec_1 =  pygame.Rect(330,420,600,30)
            self.fps = 1
            if self.fase_atual == 1:
                self.tele(0, 1, 4)
            else:
                if self.fase_atual == 2:
                    self.tele(2, 3, 4)
                else:
                    if self.fase_atual == 3:
                        self.tele(4, 5, 4)
                    else:
                        if self.fase_atual == 4:
                            self.tele(6, 7, 5)
        else:
            self.fps = 60

        if self.play == 2:
            self.rect_2 = pygame.Rect(0,0,0,0)
            self.cor = 'green'
            self.dec_1 =  pygame.Rect(1050,420,600,30)
        elif self.play == 3:
            self.dec_1 =  pygame.Rect(0,0,0,0)

    # parte 2 - add lista
    def click_mouse(self, hit, num, letra):
        if self.mouse.mouse.colliderect(hit) and self.area_clicada != num:
            self.cont_tentativas += 1
            self.area_clicada = num
            self.list_player.append(letra)

    def add_resposta(self): 
        if self.play == 2:
            self.click_mouse(self.hit_1, 1, 'a') 
            self.click_mouse(self.hit_2, 2, 'b') 
            self.click_mouse(self.hit_3, 3, 'c') 
            self.click_mouse(self.hit_4, 4, 'd') 
            self.click_mouse(self.hit_5, 5, 'e') 
            self.click_mouse(self.hit_6, 6, 'f') 
            self.click_mouse(self.hit_7, 7, 'g') 
            self.click_mouse(self.hit_8, 8, 'h')
    
    #PARTE 3 - PISCAR LOCAL DO MOUSE
    def click_cor(self, surface, click, num, botao ):
        if click == num and self.play == 2:
            pygame.draw.rect(surface, 'green', botao)
        else:
            pygame.draw.rect(surface, 'black', botao)

    # A PARTE 4 - COMPARAR AS COMBINAÇÕES!
    def comp(self, fase, tentativas, fase_res, text):
        if self.fase_atual == fase and self.cont_tentativas == tentativas:
            if self.list_player == fase_res:
                self.prox_fase = True
                self.cont_tentativas = 0
                self.cont_time = 0
                self.m = 750
                self.n = 250
                self.list_player.clear()
                self.msg = self.font.render(text, True, (0, 0, 0))
                
            else:
                self.reptir_fase = True
                self.cont_tentativas = 0
                self.m = 600
                self.n = 310
                self.list_player.clear()
                self.msg = self.font.render(self.errou, True, 'red')  
                
    def comparar_fim(self):
        self.comp(1, 4, self.fase_1_res, 'FASE 1 FEITA!')
        self.comp(2, 4, self.fase_2_res, 'FASE 2 FEITA!')
        self.comp(3, 4, self.fase_3_res, 'FASE 3 FEITA!')
        self.comp(4, 5, self.fase_4_res, 'FASE 4 FEITA!')

    # PARTE 5.1: 'SE ACERTAR'
    def proxima(self):
        if self.prox_fase:
            if not self.mouse.mouse.colliderect(self.rect_fundo):
                self.play = 1
                self.fase_atual += 1
                self.area_clicada = 0
                self.prox_fase = False

    # PARTE 5.2: 'SE ERRAR'
    def reptir(self):
        if self.reptir_fase:
            if not self.mouse.mouse.colliderect(self.rect_fundo):
                self.play = 1
                self.area_clicada = 0
                self.reptir_fase = False
    
    def iniciar(self, root):
        if self.play == 0:
            root.blit(self.bilhete, (100,15))
            for i, text in enumerate(self.his):
                text = self.font2.render(text, True, 'black')
                root.blit(text, (150, (50 + (i * 48))))
            if self.mouse.x > 0:
                self.text_exp_1 = self.font.render('', True, (189,83,107))
                self.text_exp_2 = self.font.render('', True, (75,0,130))
                self.play = 1

    def fim(self, root):
        if self.fase_atual >= 5:
            self.cont_time += 1
            if self.cont_time > 5: 
                self.fps = 60 # Verifica se está na fase 5
                self.m = 650
                self.n = 200
                self.dec_1 =  pygame.Rect(0,0,0,0)
                self.msg = self.font.render('CONECTADO A REDE', True, 'green')
                self.text_exp_2 = self.font.render('Clique em algo para continuar...', True, (0, 0, 0)) 
                if self.mouse.click:
                    self.fase_atual += 1
                    self.rodando = False

    # ----------------------------------------

    def desenhar(self, surface):
        surface.blit(self.fundo, (0,0))
        pygame.draw.rect(surface, 'black', self.rect_1)
            
        #interagiveis
        self.click_cor(surface, self.area_clicada, 1, self.hit_1)
        self.click_cor(surface, self.area_clicada, 2, self.hit_2)
        self.click_cor(surface, self.area_clicada, 3, self.hit_3)
        self.click_cor(surface, self.area_clicada, 4, self.hit_4)
        self.click_cor(surface, self.area_clicada, 5, self.hit_5)
        self.click_cor(surface, self.area_clicada, 6, self.hit_6)
        self.click_cor(surface, self.area_clicada, 7, self.hit_7)
        self.click_cor(surface, self.area_clicada, 8, self.hit_8)

        self.draw_fase()
        pygame.draw.rect(surface, 'red', self.rect_2)
        pygame.draw.rect(surface, self.cor, self.dec_1)


        surface.blit(self.swith, (0,0))
        
        surface.blit(self.msg, (self.m, self.n))
        surface.blit(self.text_exp_1, (475, 100))
        surface.blit(self.text_exp_2, (500, 280))


    def events(self, event): 
        self.mouse.atualizar(event)
        self.add_resposta()
        self.proxima()
        self.reptir()
        

    def executar(self, root, event):
        self.comparar_fim()
        self.desenhar(root)
        self.events(event)
        self.iniciar(root)
        self.fim(root)
        
        self.clock.tick(self.fps)
        
puzzle2 = Inter_Geral(gp_pos)

# Inicializar a variável de controle do puzzle
dialogo2_concluido = False
puzzle2_ativo = False  # Indica se o puzzle está ativo ou não
puzzle2_concluido = False
