def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result < 2:
            print("Составное")
        else:
            for n in range(2, result - 1):
                if result % n == 0:
                    print("Составное")
                    break
            print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)
