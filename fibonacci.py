def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

x = int(input("Ingrese el numero de succesiones:"))

print("si fueran " + str(x) +" sucesiones, entonces el resultado seria: " + str(fibonacci(x)))
