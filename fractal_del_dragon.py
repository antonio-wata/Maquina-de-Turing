def curva(n):
    if n == 0:
        return []
    cadena = curva(n - 1) 
    cadena_reversa = cadena[::-1]
    cambio = ['L' if rotacion == 'R' else 'R' for rotacion in cadena_reversa]
    return cadena + ['L'] + cambio

for i in range(5):
    print("la secuencia: ", i, " es ", curva(i))