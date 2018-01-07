# RC4 Algorithm
This Python script is meant to present the basic RC4 algorithm, which is/was used in WEP, WPA, TLS/SSL (now prohibited), and [more](https://en.wikipedia.org/wiki/RC4#RC4-based_protocols).

## THEORY
RC4 is a **stream cipher**: it encrypts/decrypts all bytes one at a time.<br/>
To do so, it generates a **pseudo-random keystream** with the help of a secret key, and uses it to encrypt the plainText with a binary XOR, byte after byte.<br/>
The decryption process works the same way as the encryption, since we are using a XOR operation.<br/>

### Generating the pseudo-random keystream: KSA
The script creates an array S, containing all of the possible bytes (ie. all of the integers in [0, 255])<br/>
The Key Schedule Algorithm (KSA) uses the key to shuffle S, which becomes the pseudo-random keystream.

### Encryption and Decryption
The actual encryption/decryption function works a bit like KSA: it pseudo-randomly chooses a byte from S to encrypt a byte from the plainText/cipherText (using XOR). 

## CODING
The script is divided into three main parts:
* conversion functions, which are just used to switch from one type to another (e.g. convert the plain text into a list of integers).
* encryption/decryption functions, which are the KSA (key schedule algorithm) ```schedule()```, the actual encrypting/decrypting function ```cipher()```, the key generation function ```genKey()```, and the binary XOR function ```xor```.
* the "main", which gets the plainText (and the key) from stdin, and calls the different functions to encrypt then decryupt the plainText. It's also where all the ```print()``` are called.

## TESTING THE SCRIPT
The user can either choose his/her own key, or let the script randomly choose one.
* Using "MySecretKey" as key:
```sh
$ ./rc4-cipher.py "The message to be encrypted" "MySecretKey"
[INFO] using your key: MySecretKey
Plain text: The message to be encrypted
Secret Key: 0x4d795365637265744b6579
Cipher bytes: 0x556eb3a1b5ed4a2fdcbba263286885cfcd4cf4a3d89264a1d9d0a4
Result after decrypting: The message to be encrypted
```
* Using a script-generated random key:
```sh
$ ./rc4-cipher.py "My message"
[INFO] using a randomly-generated key
Plain text: My message
Secret Key: 0xbe839965d882a90ea5cfc1a589f12897
Cipher bytes: 0x99b0bd45ae2b4dfb9c41
Result after decrypting: My message
```

## SOURCES
* [Secure Communications course](http://www.eurecom.fr/en/course/SecCom-2017Fall) by [Refik MOLVA](http://www.eurecom.fr/en/people/molva-refik) from [EURECOM](http://www.eurecom.fr/en/eurecom/strategy)
* [GitHub user g2jun](https://github.com/g2jun/RC4-Python)
* [Wikipedia](https://en.wikipedia.org/wiki/RC4)
