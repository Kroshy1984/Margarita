import random
def Level (countries,CorrectDir, capitals):
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
        while True:
            try:
                answ=input('Select your answer please ')
                a=key[int(answ)]
            except ValueError as err:
                print (chr(9940),"Your answer is not int (1-4). Please load number of answer correctly!",chr(9757))
                continue
            except KeyError as err:
                print (chr(9940),"Your should  tape only 1 or 2 or 3 or 4 buttons on your keyboard. Please load number of your question correctly!",chr(9757))
                continue
            else: break
        print('Your answer is - ', a)
        if a==CorrectDir[countries[n]]:
            print('You are right')
            r+=1
        else:
            print('your are wrong!')
            w+=1
    print('Now our test is end!')
    return r