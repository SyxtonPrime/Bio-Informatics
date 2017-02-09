import my_hashing
import python_hashing
import random
import itertools
import numpy as np

f = open('genome.txt', 'r')
genome = f.read()
guide = {'A': '0', 'C': '1', 'T': '2', 'G': '3', '0': 'A', '1': 'C', '2': 'T', '3': 'G'}
klen = 20
size = len(genome)
cap = size - klen
N = 10000000
w = 2**20
error = 2*N/w
print(error)
prefixes = []
x = itertools.product('ACTG', repeat = 10)
for i in x:
	prefixes.append(''.join(i))
print('Hi')
# These bins are for my hasing
my_hash_bin = np.zeros((4, w))
# These bins are for the Python Hash function DSA
py_hash_bin = np.zeros((4, 2**28))

for _ in range(0, N):
	choice = random.randrange(0, cap + 1)
	kmer = genome[choice : choice + klen]
	for i in range(4):
		my_hash_bin[i][my_hashing.my_second_hash(kmer, i)] += 1
		py_hash_bin[i][python_hashing.DSA_hash(kmer, i)] += 1

print('Hi')

# This naturally produces alot of intersections
# so we set all boxes with frequency less than 2N/w to 0.

my_hash_bin[my_hash_bin < error] = 0

# Now we want to recombine our 4 bins to get frequency estimates for each 20-mer
# bin1 gives the frequency of the first 0-10
# bin2 gives the frequency of the first 5-15
# bin3 gives the frequency of the first 10-20
# bin4 gives the frequency of the first 0-5 and 15-20

bin3_reduced = [(prefixes[x], my_hash_bin[2][x]) for x in range(0, w) if my_hash_bin[2][x] != 0]

print(len(bin3_reduced))

g = open('data4.txt', 'w')

# k_mer_frequency = []
for k in range(0, w):
	if k%100000 == 0:
		print(k)
	if my_hash_bin[0][k] != 0:
		for l in bin3_reduced:
			k_mer = prefixes[k] + l[0]
			frequency = min(my_hash_bin[0][k],
				my_hash_bin[1][my_hashing.my_second_hash(k_mer, 1)], l[1],
				my_hash_bin[3][my_hashing.my_second_hash(k_mer, 3)])
			if frequency != 0:
				second_estimate = min(py_hash_bin[i][python_hashing.DSA_hash(k_mer, i)] for i in range(4))
				# k_mer_frequency.append((k_mer, frequency))
				g.write('k_mer: ' + k_mer + ', ' )
				g.write('Frequency: ' + str(frequency) + ', ')
				g.write('Second Estimate: ' + str(second_estimate) + '\n')
# print(k_mer_frequency)

