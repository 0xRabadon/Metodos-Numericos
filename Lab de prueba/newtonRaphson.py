'''
Luis Ovalle Grupo 3 (creo)
'''

def f(c):
    return W - (Q * c) - (k * V * (c**0.5))

def df(c):
    return -Q - (k * V * (1 / (2 * (c**0.5))))

def Newton_Raphson(p0, TOL, n0):
    k = 1
    while (k <= n0):
        p = p0 - (f(p0)/df(p0))
        if (abs(p-p0) < TOL):
            print(f"Procedimiento completado exitosamente: {p}")
            return
        k += 1
        p0 = p
    print(f"El metodo falló despues de N0 iteraciones:\nN0 = {n0}")
    return

if __name__ == "__main__":

    # Valores
    V = 1*(10**6)
    Q = 1*(10**5)
    W = 1*(10**6)
    k = 0.25
    
    # Parametros
    p0 = 4 # Aprox. Inicial
    TOL = 10**(-6)# Tolerancia
    n0 = 1000 # N° max. de iteraciones
    
    Newton_Raphson(p0, TOL, n0)