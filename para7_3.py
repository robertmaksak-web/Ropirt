def raise_to_the_degrees(number, max_degree):
    i = 0
    for j in range(max_degree):
        yield number ** i
        i += 1



res = raise_to_the_degrees(1234, 200)
print(res)
for el in res:
    print(el)
    print()
print("new")
for el in res:
    print(res)
