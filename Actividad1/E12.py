# Leer las horas trabajadas y la tarifa por hora desde la entrada estándar
horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

# Calcular el salario bruto multiplicando las horas trabajadas por la tarifa por hora
salario_bruto = horas_trabajadas * tarifa_por_hora

# Calcular la retención en la fuente, que es el 12.5% del salario bruto
retencion_fuente = salario_bruto * 0.125

# Calcular el salario neto restando la retención en la fuente al salario bruto
salario_neto = salario_bruto - retencion_fuente

# Mostrar el salario bruto, la retención en la fuente y el salario neto
print("SALARIO BRUTO:", salario_bruto)
print("RETENCIÓN EN LA FUENTE:", retencion_fuente)
print("SALARIO NETO:", salario_neto)
