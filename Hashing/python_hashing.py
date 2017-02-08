import hashlib

# word = ACCGTACGTACGATTAGCAT
# hash_object = hashlib.md5()
# hash_object.update(str.encode(word))
# hash_object.update(b'3')
# hex_ob = hash_object.hexdigest()
# small_hash = int(hex_ob[0:7], 16)
# print(small_hash)

# hash_object = hashlib.new('DSA')
# hash_object.update(b'ACCGTACGTACGATTAGCAT')
# hash_object.update(b'2')
# hex_ob = hash_object.hexdigest()
# small_hash = int(hex_ob[0:7], 16)
# print(small_hash)

# print(2**28)

# This defines a set of hashes all based off the integer value provided.
# word should be a 20-length string in the genome
def DSA_hash(word, value):
	hash_object = hashlib.new('DSA')
	hash_object.update(str.encode(word + str(value)))
	hex_ob = hash_object.hexdigest()
	small_hash = int(hex_ob[0:7], 16)
	return small_hash
# DSA_hash returns an integer value in (0, 16**7 = 2**28)

# Using Sympy the smallest prime bigger than 2**41 is 2199023255579
def py_hash(word, value):
	word_hash = hash(word)
	return (((value + 7)*word_hash + 1000*value)%2199023255579)%(2**29)



