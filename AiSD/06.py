def mnoj1(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def replaced(n):
    result = []
    for num in n:
        if num > 1:
            factors = mnoj1(num)
            result.extend(factors)
        else:
            result.append(num)
    return result

n = list(range(1, 21))
result = replaced(n)
print(result)