import random
def Level(countries,CorrectDir, capitals):
	print('Hi! This is the geographical knolege test.Level 3')
	print('Now you have to ask on our ten question')
	q=0 # question number
	w=0 #wrong answers counter
	r=0 #right answer counter
	while q<10: #loop for 10 questions
		q+=1 #question counter level up
		n=random.randint(0,9)
		question= countries[n]+' has capital of?'
		print('The question ',q,'-',question) #print question
		answer='the capital of ' +countries[n]+' is '+CorrectDir[countries[n]] # right answer
		answ=input('Tape your answer please ') # ask answer
		answ=answ.strip()
		answ=answ.capitalize()
		print('Your answer is - ', answ)
		if answ==CorrectDir[countries[n]]: 
			print('You are right')
			r+=1 #right counter's level up
		else:
			print('you are wrong!')
			w+=1 #wrong answers level up
	print('Now our test is end!')
	return r