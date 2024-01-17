def fibonacci(n):
    if n <= 0:
        return None

    fib = [0, 1]
    while len(fib) < n:
        next_el = fib[-1] + fib[-2]
        fib.append(next_el)

    return fib[n-1]

res = fibonacci(50)
print(res)
