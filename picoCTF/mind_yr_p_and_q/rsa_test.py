import os, sys, traceback, math, rsa, decimal, ctypes as cpp
import numpy as np
from functools import lru_cache
from Crypto.Util.number import inverse

data = {
#	Crypted flag I guess:
'c': 8533139361076999596208540806559574687666062896040360148742851107661304651861689,
#	N is too high, currently uncrackable:
'n': 769457290801263793712740792519696786147248001937382943813345728685422050738403253,
#	Result of floor(sqrt(n)): 
'nfloorsqrt' : 27739093186354592758038385582855288027292,
'e': 65537,
#	[According to factordb.com]:
'p':1617549722683965197900599011412144490161,
'q':475693130177488446807040098678772442581573,
}
phi = (data.get('p')-1) * (data.get('q')-1)
print('[*] phi ==',phi)
d = inverse(data.get('e'), phi)
print('[*] d ==',d)
m = pow(data.get('c'), d, data.get('n'))
print('[*] m ==', m)
print(bytearray.fromhex(hex(m)[2:]))



decimal.getcontext().prec=100000000000000000

#	Function to get manual starting point of floor(sqrt(int)):
def start_point(largeInt:int):
	print('[*] Initial value:', largeInt)
	largeInt = decimal.Decimal(largeInt)
	startPoint = math.floor(largeInt.sqrt())
	print('[*] Starting pt:', startPoint)
	return decimal.Decimal(startPoint)


@lru_cache(maxsize=None, typed=True)
def is_prime(number:int):
	nah = ('0', '2', '4', '6', '8')
	if str(number)[-1] in nah: return False
	for x in range(3, number//2, 2):
		if not number % x: return False
	return True


@lru_cache(maxsize=None, typed=True)
def prime_list(number:int):
	ret_list = []
	for n in range(number):
		if is_prime(n):
			ret_list.append(str(n))
			print(str(n)+(' '*16), flush=False, end='\r')
	print(len(ret_list))
	return ret_list


@lru_cache(maxsize=None, typed=True)
def cracker(floorskrt:int):
	"""
	Typical attack on low N.
	If length of N is more than 30 integers it is NOT low, 
	and no vertical nor horizontal scaling can help, ie:
	879600874757565786163347170 approx days needed to exhaust the search,
	(on len-42 int while doing 1M mod checks per sec).
	However, sometimes it can get lucky if P is close to startPoint. 
	"""
	floorskrt = decimal.Decimal(data.get('nfloorsqrt'))
	unknown = decimal.Decimal(data.get('n'))
	if not floorskrt % 2 : 
		floorskrt = floorskrt-1
		traceback.print_exc()
		#	( N is supposed to be a product of 2 smaller primes p*q )
		print('[*]This does not look like a prime factor, success is unlikely') 
	for i in range(int(floorskrt), 3, -2):
		print(f'{i}'+(' '*16), end='\r', flush=False)
		if unknown % i == 0:
			print('[*] Cracked with ', i)
			return i
	print('[*] Failed successfully.')

