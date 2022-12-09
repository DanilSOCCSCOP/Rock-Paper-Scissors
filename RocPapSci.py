# Rock-Scissors-Paper / Камень-Ножницы-Бумага

from random import *

rock = 1
paper = 2
scissors = 3

# User and computer select a number / Пользователь и компьютер выбирают число
user = int(input("\nSelect the number/Выберите число:\n1) Rock/Камень\n2) Paper/Бумага\n3) Scissors/Ножницы\n\n>>> "))
computer = randint(1, 3)

# The user has selected a rock / Пользователь выбрал камень
if user == rock and computer == rock:
	print("\nDraw!/Ничья!\nComputer has selected a rock/Компьютер выбрал камень")
elif user == rock and computer == paper:
	print("\nYou lose!/Вы проиграли\nComputer has selected a paper/Компьютер выбрал бумагу")
elif user == rock and computer == scissors:
	print("\nYou won!/Вы выиграли!\nComputer has selected a scissors/Компьютер выбрал Ножницы")

# The user has selected a paper / Пользователь выбрал бумагу
if user == paper and computer == rock:
	print("\nYou won!/Вы выиграли!\nComputer has selected a rock/Компьютер выбрал камень")
elif user == paper and computer == paper:
	print("\nDraw!/Ничья!\nComputer has selected a paper/Компьютер выбрал бумагу")
elif user == paper and computer == scissors:
	print("\nYou lose!/Вы проиграли\nComputer has selected a scissors/Компьютер выбрал ножницы")

# The user has selected a scissors / Пользователь выбрал ножницы
if user == scissors and computer == rock:
	print("\nYou lose!/Вы проиграли\nComputer has selected a rock/Компьютер выбрал камень")
elif user == scissors and computer == paper:
	print("\nYou won!/Вы выиграли!\nComputer has selected a paper/Компьютер выбрал бумагу")
elif user == scissors and computer == scissors:
	print("\nDraw!/Ничья!\nComputer has selected a scissors/Компьютер выбрал ножницы")

# If the user selects something other than 1, 2 or 3 / Если пользователь выберет не 1, 2 или 3
if user < 1 or user > 3:
	print("\nYou have chosen an answer that does not exist!/Вы выбрали вариант ответа которого нету!\n")