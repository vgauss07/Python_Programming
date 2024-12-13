def division(x, y):
    try:
        x / y
    except ZeroDivisionError as ex:
        print(ex)