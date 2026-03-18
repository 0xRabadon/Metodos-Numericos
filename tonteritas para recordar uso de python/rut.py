def verificarRUT(list_RUT):
    sum = 0
    j = 2
    for i in range (7,-1,-1):
        sum = sum + list_RUT[i]*j
        j += 1
        if j == 8:
            j = 2
    verificador = 11 - (sum % 11)
    if verificador == 11:
        verificador = 0
    elif verificador == 10:
        verificador = 'K'
    return verificador

print("Ingrese su rut sin digito verificador:")
x = input()
RUT = [int(i) for i in str(x)]
ultimo = verificarRUT(RUT)
print("El RUT '" + str(x) + "' tiene como digito verificador: -" + str(ultimo))

