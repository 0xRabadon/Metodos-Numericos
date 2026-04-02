
def biseccion(fun, a, b, tol, No):
    """
    fun es la funcion
    a es el tope minimo
    b es el tope maximo
    tol es la tolerancia
    No es el numero maximo de iteraciobes
    """
    # Paso 1 
    i = 1
    fa = fun(a)
    
    # Corroboracion
    if fa*fun(b) > 0:
        raise ValueError("Error: f(a) y f(b) deben tener signos opuestos.")
    
    while i <= No:
    #Paso 3
        p = a + (b-a) /2
        fp = fun(p)
        
    # Paso 4
        if fp == 0 or (b - a)/2 < tol:
            print("Procedimiento completado exitosamente")
            return p
        
    # Paso 5
        i += 1
      
     # Paso 6  
        if fa*fp > 0:
            a = p
            fa = fp
        else:
            b = p
            
    return f"el metodo fracaso despues de {No} iteraciones"
            
def funcionMat(x):
    return x**2 - 2

def main():

    a = 0
    b = 3
    tolerancia = 0.0000001
    max_iter = 100

    resultado = biseccion(funcionMat, a, b, tolerancia, max_iter)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()

