#Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.
total = 0
while True:
    i = input("ingrese un numero (utilise 0 para finalizar)")
    if i == "0":
        break
    total += int(i)
print("Total:", total)
