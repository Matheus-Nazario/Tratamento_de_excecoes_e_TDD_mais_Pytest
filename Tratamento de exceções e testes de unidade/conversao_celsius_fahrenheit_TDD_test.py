import conversao_celsius_fahrenheit


def segundo_teste():
    try:
        c2 = conversao_celsius_fahrenheit.converte_para_celsius(32)
        assert c2 == 0
        print("segundo Teste Correto")
    except AssertionError:
        print("segundo Teste com Erro")
        print("retorno: ", c2)
        print("esperado", 0)


def primeiro_teste():
    try:
        c = conversao_celsius_fahrenheit.converte_para_fahrenheit(0)
        assert c == 32.0
        print("Primeiro Teste Correto")
    except AssertionError:
        print("Primeiro Teste com Erro")
        print("retorno: ", c)
        print("esperado", 32.0)


primeiro_teste()
segundo_teste()
