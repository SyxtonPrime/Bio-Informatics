import random
import numpy as np

def genome(x):

	# This function generates a genome (Organism) for length x.
	# Essentially writes a file consisting of a word of length x over the alphabet {A, T, C, G}

	f = open('genome.txt', 'w')

	for _ in range(x):
		f.write(random.choice('ATCG'))

def markov_genome(x):

	# This function generates a genome (Organism) for length x.
	# Essentially writes a file consisting of a word of length x over the alphabet {A, T, C, G}
	# The difference from the last function is that the previous letter influences the following.

	f = open('markov_genome.txt', 'w')

	array = np.array(['A', 'T', 'C', 'G'])

	letter = random.choice('ATCG')
	f.write(letter)

	for _ in range(x - 1):
		if letter == 'A':
			letter = np.random.choice(array, p=[0.4, 0.3, 0.2, 0.1])
			f.write(letter)
		if letter == 'T':
			letter = np.random.choice(array, p=[0.1, 0.4, 0.3, 0.2])
			f.write(letter)
		if letter == 'C':
			letter = np.random.choice(array, p=[0.2, 0.1, 0.4, 0.3])
			f.write(letter)
		if letter == 'G':
			letter = np.random.choice(array, p=[0.3, 0.2, 0.1, 0.4])
			f.write(letter)

markov_genome(100000)