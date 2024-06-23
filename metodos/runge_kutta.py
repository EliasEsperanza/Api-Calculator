def runge_kutta(f, y0, x0, x_end, h):
    # Calcula el número de pasos
    n = int((x_end - x0) / h)
    # Inicializa las variables de estado
    x = x0
    y = y0

    # Listas para almacenar los resultados y los pasos intermedios
    results = []
    steps = []

    # Bucle principal que implementa el método de Runge-Kutta de cuarto orden
    for i in range(n):
        # Calcula los coeficientes k1, k2, k3 y k4
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        
        # Calcula el nuevo valor de y usando la fórmula de RK4
        y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
        # Registra los detalles del paso actual
        steps.append(f"Paso {i + 1}: x = {x}, y = {y}, k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}, y_new = {y_new}")

        # Actualiza y para el siguiente paso
        y = y_new
        x += h

        # Almacena el resultado actual (x, y)
        results.append((x, y))

    # Prepara los datos para graficar
    plot_x = [x for x, y in results]
    plot_y = [y for x, y in results]

    # Devuelve los resultados, los pasos intermedios, y los datos para graficar
    return results, steps, plot_x, plot_y
