try:
    print("start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError):
    print("We have an  error!")
except ZeroDivisionError:
    print("We have an ZeroDivision error")

print("Code after capsule")