word='BANANA'
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        print('word[',i,':',j,'] = ',word[i:j])