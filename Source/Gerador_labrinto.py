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
    

    def verificar_direcao(self, direita, esquerda, baixo , cima): #passar os 4 pontos diretamente adjacentes ao ponto atual
        #verificar se ao redor do ponto só existem dois caminhos 
        ocupados = 0
        if direita == ".":
            ocupados += 1
        if esquerda == ".":     
            ocupados == 1 
        if baixo == ".":
            ocupados += 1
        if cima == ".":
            ocupados += 1
        return ocupados <= 1
    
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
        contador = 0
        #começar em ponto aleatorio
        x = 1
        y = altura//2
        self.matriz[y][0] = "E"
        self.matriz[y][1] = "."
        tamanho = r.randint(1, (largura * altura) // 6)
        i=0
        while i < tamanho:
            direcao = self.gerar_direcao()  #verificar se a direcao é valida. não é uma parede e nem ligada a dois caminhos
            if direcao == "cima":
                y += 1
                if y < altura - 2 and self.verificar_direcao(self.matriz[y][x+1], self.matriz[y][x - 1], self.matriz[y - 1][x], self.matriz[y + 1][x]) and self.matriz[y][x] == " ":
                    i+=1
                    print(f"Direção: {direcao}, Posição: ({x}, {y})")
                else:
                    y -= 1
            elif direcao == "baixo":
                y -= 1
                if y > 0 and self.verificar_direcao(self.matriz[y][x+1], self.matriz[y][x - 1], self.matriz[y - 1][x], self.matriz[y + 1][x]) and self.matriz[y][x] == " ":
                    i+=1
                    print(f"Direção: {direcao}, Posição: ({x}, {y})")
                else:
                    y += 1
            elif direcao == "esquerda":
                x -= 1
                if x > 1 and self.verificar_direcao(self.matriz[y][x + 1], self.matriz[y][x - 1], self.matriz[y - 1][x], self.matriz[y + 1][x]) and self.matriz[y][x] == " ":
                    i+=1
                    print(f"Direção: {direcao}, Posição: ({x}, {y})")
                else:
                    x += 1
            elif direcao == "direita":
                x += 1
                if x <= largura - 2 and self.verificar_direcao(self.matriz[y][x + 1], self.matriz[y][x - 1], self.matriz[y - 1][x], self.matriz[y + 1][x]) and self.matriz[y][x] == " ":
                    i+=1
                    print(f"Direção: {direcao}, Posição: ({x}, {y})")
                else:
                    x -= 1
            self.matriz[y][x] = "."
        self.matriz[y][x] = "S"
        return self.matriz            


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