# Leer la edad de Juan desde la entrada estándar
edad_juan = int(input("Ingrese la edad de Juan: "))

# Calcular la edad de Alberto, Ana y la mamá
edad_alberto = (2 * edad_juan) / 3
edad_ana = (4 * edad_juan) / 3
edad_mama = edad_juan + edad_alberto + edad_ana

# Mostrar las edades calculadas
print("Las edades son: Alberto =", edad_alberto, "Juan =", edad_juan, "Ana =", edad_ana, "Mamá =", edad_mama)
