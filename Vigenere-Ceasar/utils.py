'''
Author:         JB Durville (github.com/jbdrvl)
Date:           July 2018
Description:    Functions to be used to test and use Ceasar and Vigenere ciphers.
                I first coded them in 2014 (or 2015 idk), and recently had to
                    rewrite them for a CTF. So here they are.
License:        GPL-3.0
'''

## encoding

def encode(strg):
    '''
    encode(strg) returns a list of integers ([0,25]), where each integer is the number in the alphabet of its corresponding letter in *strg*, with A: 0 and Z: 25.
        type(strg) = string
    '''
    return [ord(strg[i])-65 for i in range(len(strg))]

def decode(lst):
    '''
    decode(lst) returns a string made of letters corresponding to the integers in *lst*. This is the inverse of *encode(strg)*.
        type(lst) = list
    '''
    rep=""
    for i in range(len(lst)):
        rep=rep+chr(lst[i]+65)
    return rep

def digestResult(original_text, cipher_block):
    '''
    digestResult(original_text, cipher_block) returns the text from
            *cipher_block* with the right punctuation and numbers from *original_text*.
        Since the Vigenere scripts only use strings made of uppercase letters,
            we lose all of the other characters (!.?,0-9').
        So this script takes *original_text* (which has all of the original characters),
            replaces the letters by their encrypted equivalent (from *cipher_block*)
            and keeps the other characters unchanged.
        type(original_text) = type(cipher_block) = string
    '''
    block_list = list(cipher_block)
    res=""
    for char in original_text:
        if ord(char) in range(97, 123):
            # lowercase letter
            res = res + block_list.pop(0).lower()
        elif ord(char) in range(65, 91):
            # uppercase letter
            res = res + block_list.pop(0)
        else:
            res = res + char
    return res

## Ceasar

def ceasar(msg,offset):
    '''
    ceasar(msg,offset) returns a string out of *msg* by shifting all of its letter's numbers by *offset* modulo 26
        type(msg) = string
        type(offset) = integer
    '''
    lis=encode(msg)
    for i in range(len(lis)):
        lis[i]+=offset
        while lis[i]>25:
            lis[i]-=26
        while lis[i]<0:
            lis[i]+=26
    return decode(lis)

def crackCeasar(txt):
    f=smallestDiff(txt)
    return ceasar(txt,-f)

## Vigenere

def crackVigenere(txt, knowLength=False, keyL=0):
    '''
    crackVigenere(txt) returns the (most probable) decrypted version of *txt* if it was encrypted with Vigenere's cipher (and the most probable key)
        type(txt) = string
        Example:    crackVigenere(encrypted_msg)
                    crackVigenere(encrypted_msg, True, 11)
    '''
    if not knowLength:
        return viginv(txt,searchKey(txt,lengthKey(txt))),searchKey(txt,lengthKey(txt))
    return viginv(txt,searchKey(txt,keyL)),searchKey(txt,keyL)

def vigenere(msg,key):
    '''
    vigenere(msg,key) encrypts *txt* with *key* using Vigenere's cipher
        type(msg) = type(key) = string
    '''
    lis=encode(msg)
    keylis=encode(key)
    j=0
    for i in range(len(lis)):
        if j==len(keylis):j=0
        lis[i]+=keylis[j]
        if lis[i]>25:lis[i]-=26
        j+=1
    return decode(lis)

def viginv(txt,key):
    '''
    viginv(txt,key) decrypts *txt* with *key* using Vigenere's cipher
        type(txt) = type(key) = string
    '''
    lis=encode(txt)
    keylis=encode(key)
    j=0
    for i in range(len(lis)):
        if j==len(keylis):j=0
        lis[i]-=keylis[j]
        if lis[i]<0:lis[i]+=26
        j+=1
    return decode(lis)

## Utils

def smallestDiff(txt):
    rep=[d(ceasar(txt,-i)) for i in range(0,26)]
    return rep.index(min(rep))

def frequencies(txt):
    '''
    frequencies(txt) returns the normalized list of the frequencies of the 26 letters of the alphabet that appear in *txt*
        txt:
            type(txt) = string
    '''
    lis=encode(txt)
    fre=[0 for i in range(0,26)]
    for i in lis: fre[i]+=1
    m=max(fre)
    return [round(fre[i]/m,5) for i in range(len(fre))]

def difference(lst,fre):
    return sum([(lst[i]-fre[i])**2 for i in range(0,26)])

def d(txt):
    french_frq=[0.48667,0.06141,0.17555,0.24217,1,0.06489,0.07358,0.05330,0.42526,0.01796,0.00290,0.34820,0.17150,0.41309,0.30475,0.17439,0.05736,0.37949,0.46813,0.40962,0.33256,0.07648,0.00232,0.02607,0.01738,0.00695] # french frequencies
    # need to implement frequencies for other languages
    return difference(french_frq,frequencies(txt))

def repetitions(txt,mini=2,maxi=4,la=5,lb=24):
    '''
    repetitions(txt) returns the list of distances between different identical substrings and the number of times these are found in *txt*
        type(txt) = string
        script only studies substrings that are of length l such that: *mini* <= l < *maxi*
            type(mini) = type(maxi) = integer
        script only keeps the ditances between two identical substrings that are between *la* and *lb*
            type(la) = type(lb) = interger
    '''
    rep2=[]
    for i in range(mini,maxi):
        l=[i] # lst of substrings
        l += [txt[j:j+i] for j in range(len(txt)-i)]
        distances=[]
        for j in range(1,len(l)):
            indx=j
            dist=0
            while indx!=len(l):
                found=txt.find(l[j],indx)
                if found!=-1:
                    dist=found-j+1
                    rep2.append(dist)
                    indx=found
                indx+=1
    rep=[]
    for i in range(la,lb+1):
        n=0
        for j in rep2:
            if j%i==0: n+=1
        rep.append((i,n))
    return rep

def lengthKey(txt):
    '''
    lengthKey(txt) returns the length of the most probable key (as an integer) used to encrypt *txt* using Vigenere's cipher
        type(txt) = string
    '''
    lis=repetitions(txt,2,4,4)
    repet=4  # by default
    lg_key=5 # by default
    for i in range(len(lis)):
        (a,b)=lis[i]
        if repet<=b:
            repet=b
            lg_key=a
    return lg_key

def searchKey(txt,lg_key):
    '''
    searchKey(txt,lg_key) returns the value of the most probable key (as a string) used to encrypt *txt* using Vigenere's cipher
        type(txt) = string
        type(lg_key) = integer
    '''
    st=[] # lst sous-txts
    for i in range(0,lg_key):
        k=i
        st.append('')
        while k<len(txt):
            st[i]=st[i]+txt[k]
            k+=lg_key
    liskeys=[]
    for i in range(len(st)):
        liskeys.append(smallestDiff(st[i]))
    return decode(liskeys)

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
