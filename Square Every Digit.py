d = 9119

def square_digits(num):
    if num == 0:
        return 0

    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10

    digits.reverse()
    print(digits)
    digits =[x**2 for x in digits]
    print(digits)
    return int(''.join(map(str, digits)))

print(square_digits(d))
print(d)