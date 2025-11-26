def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]

r1 = sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])

print('1st solution', r1)

def sum_two_smallest_numbers2(numbers):
    min_1 = min(numbers)
    numbers.remove(min_1)
    min2 = min(numbers)

    return min_1 + min2

r2 = sum_two_smallest_numbers2([10, 343445353, 3453445, 3453545353453])

print('2nd solution', r2)