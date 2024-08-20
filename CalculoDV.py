# Programa hecho por Francisco Sánchez M.

# [WIP]

# Declaración de variables
run = 0
runinvertido = 0

print ('Hola! Bienvenido al programa de Cálculo de Dígito Verificador.\n')
run=input("Ingresa el rut que deseas calcular: ")

runinvertido = run[::-1]

print (f"El RUN invertido es: {runinvertido}")
