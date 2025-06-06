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
    

    def verificar_direcao(self, diereita, esquerda, baixo , cima): #passar os 4 pontos diretamente adjacentes ao ponto atual
        #verificar se ao redor do ponto só existem dois caminhos 
        livres = 0
        if diereita == ".":
            livres += 1
        if esquerda == ".":     
            livres += 1 
        if baixo == ".":
            livres += 1
        if cima == ".":
            livres += 1
        return livres <= 2
    
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
        #começar em ponto aleatorio
        x = 2
        y = altura//2
        self.matriz[y][0] = "E"
        self.matriz[y][1] = "."
        tamanho = r.randint(1, (largura * altura) // 6)
        i =0
        while i <= 1:
            direcao = self.gerar_direcao()#verificar se a direcao é valida. não é uma parede e nem ligada a dois caminhos
            if i == 0:
                x += 1
                i+=1
            elif direcao == "cima" and y > 1 and self.verificar_direcao(self.matriz[y][x], self.matriz[y][x - 1], self.matriz[y + 1][x], self.matriz[y - 1][x - 1]) and self.matriz[y][x] == " ":
                y -= 1
                i+=1
            elif direcao == "baixo" and y < altura - 2 and self.verificar_direcao(self.matriz[y][x], self.matriz[y][x + 1], self.matriz[y + 1][x], self.matriz[y - 1][x]) and self.matriz[y][x] == " ":
                y += 1
                i+=1
            elif direcao == "esquerda" and x >= 1 and self.verificar_direcao(self.matriz[y][x - 1], self.matriz[y][x + 1], self.matriz[y + 1][x], self.matriz[y - 1][x]) and self.matriz[y][x] == " ":
                x -= 1
                i+=1
            elif direcao == "direita" and x <= largura - 2 and self.verificar_direcao(self.matriz[y][x + 1], self.matriz[y][x - 1], self.matriz[y + 1][x], self.matriz[y - 1][x]) and self.matriz[y][x] == " ":
                x += 1
                i+=1
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
    print()  # Nova linha após cada linha do labirinto