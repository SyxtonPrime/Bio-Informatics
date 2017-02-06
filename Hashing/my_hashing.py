import itertools

# We start with a 20-mer (A 20-legnth string in ATCG...)

guide = {'A': '0', 'C': '1', 'T': '2', 'G': '3'}
# k_mer = 'ATCTACGTA'
# val = 'ATCTACGTA'
# for k in k_mer:
# 	val = val.replace(k, guide[k])
# print(val)
# val = int(val, 4)
# print(val)

# Coverts 5 letters to a number between [0, 2^10 - 1]. Value is 0, 1, 2 or 3
# These hashes didnt work because there was too much data loss. Need to take bigger hashes. 
def my_hash(word, value):
	k_mer = word[5*value:5*value + 5]
	val = k_mer
	for k in k_mer:
		val = val.replace(k, guide[k])
	return int(val, 4)

# Coverts the 10 letters to a number between [0, 2^20 - 1]
def my_second_hash(word, value):
	if value != 3:
		k_mer = word[5*value:5*value + 10]
	else:
		k_mer = word[0:5] + word[15: 20]
	val = k_mer
	for k in k_mer:
		val = val.replace(k, guide[k])
	return int(val, 4)

# This is useful later 
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]