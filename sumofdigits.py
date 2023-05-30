sum=0


def sum_of_digits(x):
    if(x == 0):
        return 0
    else :
        sum = x%10 + int(sum_of_digits(x/10))
        return sum
x = int(input("Enter the number"))
y=sum_of_digits(x)
print(y)