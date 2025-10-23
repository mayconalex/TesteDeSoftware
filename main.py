a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilátero.")
    elif a == b or b == c or a == c:
        print("Isósceles.")
    else:
        print("Escaleno.")
else:
    print("Não é um triângulo.")