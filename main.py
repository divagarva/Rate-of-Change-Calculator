def calculate_rate_of_change(x1, y1, x2, y2):
    """
    Calculate the rate of change (slope) between two points (x1, y1) and (x2, y2).

    :param x1: x-coordinate of the first point
    :param y1: y-coordinate of the first point
    :param x2: x-coordinate of the second point
    :param y2: y-coordinate of the second point
    :return: Rate of change or slope between the two points
    """
    try:
        # Calculate the rate of change
        rate_of_change = (y2 - y1) / (x2 - x1)
        return rate_of_change
    except ZeroDivisionError:
        return "Error: Division by zero. The x-values of the two points cannot be the same."


def main():
    print("Rate of Change Calculator")
    try:
        # Get input from the user
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))

        # Calculate the rate of change
        rate = calculate_rate_of_change(x1, y1, x2, y2)

        # Display the result
        print(f"The rate of change between points ({x1}, {y1}) and ({x2}, {y2}) is: {rate}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")


if __name__ == "__main__":
    main()
