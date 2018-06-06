# Data Encryption Standard - DES
DES is a **symetric-key block cipher**.<br/>
* Input : 64-bit plaintext blocks
* Key: 64 bits but only 56 are used - 8 are for parity checks
* Output : 64-bit ciphertext block

### Remarks:
* In this implementation, only one 64-bit key is used to encrypt/decrypt the whole message. We could decide to use a different key for each block.
* Even though only one key is used for an entire message, the subkeys are re-computed for each block. To be more efficient, we could decide to compute the subkeys only once and send them along with each block.

## THEORY
The DES algorithm is built on top of a **[Feistell structure](https://github.com/jbdrvl/cryptography/tree/master/feistel-cipher)**, with a very specific *f* function (Feistel function) to be used in each round:<br/>
<div style="text-align:center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/DES-main-network.png/250px-DES-main-network.png"/><p><i>from Wikipedia</i></p></div>

### Feistel Function for DES
Below is a representation of the Feistel Function for DES (*from Wikipedia*):<br/>
<div style="text-align:center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Data_Encription_Standard_Flow_Diagram.svg/250px-Data_Encription_Standard_Flow_Diagram.svg.png"/></div>

This Feistel function uses **subkeys** that are derived from the original key using a **key schedule** algorithm, which uses *rotations* to generate subkeys from the main key.<br/>
The first step is to expand the input into a 48-bit block to be able to *xor* it with the subkey: this is the **expansion** phase.<br/>
Then the (*block xor subkey*) block is passed through the **substitution** boxes, where the script uses pre-defined *S-boxes* to compute the output out of the input.<br/>
Finally, there is a permutation to re-arrange the output of the *S-boxes*.<br/>

## CODING
The script is divided into five sections:
1. The data section where all of the **permutation and substitution tables** are stored.
2. The main functions:
	* ```des()```: takes as input a plain text, divides it into 64-bit blocks, to then passes them to *desBlock()*.
	* ```desBlock()```: sub-function of *des()*, which is used to encrypt/decrypt a given block with a given key (this function can however be used independently).
	* ```f()```: the Feistel function used in each round of the Feistel cipher, specific to DES.
3. The secondary functions: mainly those in charge of the permutations and substitutions.
4. Utils: sub-functions used by the main and secondary functions.
5. Driver: gets the input from the terminal, generates a key, encrypts the message then tries to decrypt. Prints out the different variables.

## TESTING THE SCRIPT
The script can be used like this:
```sh
$ ./des.py "Hello World!"
Plain text =        Hello World!
Plain text (hexa) = 0x48656c6c6f20576f726c6421
Key =               0xc577f87f41488dc9
Encrypted (hexa) =  0x84ba9cb45625cbdfb19c989ac21644c0
Decrypted (hexa) =  0x48656c6c6f20576f726c642100000000
Decrypted =         Hello World!
```
If no input is given, "This is an example!" is the chosen plain text.

## SOURCES
* [Secure Communications course](http://www.eurecom.fr/en/course/SecCom-2017Fall) by [Refik MOLVA](http://www.eurecom.fr/en/people/molva-refik) from [EURECOM](http://www.eurecom.fr/en/eurecom/strategy).
* Wikipedia: [Presentation](https://en.wikipedia.org/wiki/Data_Encryption_Standard) and [supplementary material](https://en.wikipedia.org/wiki/DES_supplementary_material).

## License

    Copyright (C) 2018 Jean-Baptiste DURVILLE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
