print('* '*20)
k=['a','b','c']
v=list(range(1,4))            #[1,2,3]
print(dict(zip(k,v)))         #{'a': 1, 'b': 2, 'c': 3}
print(set(zip(k,v)))          #{('b', 2), ('c', 3), ('a', 1)}
