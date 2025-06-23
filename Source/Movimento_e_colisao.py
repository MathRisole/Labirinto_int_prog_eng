import pygame
from Source import Gerador_labrinto as GL

# 1. Velocidade do movimento: mover 1 célula por passo
velocidade = 1  # número de células por movimento

# 2. Controle da taxa de atualização (FPS)
FPS = 10  # máximo de 10 movimentos por segundo

pos_x, pos_y = 1, 1


def pode_mover(x, tamanho_lab_x, y, tamanho_lab_y, labirinto):
    if 0 <= x < tamanho_lab_x and 0 <= y < tamanho_lab_y:
        return labirinto.mapa[y][x] != '#'
    return False

def pode_mover_pronto(x, tamanho_lab_x, y, tamanho_lab_y, caminho_arquivo_fase):
    lab_string_inteiro = caminho_arquivo_fase.read()
    lab_string_separado = lab_string_inteiro.split("\n")
    if 0 <= x < tamanho_lab_x and 0 <= y < tamanho_lab_y:
        return lab_string_separado[y][x] != '#'
    return False

clock = pygame.time.Clock()
rodando = True

def rodar_aleatorio(pos_x, tamanho_lab_x, pos_y, tamanho_lab_y, velocidade, TELA, labirinto):
    teclas = pygame.key.get_pressed()
    novo_x, novo_y = pos_x, pos_y

    # 3. Movimento discreto: mover 1 célula por vez (velocidade=1)
    if teclas[pygame.K_LEFT]:
        if pode_mover(pos_x - velocidade, tamanho_lab_x, pos_y, tamanho_lab_y, labirinto):
            novo_x = pos_x - velocidade
    elif teclas[pygame.K_RIGHT]:
        if pode_mover(pos_x + velocidade, tamanho_lab_x, pos_y, tamanho_lab_y, labirinto):
            novo_x = pos_x + velocidade
    elif teclas[pygame.K_UP]:
        if pode_mover(pos_x, tamanho_lab_x, pos_y - velocidade, tamanho_lab_y, labirinto):
            novo_y = pos_y - velocidade
    elif teclas[pygame.K_DOWN]:
        if pode_mover(pos_x, tamanho_lab_x, pos_y + velocidade, tamanho_lab_y, labirinto):
            novo_y = pos_y + velocidade

    # 4. Colisão simples: só move se a célula destino não for parede
    pos_x, pos_y = novo_x, novo_y

    labirinto.desenhar_mapa(TELA)
    rect_jogador = pygame.Rect(pos_x * labirinto.tamanho_celula, pos_y * labirinto.tamanho_celula, labirinto.tamanho_celula, labirinto.tamanho_celula)
    pygame.draw.rect(TELA, "Azul", rect_jogador)

    pygame.display.flip()
    clock.tick(FPS)  # 2. controla FPS (velocidade do jogo)

def rodar_pronto(pos_x, tamanho_lab_x, pos_y, tamanho_lab_y, velocidade, TELA, lab_linhas, teclas):
    tamanho_celula = min(tamanho_lab_x, tamanho_lab_y)
    novo_x, novo_y = pos_x, pos_y

    if teclas[pygame.K_LEFT]:
        if pode_mover_pronto(pos_x - velocidade, tamanho_lab_x, pos_y, tamanho_lab_y, lab_linhas):
            novo_x = pos_x - velocidade
    elif teclas[pygame.K_RIGHT]:
        if pode_mover_pronto(pos_x + velocidade, tamanho_lab_x, pos_y, tamanho_lab_y, lab_linhas):
            novo_x = pos_x + velocidade
    elif teclas[pygame.K_UP]:
        if pode_mover_pronto(pos_x, tamanho_lab_x, pos_y - velocidade, tamanho_lab_y, lab_linhas):
            novo_y = pos_y - velocidade
    elif teclas[pygame.K_DOWN]:
        if pode_mover_pronto(pos_x, tamanho_lab_x, pos_y + velocidade, tamanho_lab_y, lab_linhas):
            novo_y = pos_y + velocidade

    pos_x, pos_y = novo_x, novo_y

    # Aqui desenha o mapa e o jogador
    GL.desenhar_mapa_pronto(lab_linhas, tamanho_celula, TELA)
    rect_jogador = pygame.Rect(pos_x * tamanho_celula, pos_y * tamanho_celula, tamanho_celula, tamanho_celula)
    pygame.draw.rect(TELA, (66, 135, 245), rect_jogador)

    pygame.display.flip()

    return pos_x, pos_y


def jogar_fase_pronta(pos_x, tamanho_lab_x, pos_y, tamanho_lab_y, velocidade, TELA, caminho_arquivo_fase):
    import pygame
    clock = pygame.time.Clock()
    rodando = True

    # Ler o arquivo da fase só uma vez
    lab_string_inteiro = caminho_arquivo_fase.read()
    lab_linhas = lab_string_inteiro.splitlines()

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False  # Voltar para o menu ao apertar ESC

        teclas = pygame.key.get_pressed()
        pos_x, pos_y = rodar_pronto(pos_x, tamanho_lab_x, pos_y, tamanho_lab_y, velocidade, TELA, lab_linhas, teclas)

        clock.tick(10)  # Controla FPS