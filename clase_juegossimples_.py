# -*- coding: utf-8 -*-
"""Clase_JuegosSimples .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17JsRQup-VUWJ-Ru8j7t-sBr-O89Tbh3G
"""

import random

opciones = ["cara", "cruz"]
opcion_pc= random.choice(opciones)


while True:
  opcion_usuario = input("Quieres jugar con cruz o cruz: ").lower()

  if opcion_usuario != "cara" and opcion_usuario != "cruz":
    print("No te hagas el vivo, te dije que eligas entre cara o cruz...")
  else:
    break

if opcion_usuario == opcion_pc:
  print("Ganaste campeon!")
else:
  print("Perdiste!")

import random

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 30)

intentos = 5

print("Estoy pensando en un número entre 1 y 30. Solo tienes 30 intentos... Adivina cuál es!")

# Bucle para que el jugador siga adivinando
while True:
    intento = int(input("Ingresa tu adivinanza: "))
    intentos -= 1


    if intento < numero_secreto:
        if intentos == 0:
          print(f"Perdiste, te quedaste sin intentos. El numero era {numero_secreto}.")
          break
        print(f"El número es más grande que {intento}. Te quedan  solo {intentos} intentos")
    elif intento > numero_secreto:
        if intentos == 0:
          print(f"Perdiste, te quedaste sin intentos. El numero era {numero_secreto}.")
          break
        print(f"El número es más pequeño que {intento}. Te quedan  solo {intentos} intentos")
    else:
        print(f"¡Correcto! Adivinaste el número {numero_secreto}, en {intentos} intentos.")
        break

import random

# Opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Opción de la computadora
opcion_pc = random.choice(opciones)

# Pregunta al jugador su elección
while True:
    opcion_usuario = input("Elige: piedra, papel o tijera: ").lower()

    if opcion_usuario not in opciones:
        print("No te hagas el vivo, te dije que eligas entre piedra, papel o tijera.")
    else:
        break

print(f"Computadora eligió: {opcion_pc}")

# Determinando el ganador
if opcion_usuario == opcion_pc:
    print("¡Es un empate!")
elif (opcion_usuario == "piedra" and opcion_pc == "tijera") or  (opcion_usuario == "papel" and opcion_pc == "piedra") or (opcion_usuario == "tijera" and opcion_pc == "papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")