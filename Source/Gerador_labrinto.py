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

    def desenhar_mapa(self, TELA, margem_x=0, margem_y=0):
        for y in range(self.altura):
            for x in range(self.largura):
                if self.mapa[y][x] == '#':
                    cor = (0, 180, 0)  # parede (preto)
                elif self.mapa[y][x] == 'S':
                    cor = (255, 0, 0)
                elif self.mapa[y][x] == 'E':
                    cor = (0,255,0)
                else:
                    cor = (255, 255, 255)  # chão (branco)

                pygame.draw.rect(
                    TELA,
                    cor,
                    pygame.Rect(
                        margem_x + x * self.tamanho_celula,
                        margem_y + y * self.tamanho_celula,
                        self.tamanho_celula,
                        self.tamanho_celula
                    )
                )


    def rodar(self, TELA):
        
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            TELA.fill(self.COR_PAREDE)
            self.desenhar_mapa(TELA)
            pygame.display.flip()
        pygame.quit()

    
    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            for linha in self.mapa:
                arquivo.write("".join(linha) + "\n")


def desenhar_mapa_pronto(lab_string_inteiro, tamanho_celula, TELA):
    largura_lab = len(lab_string_inteiro[0])
    altura_lab = len(lab_string_inteiro)
    
    # Calcular margens para centralizar o labirinto na tela
    #margem_x = (TELA.get_width() - largura_lab * tamanho_celula) // 2
    #margem_y = (TELA.get_height() - altura_lab * tamanho_celula) // 2

    for i, linha in enumerate(lab_string_inteiro):
        for x in range(len(linha)):
            rect = pygame.Rect(
                margem_x + x * tamanho_celula,
                margem_y + i * tamanho_celula,
                tamanho_celula,
                tamanho_celula
            )
            if linha[x] == '#':
                pygame.draw.rect(TELA, (40, 90, 0), rect)
            elif linha[x] == '.':
                pygame.draw.rect(TELA, (255, 255, 255), rect)
            elif linha[x] == 'E':
                pygame.draw.rect(TELA, (0, 255, 0), rect)
            elif linha[x] == 'S':
                pygame.draw.rect(TELA, (255, 0, 0), rect)


#pra chamar essa função:
#lab = Labirinto(x, y) #lembra que o labirinto tem que ter largura e altura ímpares
#lab.gerar_labirinto()
#lab.rodar()