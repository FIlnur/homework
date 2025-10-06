#пользователь вводит число, если число больше 0 нужно вывести надпись "Number is positive"

number=int(input("Введите число: "))
if number == 7:
    print("Goodbye!")
elif number == 0:
    print("Number is equal to zero")
elif number < 0:
    print("Number is negative")
else:
    print("Number is positive")