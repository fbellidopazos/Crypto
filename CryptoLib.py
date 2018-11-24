from random import randint
import sympy
#Comprueba que es primo
def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

#Genera Primos dado un n(numero de BITS)
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p

#Genera Primo anterior a numero dado
def lastprime(n):
    return(sympy.prevprime(n))


#Translate Text to Numb
def encode(word, cipher):
        res = ''
        i=0
        while(i!=len(word)):
                res=res+cipher[word[i]]
                i+=1
        return res

#Translate Numb to text
def deencode(word, cipher):
        res = ''
        i=0
        j=1
        while(i!=len(word)):
                res=res+cipher[str(word[i])+str(word[j])]
                i+=2
                j+=2
        return res

#Inverso en modulo n
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encrypt():
    encryption=[]
    # Receptor define p y q, primos
    p=generate_big_prime(256)
    q=generate_big_prime(256)
    encryption.append(p)
    encryption.append(q)
    # denifir n = p*q
    n=p*q
    encryption.append(n)
    # Numero menor que Phi(n)
    x=randint(0,1000)
    y=randint(0,1000)
    ee=lastprime((p-x)*(q-y)
    )
    encryption.append(ee)
    #Obtengo Clave Privada
    dd=modinv(ee,(p-1)*(q-1))
    encryption.append(dd)

    # 0=p
    # 1=q
    # 2=n
    # 3=ee
    # 4=dd
    return(encryption)
