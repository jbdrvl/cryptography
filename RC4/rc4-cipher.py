#!/usr/bin/env python
#!/usr/bin/env python3

#######################################################################
# 
# Copyright (C) 2018 Jean-Baptiste DURVILLE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#
####################################################################### 

import random as rd
import sys

## BASIC FUNCTIONS used for conversions from one notation to another

def binary(a):
	'''
	a should be a positive integer smaller than 256
	returns the 8-bit binary writing of a
	'''
	assert a<256
	res = bin(a)[2:]
	while len(res)!=8:
		res = "0"+res
	return res

def toInts(text):
	'''
	@input: text: type(text) = string
	@output: list of the ASCII number of each character of text
	'''
	return [ord(letter) for letter in text]

def toBytes(intList):
	'''
	@intput: intList: type(intList) = list of integers
	@output: string with the different integers written in hexadecimal notation
	'''
	res = "0x"
	for integer in intList:
		hexa = hex(integer)[2:]
		if len(hexa)==1: hexa = '0'+hexa
		res = res + hexa
	return res

def toChar(intList):
	'''
	@intput: intList: type(intList) = list of integers
	@output: list of characters corresponding to the integers it got as inputs (using ASCII)
	'''
	return [chr(integer) for integer in intList]

def toStr(charList):
	'''
	charList should be a list of characters
	concatenates all the characters from the list and returns the final string
	'''
	res = ""
	for letter in charList:
		res = res+letter
	return res

## ENCRYPT/DECRYPT FUNCTIONS

def xor(a, b):
	'''
	@signature: int xor(int a, int b) - all in base 10
	returns the integer corresponding to the binary XOR operation between a and b
	'''
	a = binary(a)
	b = binary(b)
	assert (len(a)==8 and len(b)==8)
	output=""
	for i in range(len(a)):
	#print(i, a, b)
		inter=int(a[i])+int(b[i])
		if inter==2: inter=0
		output = output+str(inter)
	return int(output, 2)

def schedule(key):
	'''
	KSA: Key Schedule Algorithm
	key should be a list of positive integers (<256)
	creates S as the list of all possible bytes (base 10 integers from 0 to 255)
	shuffles S with the help of the key, using the main method from the Pseudo-Random Generation Algo (PRGA)
	'''
	S = [i for i in range(256)]
	j=0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]
	return S

def cipher(inputText, S):
	'''
	encrypts plainText with S, using the RC4 algorithm
	'''
	inputInts = toInts(inputText)
	i=0; j=0
	outputInts = []
	for elem in inputInts:
		i = (i+1) % 256
		j = (j+S[i]) % 256
		S[i], S[j] = S[j], S[i]
		t = (S[i]+S[j]) % 256
		outputInts.append(xor(elem, S[t]))
	return toChar(outputInts)

def genKey(l=16):
	'''
	generates a random key of length l bytes (16 by default)
	'''
	return [rd.randint(0,255) for i in range(l)]

## TEST SCRIPT

if __name__ == "__main__":
	if len(sys.argv)>3:
		print('[ERROR] too many arguments! If you want to encrypt a message with spaces, you will need to put quotes around it.')
		print('Example: ./rc4-cipher.py "Hello World!" "MySecretKey"')
		exit()
	# get plainText
	try:
		plainText = sys.argv[1]
	except:
		print("[ERROR] missing argument! Please add a message (and your key if you have one) to encrypt.\nExample: ./rc4-cipher.py Hello! secretKey")
		exit()
	# get secret key
	try:
		myKey = toInts(sys.argv[2])
		print("[INFO] using your key: {}".format(sys.argv[2]))
	except:
		myKey = genKey() # or use myKey=toInts("YourOwnSecretString")
		print("[INFO] using a randomly-generated key")
	print('Plain text: {}'.format(plainText))
	print('Secret Key: {}'.format(toBytes(myKey)))
	cipherText = cipher(plainText, schedule(myKey))
	print('Cipher bytes: {}'.format(toBytes(toInts(cipherText))))
	print('Result after decrypting: {}'.format(toStr(cipher(cipherText, schedule(myKey)))))








