from scipy.interpolate import CubicSpline

def cubic_spline_interpolation(x_vals, y_vals, x):
    # Basic validations
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) < 3:
        raise ValueError("At least three data points are recommended for cubic spline interpolation")
    if sorted(x_vals) != x_vals:
        raise ValueError("x values must be sorted in increasing order")
    if x < x_vals[0] or x > x_vals[-1]:
        raise ValueError("The point is outside the range of the table")

    # Create the spline object and evaluate
    cs = CubicSpline(x_vals, y_vals)
    return cs(x)


def main():
    # Table values
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [1, 4, 9, 16, 25]

    # The x we want to estimate
    x = 2.5

    try:
        result = cubic_spline_interpolation(x_vals, y_vals, x)
        print(f"Cubic spline interpolation at x = {x}: {result}")
    except ValueError as e:
        print("Interpolation error:", e)


if __name__ == "__main__":
    main()
