def runge_kutta(f, y0, x0, x_end, h):
    n = int((x_end - x0) / h)
    x = x0
    y = y0

    results = []
    steps = []

    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        
        y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        steps.append(f"Step {i + 1}: x = {x}, y = {y}, k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}, y_new = {y_new}")

        y = y_new
        x += h

        results.append((x, y))

    return results, steps

