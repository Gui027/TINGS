# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
# https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print('Formato inválido', file=sys.stderr)

    try:
        with open(path_file, 'r') as arquivo:
            news = arquivo.read()
            news_formated = news.split('\n')

            return news_formated
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
