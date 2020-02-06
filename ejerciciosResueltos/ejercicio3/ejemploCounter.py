import collections
contador = collections.Counter()
for word in ['uno','dos','dos','tres','tres','tres','cuatro','cuatro','cuatro','cuatro']:
	contador[word]+=1

print (contador['tres'])