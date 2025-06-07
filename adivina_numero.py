import random

numero_secreto = random.randint(1, 100)
intentos = 8

print("¡Adivina el número del 1 al 100!")
print("Tienes 8 intentos.")

while intentos > 0:
    entrada = input(f"Intento #{9 - intentos} - Ingresa tu número: ")

    if not entrada.isdigit():
        print("Por favor, ingresa un número válido.")
        continue

    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break
    elif numero < numero_secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")

    intentos -= 1

if intentos == 0:
    print(f"¡Se acabaron los intentos! El número era {numero_secreto}.")
