numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(num)
    else:
        if num == 1:
            continue
        else:
            not_primes.append(num)

print("Простые числа:", primes)
print("Составные числа:", not_primes)
