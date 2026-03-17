def factorial(n):
    if n < 0:
        raise ValueError("n no puede ser negativo")
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
x = int(input("Ingrese un numero postivo: "))
print("el numero " + str(x) + " factorial seria: " + str(factorial(x)))
