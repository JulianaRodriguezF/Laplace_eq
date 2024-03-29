# -*- coding: utf-8 -*-
"""Taller3_Electromagnetismo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/141aStLhRVJJYQlm4mb2rIzzjHcksCFxO
"""

import numpy as np
import math

def metodo_relajacion(A, maxsi, convergencia):
    """
    Ya que tenemos la ecuacion de Laplace en 2D, esta funcion se va a encargar de implementar
    el método de relajación a una Matriz A, hasta que la suma de las diferencias absolutas entre
    el paso anterior y el proximo paso este abajo de la convergencia o el numero de iteraciones
    (maxi) sea alcanzado.

    """
    i = 0
    diff = convergencia + 1    #Suma de diferencias absolutas entre valores de la matriz A

    Nx, Ny = A.shape

    while i < maxsi and diff > convergencia:
        #Aqui se hace el ciclo en todos los puntos que estan adentro del contorno delimitado
        Atemp = A.copy()
        diff = 0.0

        for y in range(1, Ny - 1):
            for x in range(1, Nx - 1):
                A[y, x] = 0.25 * (Atemp[y, x + 1] + Atemp[y, x - 1] + Atemp[y + 1, x] + Atemp[y - 1, x])
                diff += math.fabs(A[y, x] - Atemp[y, x])

        diff /= (Nx * Ny)
        i += 1
        print(f"Iteración #{i}, diff = {diff}")

def condiciones_frontera(A, x, y, v0):
  """
  Establecemos condiciones de frontera de Dirichlet
  """
  a = x[-1]
  b = y[-1]

  # Condición de frontera izquierda y derecha
  A[:, 0] = 0
  A[:, -1] = 0

  # Condición de frontera inferior
  A[0, :] = -v0

  # Condición de frontera superior
  A[-1, :] = v0

  # Asignar las esquinas
  A[0, 0] = A[-1, -1] = 0

# Test del Programa Principal

#En esta linea de codigo, se colocan los parametros inciciales, para empezar a correr el test del programa principal dx=dy=h
input_parameters = {
    "Nx": 100,
    "Ny": 100,
    "h": 1000,
    "v_0": 200
}


x = np.linspace(0, 1, input_parameters["Nx"] + 2)
y = np.linspace(0, 1, input_parameters["Ny"] + 2)
A = np.zeros((input_parameters["Ny"] + 2, input_parameters["Nx"] + 2))

v = input_parameters["v_0"]
condiciones_frontera(A, x, y, v)
metodo_relajacion(A, input_parameters["h"], 0.00001)

#El código crea una cuadrícula de puntos en 2 dimensiones y define una matriz para almacenar coeficientes.
#Luego, establece condiciones en los bordes de la cuadrícula y utiliza un método de relajación para resolver un sistema de ecuaciones representado
#por la matriz

import matplotlib.pyplot as plt

plt.imshow(A, extent=(0, 1, 0, 1), cmap='plasma')
plt.colorbar(label="Potencial")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distribucion de Potencial, Utilizando Condiciones de Frontera de Dirichlet")
plt.show()