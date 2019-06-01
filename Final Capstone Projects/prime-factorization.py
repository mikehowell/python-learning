prime_number_list = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    97,
]

number_to_factorize = int(input("Please enter a number to get its prime factors: "))

prime_factors = list()

for num in prime_number_list:
    while number_to_factorize % num == 0:
        prime_factors.append(num)
        number_to_factorize = number_to_factorize / num
        if number_to_factorize == num:
            prime_factors.append(num)
            break

print(prime_factors)
