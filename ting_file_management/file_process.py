import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text = txt_importer(path_file)

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }

    instance.enqueue(file)
    sys.stdout.write(str(file))
    return file


def remove(instance):
    if not len(instance):
        sys.stdout.write("Não há elementos\n")
        return None

    file = instance.dequeue()
    file_name = file["nome_do_arquivo"]

    sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    except IndexError:
        sys.stderr.write("Posição inválida")
