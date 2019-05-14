from random import randint


L = [randint(0, 100) for i in range(100)]
sort_L = sorted(L) # using python built-in funtion
L.sort() # using list sort method 

L = ['abse', 'xtw', 'hello', 'keysvalue']
sort_L = sorted(L, key=lambda x : len(x)) # by using lambda sort by length

L = [{'name': 'nathan', 'score': 99}, {'name': 'jane', 'score': 85}]
L.sort(key=lambda x: x['score'], reverse=True) # by using lambda function sort by score

