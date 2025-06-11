def cubic_spline_interpolation(x_data, y_data, x_interp):
    """
    Perform manual cubic spline interpolation.

    Parameters:
    x_data (list of float): x values of the known data points (must be sorted).
    y_data (list of float): y values of the known data points.
    x_interp (float): the x value where interpolation is desired.

    Returns:
    float: interpolated y value or error message.
    """
    try:
        # Input validations
        if len(x_data) != len(y_data):
            raise ValueError("x and y lists must be the same length.")
        if len(x_data) < 3:
            raise ValueError("At least three data points are required.")
        if sorted(x_data) != x_data:
            raise ValueError("x values must be sorted in ascending order.")
        if not isinstance(x_interp, (int, float)):
            raise ValueError("x_interp must be a numeric value.")
        if x_interp < x_data[0] or x_interp > x_data[-1]:
            raise ValueError("x_interp is outside the interpolation range.")

        # Step 1: Compute h and alpha
        n = len(x_data)
        h = [x_data[i+1] - x_data[i] for i in range(n - 1)]
        alpha = [
            (3 / h[i]) * (y_data[i + 1] - y_data[i]) -
            (3 / h[i - 1]) * (y_data[i] - y_data[i - 1])
            for i in range(1, n - 1)
        ]

        # Step 2: Solve tridiagonal system for c
        l = [1] + [0] * (n - 1)
        mu = [0] * n
        z = [0] * n

        for i in range(1, n - 1):
            l[i] = 2 * (x_data[i + 1] - x_data[i - 1]) - h[i - 1] * mu[i - 1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]

        l[-1] = 1
        z[-1] = 0

        c = [0] * n
        b = [0] * (n - 1)
        d = [0] * (n - 1)
        a = y_data[:-1]

        for j in range(n - 2, -1, -1):
            c[j] = z[j] - mu[j] * c[j + 1]
            b[j] = ((y_data[j + 1] - y_data[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j]) / 3)
            
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        # Step 3: Find the interval and interpolate
        for i in range(n - 1):
            if x_data[i] <= x_interp <= x_data[i + 1]:
                dx = x_interp - x_data[i]
                return a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

    except Exception as e:
        return f"Error: {e}"


def main():
    # Sample data
    x_vals = [1.6, 2, 3, 4, 5]
    y_vals = [1, 4, -0.9, 16, 55]

    x_to_interpolate = 2.5

    result = cubic_spline_interpolation(x_vals, y_vals, x_to_interpolate)

    print("Interpolated result:", result)


if __name__ == "__main__":
    main()
