def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


if __name__ == '__main__':
    print(f'5! = {factorial(5)}')
    print(f'10! = {factorial(10)}')
    print(f'3! = {factorial(3)}')
    print(f'4! = {factorial(4)}')
