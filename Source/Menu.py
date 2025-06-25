import pygame as pg, sys
from Source import Movimento_e_colisao as MC
from Source import Gerador_labrinto as GL
from pathlib import Path
import time 

diretorio_base = Path.cwd()


class Botao():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def atualizar(self, TELA):
        if self.image is not None:
            TELA.blit(self.image, self.rect)
        TELA.blit(self.text, self.text_rect)

    def checarPorMouse(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def trocarCor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

pg.init()

TELA = pg.display.set_mode((1280, 720))
pg.display.set_caption("Labirinto") 

BG = pg.image.load("Dados/imagens_fontes/Background.png") 

def get_font(size): # Retorna Press-Start-2P no tamanho que quisermos
    return pg.font.Font("Dados/imagens_fontes/font.ttf", size) 



def facil(caminho_arquivo_jogadores, diretorio_base):
    while True:
        FACIL_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("green")

        FACIL_TEXT = get_font(45).render("Fácil", True, "Black")
        FACIL_RECT = FACIL_TEXT.get_rect(center=(640, 120))
        TELA.blit(FACIL_TEXT, FACIL_RECT)
        
        FACIL_UM = Botao(image=None, pos=(640, 330),
                                text_input="Fase F1", font=get_font(60), base_color="Black", hovering_color="Yellow")
        
        FACIL_UM.trocarCor(FACIL_MOUSE_POS)
        FACIL_UM.atualizar(TELA)

        
        FACIL_BACK = Botao(image=None, pos=(200, 560),
                                text_input="VOLTAR", font=get_font(30), base_color="Black", hovering_color="Purple")
        

        FACIL_BACK.trocarCor(FACIL_MOUSE_POS)
        FACIL_BACK.atualizar(TELA)


        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if FACIL_BACK.checarPorMouse(FACIL_MOUSE_POS):
                    campanha(caminho_arquivo_jogadores, diretorio_base)
                if FACIL_UM.checarPorMouse(FACIL_MOUSE_POS):
                    with open(diretorio_base/'Dados'/'fases'/'fase_01.txt') as arq_facil_1:
                        MC.jogar_fase_pronta(1, 16, 1, 9, 1, TELA, arq_facil_1)
                        tela_acabar_fase_c(caminho_arquivo_jogadores, diretorio_base)



        pg.display.update() # Modificado aqui



def medio(caminho_arquivo_jogadores, diretorio_base):
    while True:
        MEDIO_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("orange")

        MEDIO_TEXT = get_font(45).render("Médio", True, "Black")
        MEDIO_RECT = MEDIO_TEXT.get_rect(center=(640, 120))
        TELA.blit(MEDIO_TEXT, MEDIO_RECT)

        MEDIO_UM = Botao(image=None, pos=(400, 330),
                                 text_input="Fase M1", font=get_font(60), base_color="Black", hovering_color="Gray")

        MEDIO_UM.trocarCor(MEDIO_MOUSE_POS)
        MEDIO_UM.atualizar(TELA)

        MEDIO_DOIS = Botao(image=None, pos=(920, 330),
                                 text_input="Fase M2", font=get_font(60), base_color="Black", hovering_color="Gray")

        MEDIO_DOIS.trocarCor(MEDIO_MOUSE_POS)
        MEDIO_DOIS.atualizar(TELA)



        MEDIO_BACK = Botao(image=None, pos=(200, 560),
                                 text_input="VOLTAR", font=get_font(30), base_color="Black", hovering_color="Purple")


        MEDIO_BACK.trocarCor(MEDIO_MOUSE_POS)
        MEDIO_BACK.atualizar(TELA)

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if MEDIO_BACK.checarPorMouse(MEDIO_MOUSE_POS):
                    campanha(caminho_arquivo_jogadores, diretorio_base)
                if MEDIO_UM.checarPorMouse(MEDIO_MOUSE_POS):
                    with open(diretorio_base/'Dados'/'fases'/'fase_02.txt') as arq_medio_1:
                        MC.jogar_fase_pronta(1, 35, 1, 19, 1, TELA, arq_medio_1)
                        tela_acabar_fase_c(caminho_arquivo_jogadores, diretorio_base)
                if MEDIO_DOIS.checarPorMouse(MEDIO_MOUSE_POS):
                    with open(diretorio_base/'Dados'/'fases'/'fase_03.txt') as arq_medio_2:
                        MC.jogar_fase_pronta(1, 35, 1, 19, 1, TELA, arq_medio_2)
                        tela_acabar_fase_c(caminho_arquivo_jogadores, diretorio_base)



        pg.display.update() # Modificado aqui



def dificil(caminho_arquivo_jogadores, diretorio_base):
    while True:
        DIFICIL_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("Red")

        DIFICIL_TEXT = get_font(45).render("Difícil", True, "Black")
        DIFICIL_RECT = DIFICIL_TEXT.get_rect(center=(640, 120))
        TELA.blit(DIFICIL_TEXT, DIFICIL_RECT)

        DIFICIL_UM = Botao(image=None, pos=(400, 330),
                                 text_input="Fase D1", font=get_font(60), base_color="Black", hovering_color="White")

        DIFICIL_UM.trocarCor(DIFICIL_MOUSE_POS)
        DIFICIL_UM.atualizar(TELA)

        DIFICIL_DOIS = Botao(image=None, pos=(920, 330),
                                 text_input="Fase D2", font=get_font(60), base_color="Black", hovering_color="white")

        DIFICIL_DOIS.trocarCor(DIFICIL_MOUSE_POS)
        DIFICIL_DOIS.atualizar(TELA)

        DIFICIL_BACK = Botao(image=None, pos=(200, 560),
                                 text_input="VOLTAR", font=get_font(30), base_color="Black", hovering_color="Purple")

        DIFICIL_BACK.trocarCor(DIFICIL_MOUSE_POS)
        DIFICIL_BACK.atualizar(TELA)

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if DIFICIL_BACK.checarPorMouse(DIFICIL_MOUSE_POS):
                    campanha(caminho_arquivo_jogadores, diretorio_base)
                if DIFICIL_UM.checarPorMouse(DIFICIL_MOUSE_POS):
                    with open(diretorio_base/'Dados'/'fases'/'fase_04.txt') as arq_dificil_1:
                        MC.jogar_fase_pronta(1, 59, 1, 31, 1, TELA, arq_dificil_1)
                        tela_acabar_fase_c(caminho_arquivo_jogadores, diretorio_base)
                if DIFICIL_DOIS.checarPorMouse(DIFICIL_MOUSE_POS):
                    with open(diretorio_base/'Dados'/'fases'/'fase_05.txt') as arq_dificil_2:
                        MC.jogar_fase_pronta(1, 59, 1, 31, 1, TELA, arq_dificil_2)
                        tela_acabar_fase_c(caminho_arquivo_jogadores, diretorio_base)


        pg.display.update()



def campanha(caminho_arquivo_jogadores, diretorio_base):
    while True:
        CAMPANHA_MOUSE_POS = pg.mouse.get_pos() 

        TELA.fill("white")

        CAMPANHA_TEXT = get_font(45).render("Escolha a dificuldade:", True, "Black")
        CAMPANHA_RECT = CAMPANHA_TEXT.get_rect(center=(640, 120))
        TELA.blit(CAMPANHA_TEXT, CAMPANHA_RECT)
        
        CAMPANHA_FACIL = Botao(image=None, pos=(180, 330),
                                text_input="Fácil", font=get_font(60), base_color="Black", hovering_color="Green")
        
        CAMPANHA_FACIL.trocarCor(CAMPANHA_MOUSE_POS)
        CAMPANHA_FACIL.atualizar(TELA)

        CAMPANHA_MEDIO = Botao(image=None, pos=(550, 330),
                                text_input="Médio", font=get_font(60), base_color="Black", hovering_color="Orange")

            
        CAMPANHA_MEDIO.trocarCor(CAMPANHA_MOUSE_POS)
        CAMPANHA_MEDIO.atualizar(TELA)

        CAMPANHA_DIFICIL = Botao(image=None, pos=(990, 330),
                                text_input="Difícil", font=get_font(60), base_color="Black", hovering_color="Red")

            
        CAMPANHA_DIFICIL.trocarCor(CAMPANHA_MOUSE_POS)
        CAMPANHA_DIFICIL.atualizar(TELA)
        
        
        CAMPANHA_BACK = Botao(image=None, pos=(200, 560),
                                text_input="VOLTAR", font=get_font(30), base_color="Black", hovering_color="Purple")
        

        CAMPANHA_BACK.trocarCor(CAMPANHA_MOUSE_POS)
        CAMPANHA_BACK.atualizar(TELA)
                        
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if CAMPANHA_BACK.checarPorMouse(CAMPANHA_MOUSE_POS):
                    play(caminho_arquivo_jogadores, diretorio_base)
                if CAMPANHA_FACIL.checarPorMouse(CAMPANHA_MOUSE_POS):
                    facil(caminho_arquivo_jogadores, diretorio_base)
                if CAMPANHA_MEDIO.checarPorMouse(CAMPANHA_MOUSE_POS):
                    medio(caminho_arquivo_jogadores, diretorio_base)
                if CAMPANHA_DIFICIL.checarPorMouse(CAMPANHA_MOUSE_POS):
                    dificil(caminho_arquivo_jogadores, diretorio_base)

        pg.display.update() 



def pegar_nome_jogador(caminho_arquivo_jogadores, diretorio_base):
    nome_jogador = ""
    entrada_ativa = True
    tamanho_maximo = 15 

    while entrada_ativa:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN: 
                    input_active = False
                    return nome_jogador
                elif event.key == pg.K_BACKSPACE: 
                    nome_jogador = nome_jogador[:-1] 
                else:
                    if len(nome_jogador) < tamanho_maximo: 
                        nome_jogador += event.unicode 

        TELA.fill("black") 

        
        prompt_text = get_font(30).render("Digite seu nome:", True, "white")
        prompt_rect = prompt_text.get_rect(center=(640, 200))
        TELA.blit(prompt_text, prompt_rect)

       
        nome_surface = get_font(50).render(nome_jogador + ("|" if entrada_ativa else ""), True, "white") # Adiciona um cursor piscando
        nome_rect = nome_surface.get_rect(center=(640, 300))
        TELA.blit(nome_surface, nome_rect)

        pg.display.update()



def aleatorio(caminho_arquivo_jogadores, diretorio_base):
    import time  
    while True:
        lab_aleatorio = GL.Labirinto(55, 31)
        lab_aleatorio.gerar_labirinto()  # <<<<<<<<<<<<<<<<<<<<<<

        ALEATORIO_MOUSE_POS = pg.mouse.get_pos()

        TELA.fill((0, 0, 0))  # Fundo igual cor da parede

        ALEATORIO_TEXT = get_font(45).render("Modo Aleatório", True, "White")
        ALEATORIO_RECT = ALEATORIO_TEXT.get_rect(center=(640, 120))
        TELA.blit(ALEATORIO_TEXT, ALEATORIO_RECT)


        ALEATORIO_CRIAR = Botao(image=None, pos=(640, 360),
                                text_input="Criar usuário", font=get_font(47), base_color="White", hovering_color="Red")
        ALEATORIO_CRIAR.trocarCor(ALEATORIO_MOUSE_POS)
        ALEATORIO_CRIAR.atualizar(TELA)

        ALEATORIO_BACK = Botao(image=None, pos=(200, 560),
                               text_input="VOLTAR", font=get_font(30), base_color="White", hovering_color="Purple")
        ALEATORIO_BACK.trocarCor(ALEATORIO_MOUSE_POS)
        ALEATORIO_BACK.atualizar(TELA)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if ALEATORIO_BACK.checarPorMouse(ALEATORIO_MOUSE_POS):
                    play(caminho_arquivo_jogadores, diretorio_base)
                    return
                
                if ALEATORIO_CRIAR.checarPorMouse(ALEATORIO_MOUSE_POS):
                    username = pegar_nome_jogador(caminho_arquivo_jogadores, diretorio_base)
                    with open(caminho_arquivo_jogadores, "a", encoding="utf-8") as arq_jogadores_usavel:
                        arq_jogadores_usavel.write(username + " ")

                        pos_x, pos_y = 1, 1
                        pontuacao = 100000
                        tempo_inicio = time.time()
                        ultimo_tempo = tempo_inicio
                        clock = pg.time.Clock()

                        margem_x = (TELA.get_width() - lab_aleatorio.largura * lab_aleatorio.tamanho_celula) // 2
                        margem_y = (TELA.get_height() - lab_aleatorio.altura * lab_aleatorio.tamanho_celula) // 2

                        rodando_labirinto = True
                        while rodando_labirinto:
                            #por aqui pause
                            TELA.fill((0, 0, 0))  # Fundo parede
                            tempo_atual = time.time()
                            if tempo_atual - ultimo_tempo >= 1:
                                pontuacao -= 100
                                ultimo_tempo = tempo_atual

                            for event_lab in pg.event.get():
                                if event_lab.type == pg.QUIT:
                                    pg.quit()
                                    sys.exit()
                                if event_lab.type == pg.KEYDOWN:
                                    if event_lab.key == pg.K_ESCAPE:
                                        rodando_labirinto = False 

                            teclas = pg.key.get_pressed()
                            novo_x, novo_y = pos_x, pos_y

                            if teclas[pg.K_a]:
                                if MC.pode_mover(pos_x - 1, lab_aleatorio.largura, pos_y, lab_aleatorio.altura, lab_aleatorio):
                                    novo_x = pos_x - 1
                            elif teclas[pg.K_d]:
                                if MC.pode_mover(pos_x + 1, lab_aleatorio.largura, pos_y, lab_aleatorio.altura, lab_aleatorio):
                                    novo_x = pos_x + 1
                            elif teclas[pg.K_w]:
                                if MC.pode_mover(pos_x, lab_aleatorio.largura, pos_y - 1, lab_aleatorio.altura, lab_aleatorio):
                                    novo_y = pos_y - 1
                            elif teclas[pg.K_s]:
                                if MC.pode_mover(pos_x, lab_aleatorio.largura, pos_y + 1, lab_aleatorio.altura, lab_aleatorio):
                                    novo_y = pos_y + 1

                            if (novo_x != pos_x) or (novo_y != pos_y):
                                pontuacao -= 50
                            pos_x, pos_y = novo_x, novo_y
                            if lab_aleatorio.mapa[novo_y][novo_x] == lab_aleatorio.mapa[lab_aleatorio.altura - 2][lab_aleatorio.largura - 2]:
                                arq_jogadores_usavel.write(f"{pontuacao}\n")

                                tela_acabar_fase_a(caminho_arquivo_jogadores, diretorio_base, pontuacao, username)
                                rodando_labirinto = False
                                #aqui tela fim

                            # Desenhar labirinto centralizado
                            lab_aleatorio.desenhar_mapa(TELA, margem_x, margem_y)

                            # Desenhar jogador centralizado
                            rect_jogador = pg.Rect(
                                margem_x + pos_x * lab_aleatorio.tamanho_celula,
                                margem_y + pos_y * lab_aleatorio.tamanho_celula,
                                lab_aleatorio.tamanho_celula,
                                lab_aleatorio.tamanho_celula
                            )
                            pg.draw.rect(TELA, (66, 135, 245), rect_jogador)

                            # Exibir pontuação
                            fonte = pg.font.SysFont(None, 36)
                            texto_pontuacao = fonte.render(f"Pontos: {max(pontuacao, 0)}", True, (255, 255, 255))
                            TELA.blit(texto_pontuacao, (10, 10))

                            pg.display.update()
                            clock.tick(10)


        pg.display.update()




def play(caminho_arquivo_jogadores, diretorio_base):
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("black")

        PLAY_TEXT = get_font(45).render("Escolha o modo de jogo:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        TELA.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_CAMPANHA = Botao(image=None, pos=(360, 360),
                                text_input="CAMPANHA", font=get_font(45), base_color="White", hovering_color="Purple")

            
        PLAY_CAMPANHA.trocarCor(PLAY_MOUSE_POS)
        PLAY_CAMPANHA.atualizar(TELA)

        PLAY_ALEATORIO = Botao(image=None, pos=(900, 360),
                                text_input="ALEATÓRIO", font=get_font(45), base_color="White", hovering_color="Blue")

            
        PLAY_ALEATORIO.trocarCor(PLAY_MOUSE_POS)
        PLAY_ALEATORIO.atualizar(TELA)


        PLAY_BACK = Botao(image=None, pos=(200, 560),
                                text_input="VOLTAR", font=get_font(30), base_color="White", hovering_color="Green")

            
        PLAY_BACK.trocarCor(PLAY_MOUSE_POS)
        PLAY_BACK.atualizar(TELA)

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if PLAY_BACK.checarPorMouse(PLAY_MOUSE_POS):
                    main_menu(caminho_arquivo_jogadores, diretorio_base)
                if PLAY_CAMPANHA.checarPorMouse(PLAY_MOUSE_POS):
                     campanha(caminho_arquivo_jogadores, diretorio_base)

                if PLAY_ALEATORIO.checarPorMouse(PLAY_MOUSE_POS):
                    aleatorio(caminho_arquivo_jogadores, diretorio_base)
                    
        pg.display.update() # Modificado aqui



def placar_lideres(caminho_arquivo_jogadores, diretorio_base):
    while True:
        PLACAR_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("black")
        PLACAR_TEXTO_TITULO= get_font(40).render("PLACAR DE LIDERES", True, "white")
        PLACAR_RECT_TITULO = PLACAR_TEXTO_TITULO.get_rect(center=(640, 25))
        TELA.blit(PLACAR_TEXTO_TITULO, PLACAR_RECT_TITULO)

        PLACAR_BACK = Botao(image=None, pos=(1160, 670),
                            text_input="VOLTAR", font=get_font(20), base_color="white", hovering_color="Green")
        
        with open(caminho_arquivo_jogadores, 'r', encoding='utf-8') as arq_usavel:
            i=70
            lista_jogadores = []
            for linha in arq_usavel:
                linha = linha.split()
                lista_jogadores.append((linha[0], linha[1]))
            lista_jogadores.sort(key=lambda x: x[1])

            for j in range(len(lista_jogadores)):
                PLACAR_TEXTO_JOGADORES = get_font(30).render(lista_jogadores[j][0]+"..........."+lista_jogadores[j][1],
                                                             True, "white")
                PLACAR_RECT_JOGADORES = PLACAR_TEXTO_JOGADORES.get_rect(center=(640, i))
                TELA.blit(PLACAR_TEXTO_JOGADORES, PLACAR_RECT_JOGADORES)
                i+=30

        PLACAR_BACK.trocarCor(PLACAR_MOUSE_POS)
        PLACAR_BACK.atualizar(TELA)               

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if PLACAR_BACK.checarPorMouse(PLACAR_MOUSE_POS):
                    main_menu(caminho_arquivo_jogadores, diretorio_base)

        pg.display.update() # Modificado aqui



def sair(caminho_arquivo_jogadores, diretorio_base):
    while True:
        SAIR_MOUSE_POS = pg.mouse.get_pos() 

        TELA.fill("white")

        SAIR_TEXT = get_font(45).render("Tem certeza que deseja sair?", True, "Black")
        SAIR_RECT = SAIR_TEXT.get_rect(center=(640, 130))
        TELA.blit(SAIR_TEXT, SAIR_RECT)

        SAIR_BACK = Botao(image=None, pos=(640, 500),
                              text_input="VOLTAR", font=get_font(75), base_color="Black", hovering_color="Green")
        SAIR_BACK.trocarCor(SAIR_MOUSE_POS)
        SAIR_BACK.atualizar(TELA)


        SAIR_SIM = Botao(image=None, pos=(640, 360),
                              text_input="SIM", font=get_font(75), base_color="Black", hovering_color="Red")
        SAIR_SIM.trocarCor(SAIR_MOUSE_POS)
        SAIR_SIM.atualizar(TELA)               

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if SAIR_BACK.checarPorMouse(SAIR_MOUSE_POS):
                    main_menu(caminho_arquivo_jogadores, diretorio_base)
                if SAIR_SIM.checarPorMouse(SAIR_MOUSE_POS):
                    pg.quit() # Modificado aqui
                    sys.exit()

        pg.display.update() # Modificado aqui






def tela_acabar_fase_a(caminho_arquivo_jogadores, diretorio_base, pontuacao, username): 
    while True:
        ACABAR_MOUSE_POS = pg.mouse.get_pos() 

        TELA.fill("gray") # Cor de fundo

        ACABAR_TEXT = get_font(32).render(f"PARABÉNS {username}, a fase foi FINALIZADA!", True, "Black")
        ACABAR_RECT = ACABAR_TEXT.get_rect(center=(640, 110))
        TELA.blit(ACABAR_TEXT, ACABAR_RECT)

        SCORE_TEXT = get_font(40).render(f"VOCÊ TEVE UM SCORE DE {pontuacao}.", True, "Black")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 220))
        TELA.blit(SCORE_TEXT, SCORE_RECT)


        
        ACABAR_OUTRA_FASE = Botao(image=None, pos=(640, 380),
                                     text_input="Jogar outra fase", font=get_font(60), base_color="Black", hovering_color="Green")
        ACABAR_OUTRA_FASE.trocarCor(ACABAR_MOUSE_POS)
        ACABAR_OUTRA_FASE.atualizar(TELA)


        ACABAR_SAIR_MENU = Botao(image=None, pos=(640, 600), 
                                     text_input="VOLTAR AO MENU", font=get_font(45), base_color="Black", hovering_color="Red")
        
        ACABAR_SAIR_MENU.trocarCor(ACABAR_MOUSE_POS)
        ACABAR_SAIR_MENU.atualizar(TELA)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if ACABAR_OUTRA_FASE.checarPorMouse(ACABAR_MOUSE_POS):
                   play(caminho_arquivo_jogadores, diretorio_base)

                if ACABAR_SAIR_MENU.checarPorMouse(ACABAR_MOUSE_POS):
                    main_menu(caminho_arquivo_jogadores, diretorio_base)
                    

        pg.display.update()

