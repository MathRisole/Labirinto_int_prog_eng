from Source import Gerador_labrinto as GL
from Source import Movimento_e_colisao as MC
from Source import Menu
from pathlib import Path
base_dir = Path.cwd()

lab_aleatorio = GL.Labirinto(55, 31)

Menu.main_menu(lab_aleatorio, base_dir/'Dados'/'jogadores.txt')