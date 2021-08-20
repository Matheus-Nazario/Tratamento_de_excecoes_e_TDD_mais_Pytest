"""
Crie um dicionário para armazenar uma listagem de alunos.
a) Utilize como chave o RA do aluno e como valor o nome do aluno.
b) Os dados devem ser informados pelo usuário
c) O RA de cada aluno deve ser composto por um número inteiro de
exatamente 7 dígitos.
- Caso o RA informado não esteja no formato correto, deve s
er gerada uma exceção
do tipo ValueError
- Caso o RA informado já exista no dicionário, deve ser gerada uma
exceção do tipo
TypeError
Observação: Você pode utilizar o código abaixo como exemplo
e alterá-lo para gerar e tratar as
exceções solicitadas.
"""

alunos = {}
for i in range(5):
    try:
        ra = int(input("RA: "))
        strRA = str(ra)
        tamanho = len(strRA)
        if tamanho != 7:
            raise ValueError
        elif ra in alunos:
            raise TypeError
        else:
            nome = input("Nome: ")
            alunos[ra] = nome
            print(alunos)

    except ValueError:
        print("O RA informado não esteja no formato correto")
    except TypeError:
        print("O RA já existe")