def tela_acabar_fase_c(caminho_arquivo_jogadores, diretorio_base): 
    while True:
        ACABARC_MOUSE_POS = pg.mouse.get_pos() 

        TELA.fill("gray") # Cor de fundo

        ACABARC_TEXT = get_font(32).render(f"PARABÉNS, a fase foi CONCLUÍDA!", True, "Black")
        ACABARC_RECT = ACABARC_TEXT.get_rect(center=(640, 110))
        TELA.blit(ACABARC_TEXT, ACABARC_RECT)


        ACABARC_OUTRA_FASE = Botao(image=None, pos=(640, 380),
                                     text_input="Jogar outra fase", font=get_font(60), base_color="Black", hovering_color="Green")
        ACABARC_OUTRA_FASE.trocarCor(ACABARC_MOUSE_POS)
        ACABARC_OUTRA_FASE.atualizar(TELA)


        ACABARC_SAIR_MENU = Botao(image=None, pos=(640, 600), 
                                     text_input="VOLTAR AO MENU", font=get_font(45), base_color="Black", hovering_color="Red")
        
        ACABARC_SAIR_MENU.trocarCor(ACABARC_MOUSE_POS)
        ACABARC_SAIR_MENU.atualizar(TELA)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if ACABARC_OUTRA_FASE.checarPorMouse(ACABARC_MOUSE_POS):
                   play(caminho_arquivo_jogadores, diretorio_base)

                if ACABARC_SAIR_MENU.checarPorMouse(ACABARC_MOUSE_POS):
                    main_menu(caminho_arquivo_jogadores, diretorio_base)
                    

        pg.display.update()




