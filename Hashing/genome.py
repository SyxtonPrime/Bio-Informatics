import random
# This simple generates a genome (Organism).

f = open('genome_short.txt', 'w')

for _ in range(0, 10**4):
	f.write(random.choice('ATCG'))