# Programa creado por Francisco Sánchez M.

from datetime import datetime
import time

# Determinar despedida según hora
hora_actual = datetime.now().hour

if 6 <= hora_actual < 12:
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
run=input("Ingresa el RUN que deseas calcular, sea de 7 o 8 dígitos (sin puntos/guión y dìgito verificador, ejemplo: 21123456): ")
print('')

# Verificación de input
if not run.isdigit() or len(run) < 7 or len(run) > 8:
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
    
    # Función para dar formato al RUN con puntos
    def formatear_run(run):
        if len(run) == 7:
            return f"{run[0]}.{run[1:4]}.{run[4:]}"
        elif len(run) == 8:
            return f"{run[:2]}.{run[2:5]}.{run[5:]}"
        else:
            return run

    # Formatear RUN con puntos
    run_formateado = formatear_run(run)

    run_completo = f"{run_formateado}-{dv}"
    print(f"El digito verificador del RUN es: {dv}")
    print(f'\nPor lo tanto, el rut completo es: {run_completo}')
    print(f"\nGracias por utilizar el programa! {despedida}")
