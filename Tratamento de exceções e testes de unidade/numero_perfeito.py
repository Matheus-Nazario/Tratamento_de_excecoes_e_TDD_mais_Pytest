def eh_perfeito(n):
    tipoN = type(n)
    tipoInt = int
    soma = 0
    if tipoN == tipoInt:
        for i in range(1, n):
            if n % i == 0:
                soma = soma + i
        if n == soma:
            return True
        else:
            return False
    else:
        return False
