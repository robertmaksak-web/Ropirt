try:
    try:
        print("start code")
        print(error_test)
        print("no error")
    except SyntaxError:
        print("We have an error!")
except NameError as error:
    print(error)

print("Code after capsule")