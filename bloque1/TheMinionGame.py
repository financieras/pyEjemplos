#The Minion Game
word='BANANA'
vowels='AEIOU'
stuart=[];kevin=[]
for i in range(len(word)): #if i=0 the character is word[0], if i=1 the character is word[1]
    for j in range(i+1,len(word)+1): #j+1 indica el nº de caracteres que tomamos
        myslice=word[i:j]
        if myslice[0] in vowels:
            kevin.append(myslice)
        else:
            stuart.append(myslice)
print('Stuart ',len(stuart),'   Kevin ',len(kevin))