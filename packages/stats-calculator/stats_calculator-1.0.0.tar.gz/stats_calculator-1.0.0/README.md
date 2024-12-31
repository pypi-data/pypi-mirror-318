# Stats Calculator

A simple Python package for calculating the mean and standard deviation of a set of numbers.

## Installation

```sh
pip install stats_calculator

from stats_calculator import calculate_mean, calculate_std_dev

numbers = [1, 2, 3, 4, 5]

# Calculate the mean
mean_result = calculate_mean(numbers)
print(mean_result)  # Output: 3

# Calculate the standard deviation
std_dev_result = calculate_std_dev(numbers)
print(std_dev_result)  # Output: approximately 1.41421 (depending on precision)
