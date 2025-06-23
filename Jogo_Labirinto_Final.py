from Source import Gerador_labrinto as GL
from Source import Movimento_e_colisao as MC
from Source import Menu
#importam os módulos dos arquivos necessários

from pathlib import Path
base_dir = Path.cwd()
#cria o caminho base do diretório atual

lab_aleatorio = GL.Labirinto(55, 31)
#cria um labirinto aleatório com largura e altura pré definidos (ÍMPARES)

Menu.main_menu(base_dir/'Dados'/'jogadores.txt', base_dir)
#chama a função do menu principal