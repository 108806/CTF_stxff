import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{00:8b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print('ENCRYPTED:', enc)




# S O L U T I O N :


_FLAG_ = 'mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj'
# pico = 'hagjgdgp'


def b16_decode(enc):
	dec = ''
	for c in [enc[x:x+2] for x in range(0, len(enc), 2)]:
		c1 = "{00:04b}".format(ALPHABET.index(c[0]))
		c2 = "{00:04b}".format(ALPHABET.index(c[1]))
		#print(c1+c2)
		unbin = int(c1 + c2, 2)
		dec += chr(unbin)
	return dec 


def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]


def crack(FLAG, K):
	dec = ''
	for x, y in enumerate(FLAG, start=0):
		dec += unshift(y, K[x % len(K)])
	#print('UNSHIFTED:', dec)
	#print('UNBASED16:', b16_decode(dec))
	return dec


for k in ALPHABET:
	keystart = ''
	decrypted = crack(_FLAG_, k)
	if all([c in ALPHABET for c in decrypted]):
		dec0ded = b16_decode(decrypted)
		if all([c in string.printable for c in dec0ded]):
			print(f'[*] DECRYPTED with {k}:', dec0ded)
