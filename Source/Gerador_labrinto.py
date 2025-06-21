import pygame
import random

class Labirinto:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        # Tamanho da janela pode ser fixo ou proporcional
        self.largura_janela = 1280
        self.altura_janela = 720

        # Ajustar o tamanho das células para caber dentro da janela
        tamanho_celula_x = self.largura_janela // largura
        tamanho_celula_y = self.altura_janela // altura
        self.tamanho_celula = min(tamanho_celula_x, tamanho_celula_y)

        # Cores
        self.COR_PAREDE = (40, 90, 0)
        self.COR_CAMINHO = (255, 255, 255)
        self.COR_SAIDA = (255, 0, 0)
        self.COR_ENTRADA = (0, 255, 0)

        # Mapa inicial
        self.mapa = [['#' for _ in range(largura)] for _ in range(altura)]

    def escavar(self, x, y):
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
        random.shuffle(movimentos)
        for dx, dy in movimentos:
            nx, ny = x + dx*2, y + dy*2
            if 0 < nx < self.largura - 1 and 0 < ny < self.altura - 1:
                if self.mapa[ny][nx] == '#':
                    self.mapa[y + dy][x + dx] = '.'
                    self.mapa[ny][nx] = '.'
                    self.escavar(nx, ny)

    def gerar_labirinto(self):
        # Começo da escavação
        self.mapa[1][1] = '.'
        self.escavar(1, 1)

        # Criar entrada
        for i in range(self.largura):
            if self.mapa[1][i] == '.':
                self.mapa[1][i] = 'E'
                break

        # Criar saída
        self.mapa[self.altura - 2][self.largura - 2] = 'S'

    def desenhar_mapa(self, screen):
        for y in range(self.altura):
            for x in range(self.largura):
                rect = pygame.Rect(x * self.tamanho_celula, y * self.tamanho_celula, self.tamanho_celula, self.tamanho_celula)
                if self.mapa[y][x] == '#':
                    pygame.draw.rect(screen, self.COR_PAREDE, rect)
                elif self.mapa[y][x] == '.':
                    pygame.draw.rect(screen, self.COR_CAMINHO, rect)
                elif self.mapa[y][x] == 'E':
                    pygame.draw.rect(screen, self.COR_ENTRADA, rect)
                elif self.mapa[y][x] == 'S':
                    pygame.draw.rect(screen, self.COR_SAIDA, rect)

    def rodar(self, screen):
        
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            screen.fill(self.COR_PAREDE)
            self.desenhar_mapa(screen)
            pygame.display.flip()
        pygame.quit()

    
    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            for linha in self.mapa:
                arquivo.write("".join(linha) + "\n")

# pra chamar essa função:
#lab = Labirinto(x, y) #lembra que o labirinto tem que ter largura e altura ímpares
#lab.gerar_labirinto()
#lab.rodar()