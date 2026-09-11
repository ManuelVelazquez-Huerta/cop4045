import math
import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns):
    """
    Evaluate and plot a mathematical function over a given domain.

    fun_str: string containing the function expression
    domain: tuple (xmin, xmax)
    ns: number of sample points
    """

    xmin = domain[0]
    xmax = domain[1]

    xs = []
    ys = []

    # Calculate spacing between sample points.
    step = (xmax - xmin) / (ns - 1)

    # Generate x and y values.
    for i in range(ns):
        x = xmin + i * step

        xs.append(x)

        # Evaluate the function expression using the current x value.
        y = eval(fun_str)

        ys.append(y)

    # Print table header.
    print()
    print("{:>10} {:>10}".format("x", "y"))
    print("----------------------")

    # Print x and y values.
    for i in range(ns):
        print("{:+10.4f} {:+10.4f}".format(xs[i], ys[i]))

    # Plot the function.
    plt.plot(xs, ys, marker=".")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)

    plt.grid()

    plt.show()


def main():
    # Read function expression.
    fun_str = input("Enter function with variable x: ")

    # Read number of samples.
    ns = int(input("Enter number of samples: "))

    # Read domain values.
    xmin = float(input("Enter xmin: "))
    xmax = float(input("Enter xmax: "))

    # Store domain in a tuple.
    domain = (xmin, xmax)

    # Call the plotting function.
    plot_function(fun_str, domain, ns)


if __name__ == "__main__":
    main()