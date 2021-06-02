from pwn import *

def UNHEXLIFY(A:str):
	return [ int(x, 16) for x in [A[i:i+2] for
		i in range(0, len(A), 2)] ]

R = remote('mercury.picoctf.net', 36449)
print(R.recvlineS())
print(R.recvlineS().strip())
enc_flag = R.recvlineS().strip()
flag_b10 = UNHEXLIFY(enc_flag)
print(enc_flag)

OFFSET = 50000 - 32

t = R.recvuntil('?')
R.sendline('A'*OFFSET)
R.recvuntil('?')
R.sendline('A'*32)
R.recvline()
resp = R.recvlineS().strip()
print(resp)

resp_b10 = UNHEXLIFY(resp)
print(resp_b10)

msg = 'A'*32

K = []

for i in range(len(resp_b10)):
	K.append((ord('A') ^ resp_b10[i]))
print('[*] Decrypted K:', K)

secret = ''.join([ chr(x ^ y) for x,y in zip(K, flag_b10)])
info(secret)

R.close()
