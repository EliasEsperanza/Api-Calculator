def hermite_interpolation(x_values, y_values, derivatives):
    n = len(x_values)
    q = [[0] * (2 * n) for _ in range(2 * n)]
    z = [0] * (2 * n)
    steps = []

    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x_values[i]
        q[2 * i][0] = q[2 * i + 1][0] = y_values[i]
        q[2 * i + 1][1] = derivatives[i]

        if i != 0:
            q[2 * i][1] = (q[2 * i][0] - q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])
        
        steps.append(f"z[{2 * i}] = z[{2 * i + 1}] = {x_values[i]}")
        steps.append(f"q[{2 * i}][0] = q[{2 * i + 1}][0] = {y_values[i]}")
        steps.append(f"q[{2 * i + 1}][1] = {derivatives[i]}")
        if i != 0:
            steps.append(f"q[{2 * i}][1] = (q[{2 * i}][0] - q[{2 * i - 1}][0]) / (z[{2 * i}] - z[{2 * i - 1}]) = {q[2 * i][1]}")

    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            q[i][j] = (q[i][j - 1] - q[i - 1][j - 1]) / (z[i] - z[i - j])
            steps.append(f"q[{i}][{j}] = (q[{i}][{j - 1}] - q[{i - 1}][{j - 1}]) / (z[{i}] - z[{i - j}]) = {q[i][j]}")

    return z, q, steps


