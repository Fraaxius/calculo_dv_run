from datetime import datetime
import time

# Programa creado por Francisco Sánchez M.

# Determinar despedida según hora
hora_actual = datetime.now().hour

if 7 <= hora_actual < 12:
    despedida = "Buenos días. :)"
elif 12 <= hora_actual < 18:
    despedida = "Buenas tardes. :)"
else:
    despedida = "Buenas noches. :)"

# Variables
run = 0
runinvertido = 0
dv = ''

print ('Hola! Bienvenido al programa de Cálculo de Dígito Verificador.\n')
run=input("Ingresa el RUN que deseas calcular (sin dìgito verificador, ejemplo: 21123456): ")
print('')

# Verificación de input
if not run.isdigit():
    print("\nError: La entrada no es válida. Verifica si escribiste el RUN con el formato antes mencionado.")
else:
    runinvertido = run[::-1]
    print ('Calculando...\n')
    time.sleep(3)

    # Secuencia de multiplicación
    multiplicacion = [2, 3, 4, 5, 6, 7]

    # Cálculo de suma de las multiplicaciones
    suma = 0
    for i in range(len(runinvertido)):
        digito = int(runinvertido[i])
        peso = multiplicacion[i % len(multiplicacion)]
        suma += digito * peso
    
    # Calculo de dígito verificador (finalmente)
    residuo = suma % 11
    dv = 11 - residuo

    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = 'K'
    
    print(f"El digito verificador del RUN es: {dv}")
    print(f"\nGracias por utilizar el programa! {despedida}")
