# https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):

    for i in instance._data:
        while i['nome_do_arquivo']:
            if i['nome_do_arquivo'] == path_file:
                return None

    print_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(print_file)
    return sys.stdout.write(str(print_file))


def remove(instance):
    if len(instance) < 1:
        return print('Não há elementos', file=sys.stdout)
    else:
        path_file = instance.dequeue()['nome_do_arquivo']
        return print(
            f'Arquivo {path_file} removido com sucesso', file=sys.stdout
        )


def file_metadata(instance, position):
    while position > (len(instance) - 1):
        return print('Posição inválida', file=sys.stderr)
    else:
        path_file = instance.search(position)
    # print_file = {
    #     "nome_do_arquivo": path_file
    #     # "qtd_linhas": len(path_file),
    #     # "linhas_do_arquivo": ...
    # }
    return print(path_file, file=sys.stdout)