def main_menu(caminho_arquivo_jogadores, diretorio_base):
    while True:
        TELA.blit(BG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        MENU_TEXT = get_font(120).render("MENU", True, (182, 143, 64))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BOTAO = Botao(image=pg.image.load("Dados/imagens_fontes/Play Rect.png"), pos=(640, 250), # Modificado aqui
                             text_input="JOGAR", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")
        PLACAR_LIDERES_BOTAO = Botao(image=pg.image.load("Dados/imagens_fontes/PLACAR Rect.png"), pos=(640, 400), # Modificado aqui
                                text_input="PLACAR", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")
        SAIR_BOTAO = Botao(image=pg.image.load("Dados/imagens_fontes/Quit Rect.png"), pos=(640, 550), # Modificado aqui
                             text_input="SAIR", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")

        TELA.blit(MENU_TEXT, MENU_RECT)

        for botao in [PLAY_BOTAO, PLACAR_LIDERES_BOTAO, SAIR_BOTAO]:
            botao.trocarCor(MENU_MOUSE_POS)
            botao.atualizar(TELA)

        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                pg.quit() 
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: 
                if PLAY_BOTAO.checarPorMouse(MENU_MOUSE_POS):
                    play(caminho_arquivo_jogadores, diretorio_base)
                if PLACAR_LIDERES_BOTAO.checarPorMouse(MENU_MOUSE_POS):
                    placar_lideres(caminho_arquivo_jogadores, diretorio_base)
                if SAIR_BOTAO.checarPorMouse(MENU_MOUSE_POS):
                    sair(caminho_arquivo_jogadores, diretorio_base)

        pg.display.update() # Modificado aqui
