from pwn import *


def worker():
	recvng = b''
	while b'ctf' not in recvng:
		try:
			host = remote('misc.bcactf.com', 49156)
			recvng = host.recvuntil(b'Enter the letter')
			letter = chr(host.recvline().strip().split()[0][1])
		except Exception:
			continue
		info(letter)
		host.sendline(letter)
		
		host.recvuntil(b'Spinning...')
		chall = host.recvuntil(']]]\r').strip()
		TRIES, HITS = 0, 0
		while b'[[[' in chall:
			TRIES += 1
			print(f'Tries : {TRIES}\t\tHITS : {HITS}\t\t{chall}\t{letter}', flush=False, end='\r')
			try:
				chall = host.recvuntil(b']]]').strip()
			except EOFError as e:
				break
		recvng = host.recvall()
		info(recvng)

worker()
