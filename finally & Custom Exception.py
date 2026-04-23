try:
    a = int(input())
    if a < 0:
        raise Exception("Negative not allowed")
except Exception as e:
    print(e)
finally:
    print("Done")