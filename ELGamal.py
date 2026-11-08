import random
def check_on_common_numbers(p):
    num=2
    if p <=1:
        return False
    elif p==2:
        return True
    while True:
        if(p % num ==0):
            return False
        elif num*num>p:
            return True
        else:
            num+=1
def is_primary_root(p,factors):
    while True:
        is_good = True
        g=random.randint(2,p-1)
        for i in factors:
         if pow(g,(p-1)//i,p)==1:
            is_good=False
            break
        if(is_good==True):
            return g

def simple_multipliers(p):
    n=p-1
    d=2
    factors=set()
    while d*d<=n:
       if(n % d == 0):
        factors.add(d)
        while n%d==0:
            n=n//d
       d += 1
    if(n>1):
        factors.add(n)
    return factors

def generator_key():
    while True:
     p=random.randint(10000,10000000)
     if check_on_common_numbers(p):
        break
    x=random.randint(2,p-2)
    g=is_primary_root(p,simple_multipliers(p))
    y=pow(g,x,p)
    return y,g,p,x
def elgamal_encode(text,y,g,p):
    cipher_text = []
    string_cipher=""
    for i in text:
       if ord(i)<p:
        k = random.randint(1, p - 1)
        a=pow(g,k,p)
        b=(ord(i)*pow(y,k,p))%p
        cipher_text.append((a,b))
        string_cipher+=(str(a)+str(b))
       else:
           print("Symbol is to Huge")
           return None
    print(f"How string will be look like in Internet: {string_cipher}")
    return cipher_text

def elgamal_decode(cipher_text,x,p):
    decode_string=""
    for a,b in cipher_text:
        m=(b*pow(a,-x,p))%p
        decode_string+=chr(m)
    return decode_string
text=input("Input text for shifrator: ").strip()
y,g,p,x=generator_key()
print(f"public key y: {y}")
print(f"public key g: {g}")
print(f"public key p: {p}")
print(f"secret key x: {x}")
encode=elgamal_encode(text,y,g,p)
decode=elgamal_decode(encode,x,p)
print(encode)
print(decode)
