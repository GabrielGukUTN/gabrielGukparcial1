'''
1. Crear una función llamada aplicarAumento que reciba como parámetro 
el precio de un producto y devuelva el valor del 
producto con un aumento del 5%. Realizar la llamada desde el main.
'''


def aplicar_aumento(precio:int, aumento:int )->int:
    resultado = precio + aumento
    return resultado

sumar_aumento = aplicar_aumento( 20,0.05)

print('El aumento es:', sumar_aumento)
