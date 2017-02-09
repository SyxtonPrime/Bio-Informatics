from my_hashing import my_second_hash
from python_hashing import py_hash
import random
import itertools
import numpy as np
from time import process_time

t1 = process_time()

f = open('markov_genome.txt', 'r')
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
t2 = process_time()

print(t2 - t1)

# These bins are for my hashing

my_hash_bin = np.zeros((4, w))

# These bins are for the Python Hash function DSA

py_hash_bin = np.zeros((4, 2**29))

t3 = process_time()
print(t3 - t2)

for _ in range(0, N):
	choice = random.randrange(0, cap + 1)
	kmer = genome[choice : choice + klen]
	for i in range(4):
		my_hash_bin[i][my_second_hash(kmer, i)] += 1
		py_hash_bin[i][py_hash(kmer, i)] += 1

t4 = process_time()
print(t4 - t3)

# This naturally produces alot of intersections
# so we set all boxes with frequency less than 2N/w to 0.

my_hash_bin[my_hash_bin < error] = 0

# Now we want to recombine our 4 bins to get frequency estimates for each 20-mer
# bin1 gives the frequency of the first 0-10
# bin2 gives the frequency of the first 5-15
# bin3 gives the frequency of the first 10-20
# bin4 gives the frequency of the first 0-5 and 15-20

bin1_reduced = [(prefixes[x], my_hash_bin[0][x]) for x in range(0, w) if my_hash_bin[0][x] != 0]
bin3_reduced = [(prefixes[x], my_hash_bin[2][x]) for x in range(0, w) if my_hash_bin[2][x] != 0]

print(len(bin1_reduced), len(bin3_reduced))

t5 = process_time()
print(t5 - t4)

g = open('data8.txt', 'w')

# k_mer_frequency = []
for k in bin1_reduced:
	for l in bin3_reduced:
		k_mer = k[0] + l[0]
		frequency = min(k[1],
			my_hash_bin[1][my_second_hash(k_mer, 1)], l[1],
			my_hash_bin[3][my_second_hash(k_mer, 3)])
		if frequency != 0:
			second_estimate = min(py_hash_bin[i][py_hash(k_mer, i)] for i in range(4))
			if second_estimate != 0:	
				# k_mer_frequency.append((k_mer, frequency))
				g.write('k_mer: ' + k_mer + ', ' )
				g.write('Frequency: ' + str(frequency) + ', ')
				g.write('Second Estimate: ' + str(second_estimate) + '\n')

# print(k_mer_frequency)
t6 = process_time()
print(t6 - t5)

