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
import math as ma
	
def findPrime(mini,maxi):
    '''
        returns a number p (probably) prime, p being between mini and maxi.
    '''
    p = rd.randint(mini,maxi)
    counter=1
    if p%2==0: p+= 1
    while not millerRabin(p) and counter<ma.log(p):
        p+=2
        counter+=1
    if counter==ma.log(p): raise TimeoutError
    return p
    
def millerRabin(n):
    '''
    	receives as argument a 'large' number n (>0)
    	returns if n in composite (False) or probably prime (True)
    '''
    if int(n)!=n: raise TypeError("type(n) must be: <integer>. n = {}, and type(n) = {}".format(n,type(n))) # no floats allowed
    if n<0: raise ValueError("we want n>=0 and we got: n = {}".format(n)) # no negative ints
    if n==2: return False
    if n%2==0: return False # no even int
    puisDeux = puissancesDeux(n-1)
    t = puisDeux[0]
    s = puisDeux[1]
    a = rd.randint(1,n-1)
    q = puissanceModulaire(a,t,n)
    if q==1 or q==n-1: return True
    for i in range(1,s+1):
        q=(q*q)%n
        if q==n-1:
            return True
    return False

def puissancesDeux(n):
    '''
    	receives as arg an integer n>=0
    	returns (t,s) such that n = t * 2**s (using binary)
    '''
    s= 0; l = binary(n)
    while l[0]!=1:
        s+=1
        l = l[1:]
    m=''
    l.reverse()
    for i in l:
        m=m+str(i)
    return [int(m,2),s]
    
def binary(n):
    '''
    	receives as arg an integer n
    	returns the binary writing of n as a table of 1's and 0's (table is not reversed)
    '''
    try: int(n)
    except: raise TypeError('expecting type(n) = integer. got {}'.format(type(n)))
    l=[]
    while n>0:
        l.append(n%2)
        n=n//2
    return l

def puissanceModulaire(a,b,n):
    '''
    	receives as args three integers a, b, n
    	returns a**b mod n
    	prgm is a mix of modular exponention and fast exponention algorithms
        compilation du puisMod() (source = Theorie des Codes) et exponentiation_rapide() (made in MPSI 2)
    '''
    assert b>=0
    assert n>=0
    x = 1; m = b; r = [a%n]
    l = binary(m)
    for i in range(len(l)+1):
        r.append((r[i]**2)%n) # r[i+1] = r[i] ** 2
    for i in range(len(l)):
        if l[i]==1: x*=r[i]
    return x%n


if __name__=="__main__":
	try:
		v = sys.argv[1]
		verbose = False
		if v=="-v": verbose = True
	except:
		verbose = False
	# PRINTS
	if verbose: print("Finding a large prime 'p':")
	p = findPrime(100000,5000000) # p is a large prime
	print("[PUBLIC]             p = {}".format(p))
	if verbose: print('')
	if verbose: print("Finding 'x' a primitive element of Zp (lower than p):")
	x = rd.randint(2,p-1) # x is a primitive elem of Zp (!=0)
	print("[PUBLIC]             x = {}".format(x))
	if verbose: print('')
	if verbose: print("A chooses a (0 < a < p-2) as its secret:")
	a = rd.randint(1,p-3) # 0 < a < p-2
	print("[SECRET A]           a = {}".format(a))
	if verbose: print('')
	if verbose: print("B chooses b (0 < b < p-2) as its secret:")
	b = rd.randint(1,p-3) # 0 < b < p-2
	print("[SECRET B]           b = {}".format(b))
	if verbose: print('')
	alpha = x^a % p
	if verbose: print("A sends its key information to B")
	# A sends x^a mod p
	print("[PUBLIC] A -> B:     x^a mod p = {}".format(alpha))
	if verbose: print('')
	beta = x^b % p
	if verbose: print("B sends its key information to A")
	# B sends x^b mod p
	print("[PUBLIC] B -> A:     x^b mod p = {}".format(beta))
	if verbose: print('')
	k = beta^a % p
	if verbose: print("A compute the shared key")
	print("[SECRET A,B]         Kab = {}".format(alpha^b % p))
	if verbose: print('')
	# common key is x^(ab) mod p 
	if verbose: print("A compute the shared key")
	print("[SECRET A,B]         Kba = {}".format(k))
	
