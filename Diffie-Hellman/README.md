# Diffie-Hellman Key Exchange
The Diffie-Hellman Key Exchange Algorithm is designed for two parties (Alice and Bob) to decide on a mutual secret key (Kab).<br/>
It can be used to agree on a common secret key over an insecure channel.

## THEORY
* Alice first chooses a prime number *p*, then *x* a primitive element of *p* (*x* in *Zp*).
*p* and *x* are public.
* Alice then chooses her private integer *a*: 0<*a*<*p*-2.
* Bob, who wishes to communicate with Alice, chooses its own private integer *b*: 0<*b*<*p*-2.
* Bob sends Alice *x^b mod p*, and Alice sends Bob *x^a mod p*.
* Alice can then compute *(x^a)^b mod p* and Bob, *(x^b)^a mod p*.

The private key *Kab* shared by Alice and Bob is *x^(ab) mod p*.

<!--![Diffie-Hellman Key Exchange Chart]()-->

The security of the exchange comes from the fact that it is computationally very hard to deduce *a* from *x^a mod p*, even if *x* and *p* are known.

## CODING
Coding the exchange is fairly straight forward. The difficulties come in when using large numbers.<br/>
To decide whether *p* is prime, the **Miller-Rabin algorithm** is used, which returns whether *p* is 'probably' prime.<br/>
To process with the modular exponentions, I used a mix of the **fast exponention** algorithm and the **modular exponention** one.

## TESTING THE SCRIPT

To test the script, just launch ```./dh.py``` in a shell:<br/>

```sh
$ ./dh.py
[PUBLIC]             p = 3655369
[PUBLIC]             x = 3496630
[SECRET A]           a = 2976908
[SECRET B]           b = 2595246
[PUBLIC] A -> B:     x^a mod p = 1586746
[PUBLIC] B -> A:     x^b mod p = 1229592
[SECRET A,B]         Kab = 4173716
[SECRET A,B]         Kba = 4173716
```

There is a **verbose option** to display more information on each step of the process. To use it, launch ```./dh.py -v```.<br/>
The script works for integers as big as *2^2048*.

## SOURCES
* [Secure Communications course](http://www.eurecom.fr/en/course/SecCom-2017Fall) by [Refik MOLVA](http://www.eurecom.fr/en/people/molva-refik) from [EURECOM](http://www.eurecom.fr/en/eurecom/strategy)

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
