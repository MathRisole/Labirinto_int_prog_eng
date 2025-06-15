#Importando as bibliotecas necessarias
import pygame as pg
from pygame.locals import *

#configuração inicial do menu
pg.init() 
largura, altura = 1360, 700
screen = pg.display.set_mode((largura, altura))
rodando = True
pg.display.set_caption("Jogo")

#criar a classe de um botão
class Botao():
    def __init__(self, imagem, pos, text_input, font, base_color, hovering_color):
        self.imagem = imagem
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.imagem is None:
            self.imagem = self.text
        self.rect = self.imagem.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def atualizar(self, screen):
        if self.imagem is not None:
            screen.blit(self.imagem, self.rect)
        screen.blit(self.text, self.text_rect)

    def checarPorMouse(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def trocarCor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)








#definindo cores e imagens
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BG = BLUE


'''
def main_menu(): # Main Menu Screen
    pg.display.set_caption("Menu")

    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_botao = Botao(imagem=pg.imagem.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="JOGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_botao = Botao(imagem=pg.imagem.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPÇÕES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_botao = Botao(imagem=pg.imagem.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for botao in [PLAY_botao, OPTIONS_botao, QUIT_botao]:
            botao.changeColor(MENU_MOUSE_POS)
            botao.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_botao.checarPorMouse(MENU_MOUSE_POS):
                    jogar()
                if OPTIONS_botao.checarPorMouse(MENU_MOUSE_POS):
                    opcoes()
                if QUIT_botao.checarPorMouse(MENU_MOUSE_POS):
                    pg.quit()
                    

'''                

""""
while rodando:                            #loop tela
    for event in pg.event.get():          #definir eventos no loop
        print(event)                      
        if event.type == pg.QUIT:         #sair ao apertar no X
            rodando = False


    
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                background = RED
            elif event.key == pg.K_g:
                background = GREEN

    screen.fill(background)                                        #cor da tela
    pg.display.update()
"""