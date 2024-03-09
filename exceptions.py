try:
    x=int(input("What's X?"))
except ValueError:
    print("X should be an integer!!")
print(f"x is {x}")