import math
def pot2(n):
    """Retorna a pot de 2 mais proxima do numero n"""
    numero = None
    contador = 0
    while True:
        numero = math.pow(2,contador)
        if numero > n :
            numero = math.pow(2,contador-1)
            break
        contador += 1
    return numero
    
def roda(n):
    """n  seria o tamanho da roda"""
    tamanho = float(n)
    inicio = 1.0
    resto = tamanho
    atual = inicio
    pot_mais_proxima = pot2(tamanho)
    if tamanho <= 2.0 :
        return inicio
    else:
        while True:
            if resto == pot_mais_proxima:
                break
            elif atual % 2.0 == 0.0:
                resto -= 1
            
            atual += 1
    return atual

        
# Coloque a quantidade de participantes da roda dentro da funcao roda()
print(roda(2020))
    
   



    



