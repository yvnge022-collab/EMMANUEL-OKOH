
def sum_list(numbers):
    return sum(numbers)


def mean_median_mode(numbers):
    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]

    # Calculate mode
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    highest = max(frequency.values())
    mode = [num for num, count in frequency.items()
            if count == highest]

    if highest == 1:
        mode = "No mode"

    return mean, median, mode


def main():
    numbers = [2, 4, 4, 6, 8]

    print("Sum:", sum_list(numbers))

    mean, median, mode = mean_median_mode(numbers)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)


main()
