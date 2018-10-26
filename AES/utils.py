from sboxes import Sbox, Sbox_inv

def double(a):
    if (a&0x80)>>7==1:
        return (a<<1)^0x11b # operation known as "xtime" in initial AES proposal
    else:
        return a*2

def rotWord(word):
    # word = [a b c d]; return [b c d a]
    assert len(word)==4
    return word[1:]+[word[0]]

def subWord(word):
    # word = [a b c d]; return [S(a) S(b) S(c) S(d)]
    assert len(word)==4
    return [Sbox[word[i]] for i in range(4)]
