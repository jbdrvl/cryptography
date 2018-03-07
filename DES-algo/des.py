#!/usr/bin/env python3
#!/usr/bin/env python

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

###### PERMUTATION AND SUBSTITUTION DATA ######

initialPermData = [None, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28,20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

finalPermData = [None, 40, 8, 48, 16, 56, 24, 64, 32, 39,	7, 47, 15, 	55, 23, 63, 31, 38,	6, 46, 14, 	54, 22, 62, 30, 37,	5, 45, 13, 	53, 21, 61, 29, 36,	4, 44, 12, 	52, 20, 60, 28, 35,	3, 43, 11, 	51, 19, 59, 27, 34,	2, 42, 10, 	50, 18, 58, 26, 33,	1, 41, 9 , 49, 17, 57, 25]

permutation = [None, 16, 7, 20, 21, 29, 12, 28, 17, 1, 15 ,23, 26, 5, 18, 31, 10, 2, 8, 24,	14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

pc1Left = [None, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]

pc1Right = [None, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

pc2Data = [None, 14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

S1 = [[14, 0, 4, 15],[4, 15, 1, 12],[13, 7, 14, 8],[1, 4, 8, 2],[2, 14, 13, 4],[15, 2, 6, 9],[11, 13, 2, 1],[8, 1, 11, 7],[3, 10, 15, 5],[10, 6, 12, 11],[6, 12, 9, 3],[12, 11, 7, 14],[5, 9, 3, 10],[9, 5, 10, 0],[0, 3, 5, 6],[7, 8, 0, 13]]

S2 = [[15, 3, 0, 13],[1, 13, 14, 8],[8, 4, 7, 10],[14, 7, 11, 1],[6, 15, 10, 3],[11, 2, 4, 15],[3, 8, 13, 4],[4, 14, 1, 2],[9, 12, 5, 11],[7, 0, 8, 6],[2, 1, 12, 7],[13, 10, 6, 12],[12, 6, 9, 0],[0, 9, 3, 5],[5, 11, 2, 14],[10, 5, 15, 9]]

S3 = [[10, 13, 13, 1],[0, 7, 6, 10],[9, 0, 4, 13],[14, 9, 9, 0],[6, 3, 8, 6],[3, 4, 15, 9],[15, 6, 3, 8],[5, 10, 0, 7],[1, 2, 11, 4],[13, 8, 1, 15],[12, 5, 2, 14],[7, 14, 12, 3],[11, 12, 5, 11],[4, 11, 10, 5],[2, 15, 14, 2],[8, 1, 7, 12]]

S4 = [[7, 13, 10, 3],[13, 8, 6, 15],[14, 11, 9, 0],[3, 5, 0, 6],[0, 6, 12, 10],[6, 15, 11, 1],[9, 0, 7, 13],[10, 3, 13, 8],[1, 4, 15, 9],[2, 7, 1, 4],[8, 2, 3, 5],[5, 12, 14, 11],[11, 1, 5, 12],[12, 10, 2, 7],[4, 14, 8, 2],[15, 9, 4, 14]]

S5 = [[2, 14, 4, 11],[12, 11, 2, 8],[4, 2, 1, 12],[1, 12, 11, 7],[7, 4, 10, 1],[10, 7, 13, 14],[11, 13, 7, 2],[6, 1, 8, 13],[8, 5, 15, 6],[5, 0, 9, 15],[3, 15, 12, 0],[15, 10, 5, 9],[13, 3, 6, 10],[0, 9, 3, 4],[14, 8, 0, 5],[9, 6, 14, 3]]

S6 = [[12, 10, 9, 4],[1, 15, 14, 3],[10, 4, 15, 2],[15, 2, 5, 12],[9, 7, 2, 9],[2, 12, 8, 5],[6, 9, 12, 15],[8, 5, 3, 10],[0, 6, 7, 11],[13, 1, 0, 14],[3, 13, 4, 1],[4, 14, 10, 7],[14, 0, 1, 6],[7, 11, 13, 0],[5, 3, 11, 8],[11, 8, 6, 13]]

S7 = [[4, 13, 1, 6],[11, 0, 4, 11],[2, 11, 11, 13],[14, 7, 13, 8],[15, 4, 12, 1],[0, 9, 3, 4],[8, 1, 7, 10],[13, 10, 14, 7],[3, 14, 10, 9],[12, 3, 15, 5],[9, 5, 6, 0],[7, 12, 8, 15],[5, 2, 0, 14],[10, 15, 5, 2],[6, 8, 9, 3],[1, 6, 2, 12]]

S8 = [[13, 1, 7, 2],[2, 15, 11, 1],[8, 13, 4, 14],[4, 8, 1, 7],[6, 10, 9, 4],[15, 3, 12, 10],[11, 7, 14, 8],[1, 4, 2, 13],[10, 12, 0, 15],[9, 5, 6, 12],[3, 6, 10, 9],[14, 11, 13, 0],[5, 0, 15, 3],[0, 14, 3, 5],[12, 9, 5, 6],[7, 2, 8, 11]]

S = [S1, S2, S3, S4, S5, S6, S7, S8]

############################################### 

##### MAIN FUNCTIONS #####

def des(inputText, key, decrypt=False):
	'''
		@input: inputText:	plain text as string of characters)
				key:		64 bits as one string)
				decrypt: 	boolean to whether we should encrypt or decrypt the input (encryption by default)
		@output: string of characters
	'''
	plain = toStr([binary(ord(letter)) for letter in list(inputText)])
	output = ""
	while len(plain)>64:
		tmp = plain[:64]
		plain = plain[64:]
		output = output + binToText(toStr(desBlock(tmp, key, decrypt)))
	if len(plain)==0: return output
	while len(plain)!=64:
		plain = plain + "00000000"
	return output + binToText(desBlock(plain, key, decrypt))

def desBlock(block, key, decrypt=False):
	'''
		receives a 64-bit block and applies the DES algorithm to encrypt (or decrypt) it with the given key
	'''
	assert len(block)==64
	assert len(key)==64
	keys = genSubKeys(key)
	if decrypt: keys.reverse()
	inp = initialPerm(block)
	# Fiestel cipher:
	for subKey in keys:
		L, R = split(inp)
		Ln = xor(L, f(R, subKey))
		inp = toStr(R)+Ln
	output = finalPerm(Ln, R)
	return toStr(output)

def f(half, subKey):
	'''
		specific F function used in each round of the Fiestel stucture, for DES
	'''
	assert len(half)==32
	assert len(subKey)==48
	left = expansion(half)
	keyMix = xor(left, subKey)
	tmp = substit(keyMix)
	return permut(tmp)
    
##### SECONDARY FUNCTIONS #####

def initialPerm(block):
	return [block[initialPermData[i]-1] for i in range(1,len(initialPermData))]
	
def finalPerm(Ln, R):
	block = Ln+R
	return [block[finalPermData[i]-1] for i in range(1,len(finalPermData))]
	
def expansion(a):
	a = toStr(a)
	tmp=[]
	for i in range(8):
		inter=""
		if i==0:
			inter = a[-1] + a[:5]
		elif i==7:
			inter = a[-5:] + a[0]
		else:
			inter = a[i*6-(2*i+1): (i+1)*6-(2*i+2)+1]
		tmp.append(inter)
	output=""
	for j in tmp:
		output = output+j
	return output
	
def substit(inp):
	assert len(inp)==48
	pieces = []
	for i in range(8):
		pieces.append(inp[:6])
		inp = inp[6:]
	output = ""
	for i, piece in enumerate(pieces):
		output = output + binary(S[i][int(piece[1:-1], 2)][int(piece[0]+piece[-1], 2)])
	return output
	
def permut(inp):
	return [inp[permutation[i]-1] for i in range(1,len(permutation))]

def genSubKeys(key):
	key = pc1(key) # now of length 56
	keys = [] # subkeys of length 48
	L, R = split(key)
	for i in range(1, 17):
		L = rot(L, i)
		R = rot(R, i)
		keys.append(pc2(L, R))
	return keys

def pc1(key):
	left=""; right=""
	for i in range(1, len(pc1Left)):
		left=left+key[pc1Left[i]-1]
		right=right+key[pc1Right[i]-1]
	return left+right
	
def pc2(L, R):
	inp = L+R
	tmp = [inp[pc2Data[i]-1] for i in range(1, len(pc2Data))]
	output=""
	for elem in tmp:
		output = output + elem
	return output


##### UTILS #####

def rot(inp, roundNbr):
	if roundNbr in [1, 2, 9, 16]:
		offset = 1
	else:
		offset = 2
	return inp[offset:]+inp[:offset]

def split(inp):
    assert len(inp)%2==0
    return inp[:int(len(inp)/2)], inp[int(len(inp)/2):]
    
def xor(a, b):
    output=""
    for i in range(len(a)):
        inter=int(a[i])+int(b[i])
        if inter==2: inter=0
        output = output+str(inter)
    return output

def keyGen(length, nbrKeys):
    output=[]
    for i in range(nbrKeys):
        k=""
        for i in range(length):
            k = k + str(rd.randint(0, 1))
        output.append(k)
    return output

def binToHex(binar):
	res="0x"
	hexList = [hex(int(binar[i:i+8], 2))[2:] for i in range(0, len(binar),8)]
	for hexa in hexList:
		if len(hexa)==1: hexa ="0"+hexa
		res = res + hexa
	return res
    
def toStr(charList):
	'''
	charList should be a list of characters
	concatenates all the characters from the list and returns the final string
	'''
	res = ""
	for letter in charList:
		res = res+letter
	return res
   
def binToText(inp):
	# inp is a string of binary digits corresponding to several bytes. e.g. '1001010011101011'
	assert len(inp)%8==0
	output = ""
	while len(inp)!=0:
		output = output + chr(int(inp[:8], 2))
		inp = inp[8:]
	return output

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

##### MAIN #####

if __name__=="__main__":
	try:
		text = sys.argv[1]
	except:
		text = "This is an example!"
	key = keyGen(64, 1)[0]
	encrypted = des(text, key)
	decrypted = des(encrypted, key, True)
	print("Plain text =        {}".format(text))
	print("Plain text (hexa) = {}".format(binToHex(toStr([binary(ord(letter)) for letter in text]))))
	print("Key =               {}".format(binToHex(key)))
	print("Encrypted (hexa) =  {}".format(binToHex(toStr([binary(ord(letter)) for letter in encrypted]))))
	print("Decrypted (hexa) =  {}".format(binToHex(toStr([binary(ord(letter)) for letter in decrypted]))))
	print("Decrypted =         {}".format(decrypted))
