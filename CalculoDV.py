# Programa creado por Francisco Sánchez M.

from datetime import datetime
import time

# Colores para la consola (si se soporta)
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Determinar despedida según hora
hora_actual = datetime.now().hour

if 6 <= hora_actual < 12:
    despedida = f"{Color.OKGREEN}Buenos días. {Color.ENDC}:)"
elif 12 <= hora_actual < 18:
    despedida = f"{Color.OKCYAN}Buenas tardes. {Color.ENDC}:)"
else:
    despedida = f"{Color.OKBLUE}Buenas noches. {Color.ENDC}:)"

# Variables
run = ''
runinvertido = ''
dv = ''

print(f"\n{Color.HEADER}¡Hola! Bienvenido al programa de Cálculo de Dígito Verificador.{Color.ENDC}\n")

# Solicitar ingreso de RUN
run = input(f"{Color.OKBLUE}Ingresa el RUN que deseas calcular (7 u 8 dígitos, sin puntos/guión ni dígito verificador, por ejemplo: 21123456): {Color.ENDC}")

# Verificación de input
if not run.isdigit() or len(run) < 7 or len(run) > 8:
    print(f"\n{Color.FAIL}Error: La entrada no es válida. Verifica si escribiste el RUN con el formato indicado.{Color.ENDC}")
else:
    runinvertido = run[::-1]
    print(f'\n{Color.OKGREEN}Calculando...\n{Color.ENDC}')
    time.sleep(3)

    # Secuencia de multiplicación
    multiplicacion = [2, 3, 4, 5, 6, 7]

    # Cálculo de suma de las multiplicaciones
    suma = 0
    for i in range(len(runinvertido)):
        digito = int(runinvertido[i])
        peso = multiplicacion[i % len(multiplicacion)]
        suma += digito * peso
    
    # Cálculo del dígito verificador
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

    # Mostrar resultados
    print(f"{Color.OKGREEN}El dígito verificador del RUN es: {Color.BOLD}{dv}{Color.ENDC}")
    print(f'\n{Color.OKCYAN}Por lo tanto, el RUT completo es: {Color.BOLD}{run_completo}{Color.ENDC}')
    print(f"\n{Color.HEADER}¡Gracias por utilizar el programa! {despedida}{Color.ENDC}")
