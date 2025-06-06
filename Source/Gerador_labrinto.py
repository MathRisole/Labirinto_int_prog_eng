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

def criar_esqueleto_labrinto(largura, altura):
            #Criando uma matriz para o labirinto
            labirinto = []
            for i in range(altura):
                linha = []
                for j in range(largura):
                    if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:  
                        linha.append("#")  # Paredes
                    else:
                        linha.append("_")  # Espaços vazios/ nao gerados . "." == espaço vazio gerado 
                labirinto.append(linha)
            return labirinto
#Criando a classe do labirinto
class Labirinto:
    def __init__(self, largura, altura):
        #atributos do labirinto:
        self.largura = largura
        self.altura = altura
        #self.dificuldade = xxxx  # Pode ser adicionado depois
        self.labirinto = criar_esqueleto_labrinto(largura, altura)
        self.gerar_caminho()


    #printar bonitinho
    def printBonito(self):
        return "\n".join("".join(linha) for linha in self.labirinto)




    def gerar_direcao():
        direcoes = ["cima", "baixo", "esquerda", "direita"]
        return r.choice(direcoes)
    

    def verificar_direcao(diereita, esquerda, baixo , cima): #passar os 4 pontos diretamente adjacentes ao ponto atual
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
    def gerar_caminho_aleatorio(labirinto, largura, altura):
        caminho =[]
        #começar em ponto aleatorio
        x = r.randint(1, largura - 1)
        y = r.randint(1, altura - 1)
        labirinto[y][x] = "E"
        tamanho = r.randint(1, (largura * altura) // 6)
        for i in range(tamanho):
            direcao = gerar_direcao()#verificar se a direcao é valida. não é uma parede e nem ligada a dois caminhos
            if direcao == "cima" and y > 1 and verificar_direcao(labirinto[y][x], labirinto[y][x - 1], labirinto[y + 1][x], labirinto[y - 1][x - 1]):
                y -= 1
            elif direcao == "baixo" and y < altura - 2 and verificar_direcao(labirinto[y][x], labirinto[y][x + 1], labirinto[y + 1][x], labirinto[y - 1][x]):
                y += 1
            elif direcao == "esquerda" and x > 1 and verificar_direcao(labirinto[y][x - 1], labirinto[y][x + 1], labirinto[y + 1][x], labirinto[y - 1][x]):
                x -= 1
            elif direcao == "direita" and x < largura - 2 and verificar_direcao(labirinto[y][x + 1], labirinto[y][x - 1], labirinto[y + 1][x], labirinto[y - 1][x]):
                x += 1
            caminho[x][y] = "."  # Marcar o caminho
        labirinto[y][x] = "S"
                    


labirinto = Labirinto(21, 21)  
print(labirinto)  
print("-----------------------------------------------------")
labirinto = Labirinto.gerar_caminho_aleatorio(Labirinto.labirinto, Labirinto.largura, Labirinto.altura)
print(labirinto)
