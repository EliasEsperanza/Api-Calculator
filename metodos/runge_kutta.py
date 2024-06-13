def runge_kutta(f, y0, x0, x_end, h):
    n = int((x_end - x0) / h)
    x = x0
    y = y0

    results = []
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

        results.append((x, y))

    return results
