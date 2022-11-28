from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def rsa_deep_dive():
    """"
    RSA deep dive
     Args:
        None
     Returns:
           None
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    plain_text = "Swapnil we got this"
    print("plain text")
    print(plain_text)
    print("private number")
    pvt_numbers = private_key.private_numbers()
    print("p")
    print(pvt_numbers.p)
    print("q")
    print(pvt_numbers.q)
    print("d")
    print(pvt_numbers.d)

    #print(private_key)
    pub_key = private_key.public_key()
    print("public  num")
    pub_number = pub_key.public_numbers()
    e = pub_number.e
    n = pub_number.n
    print("n")
    print(n)
    print("e")
    print(e)

    plain_text_bytes = str.encode(plain_text)
    ciphertext = pub_key.encrypt(
        plain_text_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),

            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Cipher Text")
    #cipher_text = ciphertext.decode()
    print(ciphertext)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    plaintext = plaintext.decode('unicode_escape')
    print("Plain Text Recovered")
    print(plaintext)
    print("Plain Text Check")
    check = plaintext == plain_text
    print(check)

