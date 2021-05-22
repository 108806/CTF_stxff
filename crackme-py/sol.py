#! /usr/bin/env python3

secret = 'A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN'
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
print(len(alphabet))

word = lambda s : ''.join([ 
alphabet[alphabet.index(x)+47] if alphabet.index(x)+47 <= 94 else 
	alphabet[alphabet.index(x)+47-94] for x in secret
])

print(word(secret))
