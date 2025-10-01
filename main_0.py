#Пользователь вводит с клавиатуры число в диапозоне от 1 до 100. 
# если число кратно 3 (делится на 3 без остатка) 
# нужно вывести на экран слово FIZZ.
# если число кратно 5 то BUZZ. Если число кратно и 3 и 5 то 
# вывести FIZZ BUZZ. Если число не кратно не 3 ни 5 нужно вывести 
# само число. Если пользователь ввел значение не в диапазоне 
# от 1 до 100 требуется вывести сообщение об ошибке.

#number=int(input("Введите число в диапазоне от 1 до 100: "))
#if 1 > number or number>100:
#    print("Ошибка ввода")
#elif number%3==0 and number%5==0:
#    print(str(number)+ " FIZZ BUZZ")
#elif number%3==0:  
#    print(str(number) + " FIZZ")
#elif number%5==0:
#    print(str(number) + " BUZZ")
#else:
#    print(number)

number= int(input())
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0
if 1> number or number >100:
    print("ошибка ввода")
elif is_fizz and is_buzz:
    print("FizzBuzz")
elif is_fizz:
    print("Fizz")
elif is_buzz:
    print("Buzz")
else:
    print(number)