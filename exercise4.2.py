number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
number3 = int(input("შეიყვანეთ მესამე რიცხვი: "))

if number1 >= number2 and number1 >= number3:
    print("ყველაზე დიდი რიცხვია:", number1)
elif number2 >= number1 and number2 >= number3:
    print("ყველაზე დიდი რიცხვია:", number2)
else:
    print("ყველაზე დიდი რიცხვია:", number3)