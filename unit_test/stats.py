import math


def calculate_stats(data):
    """
    Calculate mean, median, and standard deviation for a list of numerical data.

    Parameters:
    ----------
        data (list): List of numerical data.

    Returns:
    -------
        dict: A dictionary containing the calculated mean, median, and standard deviation.

    """

    if not data:
        raise ValueError("Input data cannot be empty.")

    # Calculate Mean
    mean = sum(data)/len(data)

    # Calculate Median
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    # Calculate standard deviation
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    std_deviation = math.sqrt(squared_diff_sum / len(data))

    return {"mean": mean, "median": median, "standard_deviation": std_deviation}
