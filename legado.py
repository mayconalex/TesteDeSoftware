TIPO_COMUM = 1
TIPO_PRATA = 2
TIPO_OURO = 3


def calcular(tipo_cliente, valor_compra):
    if tipo_cliente == TIPO_COMUM:  # 1
        return valor_compra  # 2

    if tipo_cliente == TIPO_PRATA:  # 3
        if valor_compra > 100:  # 4
            return valor_compra * 0.9  # 5
        else:  # 6
            return valor_compra  # 6

    if tipo_cliente == TIPO_OURO:  # 7
        return valor_compra * 0.8  # 8

    return valor_compra  # 9
