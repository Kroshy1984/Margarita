def Level1():
	import random
	capitals=['Aphina','Roma','Moscow','Bejing','Tokio','Tel-Aviv','Washington','Rabbat','Monako','Paris']
	countries=['Greece','Italy','Russia','China','Japan','Israel','USA','Morokko','Monako','France']
	CorrectDir={'Greece':'Aphina','Italy':'Roma','Russia':'Moscow','China':'Bejing','Japan':'Tokio','Israel':'Tel-Aviv','USA':'Washington','Morokko':'Rabbat','Monako':'Monako','France':'Paris'}
	print('Hi! This is the geographical knolege test')
	print('Now you have to ask on our ten question')
	q=0
	w=0
	r=0
	while q<10:
		q+=1
		n=random.randint(0,9)
		question= countries[n]+' has capital of?'
		print('The question #',q,'-',question)
		answer='the capital of ' +countries[n]+' is '+CorrectDir[countries[n]]
		nint2=random.randint(1,4)
		key={}
		key[nint2]=CorrectDir[countries[n]]
		k=0
		while k<4:
			k+=1
			if k!=nint2:
				while True:
					nint=random.randint(0,9)	
					if CorrectDir[countries[nint]] not in key.values():
						key[k]=CorrectDir[countries[nint]]
						break		
		k=1
		while k<=4:
			print(k,'-',key[k])
			k+=1
		answ=input('Select your answer please ')
		a=key[int(answ)]
		print('Your answer is - ', a)
		if a==CorrectDir[countries[n]]: 
			print('You are right')
			r+=1
		else:
			print('your are wrong!')
			w+=1
	print('Now our test is end!')
	if r>7: print('You are very good specialized! You were right at', r ,'times!')
	elif r>=5 and r<=7:print('You are not bed specialized! You were right at ', r ,'times! but in ', w,' times you were wrong!')
	elif  r<5 and r!=0:print('you are bed specialized! You were right at', r ,'times! but in ', w,' times you were wrong!')
	elif r==0:print('you are very bed specialized! You were always wrong!')
    return None