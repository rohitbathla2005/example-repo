# Hours worked = 8, payment = 1500.
# worked < 8, pay less, 200 per hour.
# Hours worked > 8, pay more, 200 per hour

x = int(input("enter working hours"))

if x == 8:
    Total_Money = 1500
    print("Total money=", Total_Money)
elif x >= 1 and x < 8:
    lesshour = 8-x
    Total_Money = 1500 - lesshour*200
    print("Total money=", Total_Money)
elif x > 8 :
    morehour = x-8
    Total_Money = 1500 + morehour*200
    print("Total money=", Total_Money)