from Source import Menu
#importam os módulos dos arquivos necessários

from pathlib import Path
base_dir = Path.cwd()
#cria o caminho base do diretório atual


Menu.main_menu(base_dir/'Dados'/'jogadores.txt', base_dir)
#chama a função do menu principal