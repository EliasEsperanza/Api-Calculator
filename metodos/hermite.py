import numpy as np

def hermite_interpolation(x_values, y_values, derivatives):
    n = len(x_values)  # Número de puntos de interpolación
    q = [[0] * (2 * n) for _ in range(2 * n)]  # Matriz para almacenar las diferencias divididas
    z = [0] * (2 * n)  # Lista para almacenar los puntos de interpolación repetidos
    steps = []  # Lista para almacenar los pasos

    # Construcción de las tablas de diferencias divididas
    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x_values[i]  # Asigna los puntos de interpolación repetidos
        q[2 * i][0] = q[2 * i + 1][0] = y_values[i]  # Asigna los valores de y a la primera columna de q
        q[2 * i + 1][1] = derivatives[i]  # Asigna las derivadas de primer orden a la segunda columna de q

        if i != 0:
            q[2 * i][1] = (q[2 * i][0] - q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])  # Calcula las diferencias divididas de primer orden
        
        # Registro de pasos
        steps.append(f"z[{2 * i}] = z[{2 * i + 1}] = {x_values[i]}")
        steps.append(f"q[{2 * i}][0] = q[{2 * i + 1}][0] = {y_values[i]}")
        steps.append(f"q[{2 * i + 1}][1] = {derivatives[i]}")
        if i != 0:
            steps.append(f"q[{2 * i}][1] = (q[{2 * i}][0] - q[{2 * i - 1}][0]) / (z[{2 * i}] - z[{2 * i - 1}]) = {q[2 * i][1]}")

    # Construcción de las diferencias divididas de orden superior
    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            q[i][j] = (q[i][j - 1] - q[i - 1][j - 1]) / (z[i] - z[i - j])  # Calcula las diferencias divididas de orden superior
            steps.append(f"q[{i}][{j}] = (q[{i}][{j - 1}] - q[{i - 1}][{j - 1}]) / (z[{i}] - z[{i - j}]) = {q[i][j]}")  # Registro de pasos

    # Datos para graficar
    plot_x = np.linspace(min(x_values), max(x_values), 100).tolist()  # Valores de x para la gráfica
    plot_y = [evaluate_hermite(z, q, xi) for xi in plot_x]  # Valores de y correspondientes para la gráfica

    return z, q, steps, plot_x, plot_y  # Retorna los puntos de interpolación, las diferencias divididas, los pasos intermedios, y los datos para graficar

def evaluate_hermite(z, q, xi):
    n = len(z) // 2  # Calcula la mitad del tamaño de z, asumiendo que representa los puntos de interpolación
    result = q[0][0]  # Inicializa el resultado con q[0][0], que es el primer término de la interpolación
    product = 1  # Inicializa el producto en 1, se usa para acumular los términos del polinomio

    # Calcula el polinomio de Hermite evaluado en xi
    for i in range(1, 2 * n):
        product *= (xi - z[i - 1])  # Actualiza el producto con (xi - z[i - 1])
        result += q[i][i] * product  # Actualiza el resultado sumando q[i][i] multiplicado por el producto

    return result  # Retorna el resultado de evaluar el polinomio de Hermite en xi




