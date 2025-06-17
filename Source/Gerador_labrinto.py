import pygame
import random


largura = 31  # número de células (é importante ser impar pq tem hora que o codigo divide coisa por 2)
altura = 31
tamanho_celula = 20  # tamanho de cada quadrado em pixels

# Novo tamanho da janela
largura_janela = 600
altura_janela = 600

# Calcula o tamanho da célula para caber dentro da janela
tamanho_celula_x = largura_janela // largura
tamanho_celula_y = altura_janela // altura
tamanho_celula = min(tamanho_celula_x, tamanho_celula_y)



# Cores
COR_PAREDE = (40, 90, 0)     
COR_CAMINHO = (255, 255, 255)
COR_SAIDA = (255, 0, 0)   
COR_ENTRADA = (0, 255, 0)  

# Gerar o labirinto
mapa = [['#' for a in range(largura)] for b in range(altura)]

def escavar(x, y):
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    random.shuffle(movimentos)
    for dx, dy in movimentos:
        nx, ny = x + dx*2, y + dy*2
        if 0 < nx < largura-1 and 0 < ny < altura-1:
            if mapa[ny][nx] == '#':
                mapa[y + dy][x + dx] = '.'
                mapa[ny][nx] = '.'
                escavar(nx, ny)

# Começo da escavação
mapa[1][1] = '.'
escavar(1, 1)

# Criar entrada (no canto superior)
for i in range(largura):
    if mapa[1][i] == '.':
        mapa[1][i] = 'E'
        break

mapa[altura - 2][largura-2] = 'S'

# Inicializar Pygame
pygame.init()
#criar a tela com base no tamanho do labirinto
screen = pygame.display.set_mode((largura * tamanho_celula, altura * tamanho_celula), pygame.RESIZABLE)
pygame.display.set_caption("Labirinto")

# Função para desenhar o labirinto no pygame
def desenhar_mapa():
    for y in range(altura):
        for x in range(largura):
            rect = pygame.Rect(x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula)
            if mapa[y][x] == '#':
                pygame.draw.rect(screen, COR_PAREDE, rect)
            elif mapa[y][x] == '.':
                pygame.draw.rect(screen, COR_CAMINHO, rect)
            elif mapa[y][x] == 'E':
                pygame.draw.rect(screen, COR_ENTRADA, rect)
            elif mapa[y][x] == 'S':
                pygame.draw.rect(screen, COR_SAIDA, rect)

# Loop para a geração
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    screen.fill(COR_PAREDE)
    desenhar_mapa()
    pygame.display.flip()

pygame.quit()
