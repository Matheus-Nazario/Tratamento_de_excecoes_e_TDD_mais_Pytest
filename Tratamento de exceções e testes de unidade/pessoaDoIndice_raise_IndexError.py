"""
Exercício 03
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário.
a) Criar uma função que recebe como parâmetro de entrada a lista
e uma posição (índice) dessa lista e retorna o nome que
está nessa posição.
- Essa função deve gerar e tratar uma exceção do tipo
IndexError caso o índice não
exista na lista.
"""


def pessoaDoIndice(listaDePessoa, indice):

    try:
        total = len(listaDePessoa) - 1
        i = 0

        while i <= total:
            if i == indice:
                print(listaDePessoa[i])
            i += 1
        if indice > total:
            raise IndexError

    except IndexError:
        print("Não existe o índice")


pessoaDoIndice(["matheus", "marcello", "maria", "Grey", "isis"], 2)
