from main import classifica_triangulo

# Testes para triângulos válidos
def test_triangulo_equilatero():
    assert classifica_triangulo(7, 7, 7) == "Equilátero"

def test_triangulo_isosceles_1():
    assert classifica_triangulo(5, 5, 6) == "Isósceles"

def test_triangulo_isosceles_2():
    assert classifica_triangulo(6, 5, 5) == "Isósceles"

def test_triangulo_isosceles_3():
    assert classifica_triangulo(5, 6, 5) == "Isósceles"

def test_triangulo_escaleno():
    assert classifica_triangulo(3, 4, 5) == "Escaleno"

# Testes para casos que NÃO são triângulos
def test_nao_triangulo_desigualdade():
    assert classifica_triangulo(1, 2, 4) == "Não é um triângulo"

def test_nao_triangulo_degenerado():
    assert classifica_triangulo(1, 2, 3) == "Não é um triângulo"

# Testes para entradas inválidas
def test_lados_com_zero():
    assert classifica_triangulo(1, 2, 0) == "Lados devem ser positivos."

def test_lados_negativos():
    assert classifica_triangulo(1, -2, 3) == "Lados devem ser positivos."

def test_lados_nao_numericos():
    assert classifica_triangulo('a', 'b', 'c') == "Lados devem ser numéricos."