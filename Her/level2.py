import random
def Level(objec,correctsubject, town):	
	print('Это тест на знание субъектов Российской Федерации')
	print('Ответьте на наши вопросы и в конце вы узнаете на сколько хорошо вы знаете субъекты Российской Федерации .')
	q=0
	w=0
	r=0
	while q<10:
		q+=1
		n=random.randint(0,80)
		question= 'Какой административный центр имеет '+objec[n]+'?'
		print('Вопрос #',q,'-',question)
		answer='административный центр' +objec[n]+' это '+correctsubject[objec[n]]
		nint2=random.randint(1,4)
		key={}
		key[nint2]=correctsubject[objec[n]]
		k=0
		while k<4:
			k+=1
			if k!=nint2:
				while True:
					nint=random.randint(0,80)	
					if correctsubject[objec[nint]] not in key.values():
						key[k]=correctsubject[objec[nint]]
						break		
		k=1
		while k<=4:
            print(k,'-',key[k])
			k+=1
		while True:
			try:
				answ=input('Выберите правильный ответ')
				a=key[int(answ)]
			except ValueError as err:
				print (chr(9940),"Ваш ответ не (1-4). Пожалуйста! Вводите правильные символы!",chr(9757))
				continue
			except KeyError as err:
				print (chr(9940),"Вам нужно нажать только цифру 1 или 2 или 3 или 4 на клавиатуре!. Пожалуйста! Вводите правильные символы!",chr(9757))
				continue
			else: break	
			answ=input('Выберите правильный ответ')
			a=key[int(answ)]
			print('Ваш ответ -', a)
			if a==correctsubject[objec[n]]:
                print('Вы правы')
				r+=1
			else:
				print('Вы ошиблись!')
				w+=1
	print('Наш тест подошёл к концу!')
	if r==10: print('Вы прекрасно разбираетесь в субъектах Российской Федерации. Все ответы верны!')
	elif r>=7 and r<=10:print('Вы не плохо разбираетесь в субъектах Российской Федерации', r ,'раз вы ответили правильно! но в ', w,'случаях(е) вы ошиблись!')
	elif r<6 and r!=0:print('Вы плохо разбираетесь в субъектах Российской Федерации. Всего', r ,'раз(а) вы ответили правильно! а в', w,'случаях вы ошиблись!')
	elif r==0:print('Вы ужасно разбиаетесь в субъектах Российской Федерации. Вы ошиблись везде!')