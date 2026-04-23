try:
    a = int(input())
    print(10/a)
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print("Invalid input")