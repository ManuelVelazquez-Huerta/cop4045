import math
import matplotlib.pyplot as plt


while True:
    a_input = input("Enter a: ")

    # Blank input ends the program.
    if a_input == "":
        break

    a = float(a_input)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print("no real solutions")

        # Center graph around vertex.
        xopt = -b / (2 * a)
        xmin = xopt - 5
        xmax = xopt + 5

    elif discriminant == 0:
        x1 = -b / (2 * a)
        print("one solution: {:.5f}".format(x1))

        xmin = x1 - 5
        xmax = x1 + 5

    else:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)

        print("two solutions: x1={:.5f} x2={:.5f}".format(x1, x2))

        # Make sure both roots appear on the graph.
        xmin = min(x1, x2) - 2
        xmax = max(x1, x2) + 2

    # Generate 150 evenly spaced points.
    number_points = 150
    step = (xmax - xmin) / (number_points - 1)

    xs = []
    ys = []

    for i in range(number_points):
        x = xmin + i * step
        y = a * x ** 2 + b * x + c

        xs.append(x)
        ys.append(y)

    plt.plot(xs, ys)
    plt.axhline(0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Quadratic Function")
    plt.show()