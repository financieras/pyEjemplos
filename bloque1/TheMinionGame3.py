s = "BANANA"
l = len(s)
#Total = sum([l- i for i in range(l)])
Total=0
for i in range(l):
    Total+=l-i
print("Total=",Total)
#Kscore = sum([l-i if s[i] in 'AEIOU' else 0 for i in range(l)])
Kscore=0
for i in range(l):
    if s[i] in 'AEIOU':
        Kscore+=l-i
print("Kscore=",Kscore)
Sscore = Total - Kscore
print("Sscore=",Sscore)
if Kscore == Sscore:
    print('Draw')
else:
    print('Kevin '+str(Kscore) if Kscore>Sscore else 'Stuart '+str(Sscore))