import numero_perfeito


def primeiro_teste():
    try:
        retorno = numero_perfeito.eh_perfeito(6)
        assert retorno is True
        print("Primeiro Teste Correto")
    except AssertionError:
        print("Primeiro Teste com Erro")


def segundo_teste():
    try:
        retorno = numero_perfeito.eh_perfeito(8128)
        assert retorno is True
        print("Segundo Teste Correto")
    except AssertionError:
        print("Segundo Teste com Erro")


def terceiro_teste():
    try:
        retorno = numero_perfeito.eh_perfeito(100)
        assert retorno is False
        print("Terceiro Teste Correto")
    except AssertionError:
        print("Terceiro Teste com Erro")


def quarto_teste():
    try:
        retorno = numero_perfeito.eh_perfeito(1)
        assert retorno is False
        print("Quarto Teste Correto")
    except AssertionError:
        print("Quarto Teste com Erro")


# O número zero não é perfeito
def quinto_teste():
    try:
        retorno = numero_perfeito.eh_perfeito(0)
        assert retorno is False
        print("Quinto Teste Correto")
    except AssertionError:
        print("Quinto Teste com Erro")


def sexto_teste():
    try:
        retorno = numero_perfeito.eh_perfeito(-6)
        assert retorno is False
        print("Sexto Teste Correto")
    except AssertionError:
        print("Sexto Teste com Erro")


primeiro_teste()
segundo_teste()
terceiro_teste()
quarto_teste()
quinto_teste()
sexto_teste()
