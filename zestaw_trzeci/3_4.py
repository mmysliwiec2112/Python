def calculations():
    while True:
        print(f'Wpisz liczbę, której trzecią potęgę chcesz obliczyć \n(Wpisz stop aby zatrzymać program)')
        x = input()
        # print(f'typ x: {type(x)}')
        if str(x) == 'stop':
            break
        try:
            if float(x):
                print(f'liczba: {x}, trzecia potega liczby: {float(x) ** 3}')
        except ValueError:
            print("error")


if __name__ == '__main__':
    calculations()
