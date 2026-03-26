def newton(p0, tol, n0):
    # Paso 1
    i = 1

    # Paso 2
    while i <= n0:
        # Paso 3
        p = p0 - (f(p0)/df(p0))
        
        # Paso 4
        if abs(p-p0) < tol:
            return p
        
        # Paso 5
        i = i + 1
        
        # Paso 6
        p0 = p
    
    # Paso 7
    print (f"el metodo fracaso despues de N0 iteraciones \n N0 = '{n0}'")
    return

f = 2
df = 2

if __name__ == "__main__":
    x = newton()
    