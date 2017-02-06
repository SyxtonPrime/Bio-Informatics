import my_hashing
import python_hashing
import random
import itertools

f = open('genome.txt', 'r')
genome = f.read()
guides = {'A': '0', 'C': '1', 'T': '2', 'G': '3', '0': 'A', '1': 'C', '2': 'T', '3': 'G'}
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
bin1 = [0]*w
bin2 = [0]*w
bin3 = [0]*w
bin4 = [0]*w
# These bins are for the Python Hash function DSA
dbin1 = [0]*(2**28)
dbin2 = [0]*(2**28)
dbin3 = [0]*(2**28)
dbin4 = [0]*(2**28)
for _ in range(0, N):
	choice = random.randrange(0, cap + 1)
	kmer = genome[choice : choice + klen]
	bin1[my_hashing.my_second_hash(kmer, 0)] += 1
	bin2[my_hashing.my_second_hash(kmer, 1)] += 1
	bin3[my_hashing.my_second_hash(kmer, 2)] += 1
	bin4[my_hashing.my_second_hash(kmer, 3)] += 1
	dbin1[python_hashing.DSA_hash(kmer, 0)] += 1
	dbin2[python_hashing.DSA_hash(kmer, 1)] += 1
	dbin3[python_hashing.DSA_hash(kmer, 2)] += 1
	dbin4[python_hashing.DSA_hash(kmer, 3)] += 1

print('Hi')
# This naturally produces alot of intersections
# so we set all boxes with frequency less than 2N/w to 0.
for j in range(0, w):
	if bin1[j] < error:
		bin1[j] = 0
	if bin2[j] < error:
		bin2[j] = 0
	if bin3[j] < error:
		bin3[j] = 0
	if bin4[j] < error:
		bin4[j] = 0
# print(bin1)
# print(sum(bin1), sum(bin2), sum(bin3), sum(bin4))
# print(sum(x > 0 for x in bin1), sum(x > 0 for x in bin2), sum(x > 0 for x in bin3), sum(x > 0 for x in bin4))

# Now we want to recombine our 4 bins to get frequency estimates for each 20-mer
# bin1 gives the frequency of the first 0-10
# bin2 gives the frequency of the first 5-15
# bin3 gives the frequency of the first 10-20
# bin4 gives the frequency of the first 0-5 and 15-20

bin3_reduced = [(prefixes[x], bin3[x]) for x in range(0, w) if bin3[x] != 0]
print(len(bin3_reduced))

g = open('data.txt', 'w')

# k_mer_frequency = []
for k in range(0, w):
	if k%100000 == 0:
		print(k)
	if bin1[k] != 0:
		for l in bin3_reduced:
			k_mer = prefixes[k] + l[0]
			frequency = min(bin1[k],
				bin2[my_hashing.my_second_hash(k_mer, 1)], l[1],
				bin4[my_hashing.my_second_hash(k_mer, 3)])
			if frequency != 0:
				second_estimate = min(dbin1[python_hashing.DSA_hash(kmer, 0)],
				dbin2[python_hashing.DSA_hash(kmer, 1)], dbin3[python_hashing.DSA_hash(kmer, 2)],
				dbin4[python_hashing.DSA_hash(kmer, 3)])
				# k_mer_frequency.append((k_mer, frequency))
				g.write('k_mer: ' + k_mer + ', ' )
				g.write('Frequency: ' + str(frequency) + ', ')
				g.write('Second Estimate: ' + str(second_estimate) + '\n')
# print(k_mer_frequency)

