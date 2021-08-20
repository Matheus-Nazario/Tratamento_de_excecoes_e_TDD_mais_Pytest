from modulo import fatorial, soma


def teste_soma():
    try:
        resultado = soma(100, 200)
        assert resultado == 300
        assert resultado > 0
        assert resultado % 10 == 0
        print("OK")
    except AssertionError:
        print("Erro na funcao soma")

    try:
        resultado = soma(-100, -100)
        assert resultado == -200
        print("OK")
    except AssertionError:
        print("Erro na funcao soma")


def teste_fatorial():
    try:
        resultado = fatorial(5)
        assert resultado == 120
        print("OK")
    except AssertionError:
        print("Erro na funcao fatorial")


teste_soma()
teste_fatorial()
