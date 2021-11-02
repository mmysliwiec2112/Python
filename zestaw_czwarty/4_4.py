def fibonacci(n):
    fib_prev_1 = 1
    fib_prev_2 = 0
    fib = 0
    for x in range(1, n):
        fib = fib_prev_1 + fib_prev_2
        fib_prev_2 = fib_prev_1
        fib_prev_1 = fib

    return fib


if __name__ == '__main__':
    print(f'5th Fibonacci number = {fibonacci(5)}')
    print(f'7th Fibonacci number = {fibonacci(7)}')
    print(f'2nd Fibonacci number = {fibonacci(2)}')
    print(f'9th Fibonacci number = {fibonacci(9)}')
