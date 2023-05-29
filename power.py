
def power_no(x, y):
    if y == 1:
        return x
    else:
        return power_no(x, y-1)*x


if __name__ == '__main__':
    x = int(input("enter  the base value"))
    y = int(input("enter  the power value"))
    result = power_no(x, y)
    print("The power of", x, "to ", y,"is ", result)
