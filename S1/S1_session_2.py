
from datetime import datetime
#Dia 2 - Estructuras de control
## while 

#nombre = input("¿Cómo te llamas?: ")
#print(f"Hola, {nombre}. Adios~")

#Estructura y lógica: while
## while condicion:
#   ...
#   ...
#   if(...):
#        break
##  Cuidado con los bucles infinitos! El truco? La 'actualización/gestión' de la condición
##  break, continue

#Previa del taller de la semana (Mini-taller II): Hacer un pseudoagente estilo consola
## ¿Qué podra hacer este agente por medio de comandos?
### Terminar la sesión - salir
### Responder un ping con un pong - ping
### Contar letras en una palabra: Total, vocales y consonantes - contar

# Login Capa de seguridad
# Roles
user_guest = "invitado"
pass_guest = "invitado"
user_admin = "admin"
pass_admin = "admin1234"

# Sistema de bloqueo
attempt = 0
max_attempt = 3
is_admin = False
success_login = False
rol = None
username = None
# Agente
sistema_activo = True

#Inicio del sistema
print("----- Iniciando el pseudoagente estilo consola -------")
print("""
      Lista de usuarios disponibles
      -Invitado
      -Admin
      """)

while attempt < max_attempt:
    user_input = input ("Ingrese su usuario:")
    pass_input = input ("Ingrese su contraseña:")

    if user_input == user_admin and pass_input == pass_admin:
        is_admin = True
        rol = "admin"
        username = user_admin
        success_login = True
        break
    if user_input == user_guest and pass_input == pass_guest:
        rol = "guest"
        is_admin = False
        username = user_guest
        success_login = True
        break
    else:
        attempt +=1
        counter = max_attempt - attempt
        print(f"Contraseña o usuario invalido te quedan {counter} intentos")
        if counter == 0:
            print("Lo sentimos alcanzaste el maximo de intentos")
            print("[Alerta] Usuario bloqueado. Cerrando sistema.")



while sistema_activo and success_login:
    cmd = input("Agente>: ").lower()

    if cmd == "salir":
        print("------Agente apagado. Vuelve pronto.------")
        sistema_activo = False
    elif cmd == "ping":
        print("pong.")
    elif cmd == "contar":
        palabra = input("Ingrese una palabra: ").lower()
        tot_letras = len(palabra)
        tot_vocales = 0
        tot_cons = 0

        for p in palabra:
            if p in "aeiou":
                tot_vocales += 1
            else:
                tot_cons += 1

        print(f"Palabra ingresada: {palabra}")
        print(f"Total de vocales: {tot_vocales}")
        print(f"Total de consonantes: {tot_cons}")
        print(f"Total de letras: {tot_letras}")
    # Comando fecha hoy Valida si es admin
    elif cmd == "fecha_hoy":
        # valida el rol y el banderín del administrador para mostrar la fecha
        if rol == "admin" and is_admin:
            current_date = datetime.now()
            print("La fecha actual es: ", current_date)
            # Si no cumple con el rol no se le da acceso a la fecha
        else:
            print("[Acceso Denegado] Este comando requiere privilegios de administrador.")
    elif cmd == "validar_pass":
        print("Comando validar contraseña")
        newpass = input("Ingresa una contraseña nueva: ")
        
        # Obtener contraseña actual según el rol
        current_pass = pass_admin if is_admin else pass_guest
        
        # Validación de longitud
        if len(newpass) < 8:
            print("[Error] La contraseña debe tener al menos 8 caracteres.")
        # Validación de que no sea igual al username
        elif newpass == username:
            print("[Error] La contraseña no puede ser igual a tu nombre de usuario.")
        # Validación de que sea diferente a la anterior
        elif newpass == current_pass:
            print("[Error] La contraseña nueva debe ser diferente a la anterior.")
        # Si cumple todos los requisitos
        else:
            if is_admin:
                pass_admin = newpass
                print("[Éxito] La contraseña para el rol administrador ha sido actualizada.")
            else:
                pass_guest = newpass
                print("[Éxito] La contraseña para el rol invitado ha sido actualizada.")
    elif cmd == "calculadora":
        print("Comando calculadora")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == "+":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacion == "-":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacion == "*":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("[Error] No se puede dividir por cero.")

    else:
        print("------Comando desconocido. Intente de nuevo.-------")