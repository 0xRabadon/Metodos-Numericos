#repaso de python pq Raba se olvido el muy weon XD

print("Hola mundo") # print desde la consola

x = 1 # en python las variables no estan ligadas a un tipo de variable
print(x)
x = "que loco"
print(x)

#Ves, X paso de ser Int a String, no es como en C++, JS o java

x = int(input("Ingresa un numero cualquiera: ")) #ojo que aca input siempre va el tipo de dato, si no se asumira como un str

#Estructura If

if x < 0: #Los if (como toda estructura en python) siempre se finalizan con :
    print("Ingresaste un numero negativo")
elif x>0: # aca existe elif que reemplaza el else if en otros programas
    print("Ingresaste un numero positivo")
else: #tipico else, nada que comentar
    print("Ingresaste 0")
    
#estructura while

while x != 0: #tipico while, no falta explicar mas...
    if x<0:
        x += 1
    else:
        x -= 1
    print(x)
    
#estructura for OJO QUE EL FOR ACA ES DIFERENTE

for i in range (0, 3, 1): # la variable cambiante seria la i, range es el rango y el parentesis seria (inicio, fin, salto)
    print(i)
    
print("look, el salto es cuanto se suma i para llegar al tope, un salto")
    
for i in range (0, 100, 10):
    print(i)
    
#OJO QUE EN PUTHON NO EXISTE EL SWITCH, para eso usas elif

# LISTAS

print("mira, en python existe un arreglo especial llamado listas, son como un arreglo pero puedes meter de todo")

lista = [ "a" , 1,  2, 3, "que loco"]

#para navegar en una lista se usa el for

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
