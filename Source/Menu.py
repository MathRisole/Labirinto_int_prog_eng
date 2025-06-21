import pygame as pg, sys



#criar a classe de um botão
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
pg.display.set_caption("Menu") # Modificado aqui

BG = pg.image.load("Dados/imagens_fontes/Background.png") # Modificado aqui

def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("Dados/imagens_fontes/font.ttf", size) # Modificado aqui

def play():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("black")

        PLAY_TEXT = get_font(45).render("Essa é a tela da gameplay.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        TELA.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Botao(image=None, pos=(640, 460),
                             text_input="VOLTAR", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.trocarCor(PLAY_MOUSE_POS)
        PLAY_BACK.atualizar(TELA)

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if PLAY_BACK.checarPorMouse(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update() # Modificado aqui

def options():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        TELA.fill("white")

        OPTIONS_TEXT = get_font(45).render("Tela de estatísticas.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        TELA.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Botao(image=None, pos=(640, 460),
                              text_input="VOLTAR", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.trocarCor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.atualizar(TELA)               

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if OPTIONS_BACK.checarPorMouse(OPTIONS_MOUSE_POS):
                    main_menu()

        pg.display.update() # Modificado aqui


def sair():
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
                    main_menu()
                if SAIR_SIM.checarPorMouse(SAIR_MOUSE_POS):
                    pg.quit() # Modificado aqui
                    sys.exit()

        pg.display.update() # Modificado aqui


    


def main_menu():
    while True:
        TELA.blit(BG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos() # Modificado aqui

        MENU_TEXT = get_font(120).render("MENU", True, (182, 143, 64))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BOTAO = Botao(image=pg.image.load("Dados/imagens_fontes/Play Rect.png"), pos=(640, 250), # Modificado aqui
                             text_input="JOGAR", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")
        OPTIONS_BOTAO = Botao(image=pg.image.load("Dados/imagens_fontes/Options Rect.png"), pos=(640, 400), # Modificado aqui
                                text_input="ESTATÍSTICAS", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")
        SAIR_BOTAO = Botao(image=pg.image.load("Dados/imagens_fontes/Quit Rect.png"), pos=(640, 550), # Modificado aqui
                             text_input="SAIR", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")

        TELA.blit(MENU_TEXT, MENU_RECT)

        for botao in [PLAY_BOTAO, OPTIONS_BOTAO, SAIR_BOTAO]:
            botao.trocarCor(MENU_MOUSE_POS)
            botao.atualizar(TELA)

        for event in pg.event.get(): # Modificado aqui
            if event.type == pg.QUIT: # Modificado aqui
                pg.quit() # Modificado aqui
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: # Modificado aqui
                if PLAY_BOTAO.checarPorMouse(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BOTAO.checarPorMouse(MENU_MOUSE_POS):
                    options()
                if SAIR_BOTAO.checarPorMouse(MENU_MOUSE_POS):
                    sair()

        pg.display.update() # Modificado aqui

main_menu()