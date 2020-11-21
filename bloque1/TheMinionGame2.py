def minion_game(string):
    vowels='AEIOU'
    stuart=[];kevin=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            myslice=string[i:j]
            if myslice[0] in vowels:
                kevin.append(myslice)
            else:
                stuart.append(myslice)
    if len(kevin)>len(stuart):
        return "Kevin "+str(len(kevin))
    elif len(stuart)>len(kevin):
        return "Stuart "+str(len(stuart))
    else:
        return "Draw"
print(minion_game('BANANA'))