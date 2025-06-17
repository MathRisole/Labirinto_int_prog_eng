#Importando as bibliotecas necessarias
import pygame as pg   
import random as r    
import datetime       #Para registrar tempos
import os             #Gerenciamento de arquivos/diretorios
import pathlib        #Gerenciamento de arquivos/diretorios

#Primeiro criar o esqueleto do labirinto

# caso depois queiram deixar o tamanho do labirinto aleatorio:
# largura = r.randint(min , max) + 1  # Deve ser impar para ter paredes
# altura = r.randint(min, max)  + 1   # Deve ser impar para ter paredes

#Caracteres usados:
#Para o labirinto usarei "#" para paredes e "_" para espaços vazios.(sujeito a mudanças)




#Criando a classe do labirinto

class Labirinto:
    def criar_esqueleto_labrinto(self, largura, altura):
        #Criando uma matriz para o labirinto
        self.matriz = []
        for i in range(altura):
            linha = []
            for j in range(largura):
                if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:  
                    linha.append("#")  # Paredes
                else:
                    linha.append(" ")  # Espaços vazios/ nao gerados . "." == espaço vazio gerado 
            self.matriz.append(linha)
        return self.matriz
    

    def verificar_direcao(self, x, y): #passar o ponto atual
        #verificar se ao redor do ponto só existem dois caminhos 
        #quanto mais pra cima menor o y e mais pra direita maior o x
        ocupados = 0
        direita = self.matriz[y][x + 1] if x + 1 < self.largura else "#"
        esquerda = self.matriz[y][x - 1] if x - 1 >= 0 else "#" 
        cima = self.matriz[y - 1][x] if y - 1 >= 0 else "#"
        baixo = self.matriz[y + 1][x] if y + 1 < self.altura else "#"
        if direita == ".":
            ocupados += 1
        if esquerda == ".":     
            ocupados += 1 
        if baixo == ".":
            ocupados += 1
        if cima == ".":
            ocupados += 1
        if ocupados <= 1:
            return True
        else:
            return False
    
    def __init__(self, largura, altura):
        #atributos do labirinto:
        self.largura = largura
        self.altura = altura
        #self.dificuldade = xxxx  # Pode ser adicionado depois
        self.matriz = self.criar_esqueleto_labrinto(largura, altura)

    def gerar_direcao(self):
        direcoes = ["cima", "baixo", "esquerda", "direita"]
        return r.choice(direcoes)


    def gerar_caminho_aleatorio(self, largura, altura):
        #tratando erro de loop, APAGAR DEPOIS
        continuar = True
        x = 1
        y = 1
        x1 = x
        y1 = y-1
        x2 = x
        y2 = y+1
        x3 = x+1
        y3 = y
        x4 = x-1
        y4 = y
        cima = ["cima", x1, y1]
        baixo =["baixo", x2, y2]
        direita = ["direita", x3, y3]
        esquerda = ["esquerda", x4, y4]
        #começar em ponto aleatorio
        direcoes = [cima , baixo, direita, esquerda]
        self.matriz[1][1] = "E"
        while continuar:
            r.shuffle(direcoes)
            continuar = False
            for i in direcoes:
                x = i[1]
                y = i[2]
                print(x, y)
                if self.verificar_direcao(x, y):
                    self.matriz[y][x] = "."
                    if i[0] == "cima":
                        i[2] -= 1  # Mover para cima
                    elif i[0] == "baixo":
                        i[2] += 1
                    elif i[0] == "direita":
                        i[1] += 1
                    elif i[0] == "esquerda":
                        i[1] -= 1
                    
                    
                    continuar = True
                    print(f"Direção: {i[0]} - Ponto: ({x}, {y})")
                    break
                else:
                    continuar = False
                    print("parar")

labirinto = Labirinto(21, 21) 
for i in range(0, labirinto.altura):
    for j in range(0, labirinto.largura):
        print(labirinto.matriz[i][j], end="")
    print()  # Nova linha após cada linha do labirinto
print("-----------------------------------------------------")
labirinto.matriz = labirinto.gerar_caminho_aleatorio( labirinto.largura, labirinto.altura)

for i in range(0, labirinto.altura):
    for j in range(0, labirinto.largura):
        print(labirinto.matriz[i][j], end="")
    print()  # Nova linha após cada linha do labirinto[]