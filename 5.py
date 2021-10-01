try:
    X0=float(input('введите координату центра X0:'))
    Y0=float(input('введите координату центра Y0:'))
    X=float(input('введите координату X:'))
    Y=float(input('введите координату Y:'))
    R=float(input('введите радиус R:'))
    if (X-X0) ** 2 + (Y-Y0) ** 2 <= R ** 2:
        print ('попал')
    else:
        print('не попал')
except ValueError:
    print('это не число. введите число')