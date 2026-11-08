# ElGamal Encryption

A simple Python implementation of the ElGamal asymmetric encryption algorithm. The program generates a key pair (public and private), encrypts user-inputted text character by character, and decrypts it back to the original string.

## Features

* Generates a random prime number `p` in the range from 10,000 to 10,000,000.
* Finds a primitive root `g` modulo `p`.
* Generates a public key `(y, g, p)` and a private key `x`.
* Encrypts text character by character using a random ephemeral session key `k`.
* Decrypts the resulting list of `(a, b)` pairs back into the original string.

## Requirements

* Python 3.8 or higher (uses the built-in `pow(a, -x, p)` function to compute the modular multiplicative inverse).
* No external libraries required (uses only the built-in `random` module).


## Example Output

After running the script, enter the text you want to encrypt. The program will output the generated keys, the ciphertext, and the decrypted message:

```text
Input text for shifrator: Hello
public key y: 4829104
public key g: 7
public key p: 8392019
secret key x: 192837
How string will be look like in Internet: 5192834918273...
[(519283, 4918273), (102938, 7483920), ...]
Hello
```

## Security Disclaimer ⚠️

This project is created for educational purposes to demonstrate the mathematics behind the algorithm. For real-world data protection, the prime number `p` should be at least 2048 bits long, and the cryptographically secure `secrets` module should be used instead of `random`.
