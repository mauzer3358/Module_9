def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        Is_prime = True
        for i in range(2, res):
            if res % i == 0:
                Is_prime = False
        if Is_prime:
            print('Простое')
        elif Is_prime == False:
            print('Составное')
        return res
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)