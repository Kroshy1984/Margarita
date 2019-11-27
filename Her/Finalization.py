def Finalization(r):
    w=10-r
    if r>7: p='You are very good specialized! You were right at', r ,'times!'
    elif r>=5 and r<=7:p='You are not bed specialized! You were right at ', r ,'times! but in ', w,' times you were wrong!'
    elif  r<5 and r!=0:p='you are bed specialized! You were right at', r ,'times! but in ', w,' times you were wrong!'
    elif r==0:p='you are very bed specialized! You were always wrong!'
    return p