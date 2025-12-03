def Answer(i):
    # Código refatorado
    resultado = ""
    
    if i % 3 == 0:
        resultado += "fizz"
    
    if i % 5 == 0:
        resultado += "buzz"
        
    if resultado == "":
        return str(i)
        
    return resultado