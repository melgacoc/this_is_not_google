def exists_word(word, instance):
    response = []

    for index in range(len(instance)):
        file = instance.search(index)

        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index, content in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in content.lower():
                result["ocorrencias"].append({"linha": index + 1})

        if result["ocorrencias"]:
            response.append(result)

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
