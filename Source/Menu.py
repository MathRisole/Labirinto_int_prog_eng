#Importando as bibliotecas necessarias
import pygame as pg

#configuração inicial do menu
pg.init() 
largura, altura = 1000, 760
screen = pg.display.set_mode((largura, altura))
rodando = True

while rodando:                            #loop tela
    for event in pg.event.get():          #definir eventos no loop
        print(event)                      
        if event.type == pg.QUIT:         #sair ao apertar no X
            rodando = False




#definindo cores
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pg.quit()