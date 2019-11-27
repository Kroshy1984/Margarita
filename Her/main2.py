# начало
from dic2 import  *
import random,Ded2,Finalization
print('Я игра-тест по географии')
while True:
	b = input('Введите желаемый уровень для начала игры(1-3 на клавиатуре)')
	if b =='1': 
		r=Ded2.Level(countries,CorrectDir, capitals)
		break
	elif b =='2': 
		r=Ded2.Level(objec,correctsubject, town)
		break
	elif b=='3':
		r=Ded2.Level(country,correct, cityand)
		break
	else: 
		print ('Вам нужно нажать только цифру 1 или 2 или 3 на клавиатуре!')
		continue
print(Finalization.Finalization(r))