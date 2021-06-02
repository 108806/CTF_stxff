flag_start	= 'pico' # Used to check if im on the right tracks
Ax5K 	= '3979711d3920221d3970221d3922271d39782024623d02691d392323791d39717904691d3978276b1d3927791d3920201d3920271d3978771334696a131d3970241d392376061d3925201d3920791d397920011d3924731d3920721d3971770d1d392323076f161d3978201d3978767903061d3927751d397074241d3927791d' # 5K of 'A' char, but without padding offset yet cause im dumb.

flag 	= '551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b' # Hex of the flag
AA 		= '236625611d392070281d3971731d3922251d3923201d3922751d392423702f1d' # 32x'A' after resetting the offset by sending max len, this shall work.


def UNHEX(A:str): #Simple lazy unhex func
	return [ int(x, 16) for x in [A[i:i+2] for
		i in range(0, len(A), 2)] ]

B = UNHEX(Ax5K) # Pray for the brain to blind gods.
BB = UNHEX(AA)


def OTP_kraken(pattern:iter, char:str, type=1):
	print(f'''[*] OTP KRAKEN NO RIGHTS RESERVED
	USING pattern: {pattern} - {len(pattern)}
	USING char: {char} - {len(char)}\n''')

	result = []


	if type==1:
		for num in pattern:

			for XORKEY in range(0x111001):
				print(f'[*] {num} vs {XORKEY} #{len(result)}'+(' '*4),
					end='\r', flush=False)

				if num ^ XORKEY == ord(char):
					result.append(XORKEY)
					break
		
				if XORKEY == 0x111000:
					print(result)
					raise Exception('This wont work, 0x110000 reached.')
		print('[*] CIPHER FOUND :', result)
		return result


	if type==2: # For checking if the pico is in substr
		flag_index = 0
		for x in range(len(char)):
			for y in range(0x111000):
				XORKEY = y
				XORED = x ^ y
				print(f'[*] XORED {XORED} : {XORKEY}', flush=False,
					end='\r')
				if chr(XORED) == char[flag_index]:
					result.append(XORED)
					flag_index += 1 
					break
				if x > 110999:
					print(result)
					raise Exception('[*] Err, chr not found')
		return result


def showSecret(cipher:iter, secret:str): # Final move
	print('\n[*] Final args len:', len(cipher), len(secret)) #Should be in ratio 2:1
	
	secret_ints = [ int(x, 16) for x in [secret[i:i+2] for
		 i in range(0, len(secret), 2)] ]
	crackd = ''.join([chr(x ^ y) for
		x,y in zip(secret_ints, cipher)])
	crackd_ints = [ord(x) for x in list(crackd)] # Debug
	
	print('\n[*] FINAL RESULTS:', crackd_ints, crackd, sep='\n')
	return crackd


PICO = OTP_kraken(BB, flag_start, type=2)
print('[*] PICO substring found : ', PICO==[112, 105, 99, 111])


CIPHERTEXT = OTP_kraken(BB, 'A')
S = showSecret(CIPHERTEXT, flag)
print("".join([chr(x) for x in UNHEX(S)]))


