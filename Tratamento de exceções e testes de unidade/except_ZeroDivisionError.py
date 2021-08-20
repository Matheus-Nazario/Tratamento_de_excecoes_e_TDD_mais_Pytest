# Realizar a divisão de dois números inteiros positivos
# Identificar e tratar os possíveis erros.


try:
    a = int(input("Informe um número inteiro positivo: "))
    b = int(input("Informe um número inteiro positivo: "))
    if a < 0 or b < 0:  # valida se os numeros são positivos
        raise TypeError  # gera uma exceçaõ se for negativo
    c = a / b
    print("Resultado da divisão: ", c)
except ZeroDivisionError:
    print("Ocorreu uma divisão por zero")
except ValueError:
    print("O valor informado é invalido")
except TypeError:
    print("O numero deve ser positivo")
except Exception:  # exceção generia
    print("ERRO inesperado")
else:  # é executado quando não há exceção
    print("Programa executado com sucesso")
finally:  # é executado sempre
    print("Obrigado por utilizar esse sistema")
