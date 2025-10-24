def classifica_triangulo(a, b, c):
    if not all(isinstance(lado, (int, float)) for lado in [a, b, c]):
        return "Lados devem ser numéricos."
    if any(lado <= 0 for lado in [a, b, c]):
        return "Lados devem ser positivos."

    if a + b >= c and a + c >= b and b + c >= a:
        if a == b and b == c:
            return "Equilátero"
        elif a == b or b == c or a == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"