# Ingresar datos del empleado
codigo_empleado = input("Ingrese el código del empleado: ")
nombres = input("Ingrese los nombres del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
valor_hora_trabajada = float(input("Ingrese el valor de la hora trabajada: "))
porcentaje_retencion = float(input("Ingrese el porcentaje de retención en la fuente (%): "))

# Calcular el salario bruto multiplicando horas trabajadas por valor de hora trabajada
salario_bruto = horas_trabajadas * valor_hora_trabajada

# Calcular la retención en la fuente
retencion_fuente = salario_bruto * (porcentaje_retencion / 100)

# Calcular el salario neto restando la retención en la fuente al salario bruto
salario_neto = salario_bruto - retencion_fuente

# Mostrar la información del empleado, salario bruto y salario neto
print("Código del empleado:", codigo_empleado)
print("Nombres del empleado:", nombres)
print("Salario Bruto:", salario_bruto)
print("Salario Neto:", salario_neto)
