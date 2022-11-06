from cryptography.hazmat.primitives.asymmetric import rsa
import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def avg(ls):
    """"
    Args:
        ls : list of numbers
    Returns:
          return average of ls
    """
    return sum(ls) / len(ls)


def rsa_time(plain_text_bytes, key_size=512, iterations=1):
    """Generates key for specified key size and returns with time of generation in milli seconds

    Args:
        plain_text_bytes (bytes) : Plain text to be encrypted
        key_size (int): Key size for key generation more than 512  ( default is 512)
        iterations (int): no. of iterations for average time per operation  ( default is 1)

    Returns:
        list: a list of key_size, avg_key_generation_time,  avg_encryption_time, avg_decryption_time
          """
# block size 512-bits, and it has a word size of 32-bits
    key_time = []
    enc_time = []
    dec_time = []
    for iteration in range(iterations):
        key_init_time = time.time()
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            )
        key_end_time = time.time()
        key_time_diff = key_end_time - key_init_time
        key_time.append(key_time_diff)
        public_key = private_key.public_key()
        #   plain_text_bytes = bytes(plain_text, 'utf-8')
        enc_init_time = time.time()
        cipher = public_key.encrypt(
            plain_text_bytes, padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(), label=None))
        enc_end_time = time.time()
        enc_time_diff = enc_end_time - enc_init_time
        enc_time.append(enc_time_diff)
        dec_init_time = time.time()
        plain_text = private_key.decrypt(
            cipher, padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
                ))
        dec_end_time = time.time()
        dec_time_diff = dec_end_time - dec_init_time
        dec_time.append(dec_time_diff)
        #   print("plain is : {msg}".format(msg=plain_text))
    #   key_size = private_key.key_size
    #   print(private_key.key_size)
    #   pub_key=private_key.public_key()
    #   pvt_num = private_key.private_numbers()
    #   p=pvt_num.p
    #   q=pvt_num.q
    time_factor = 100000
    key_avg = avg(key_time)*time_factor
    enc_avg = avg(enc_time)*time_factor
    dec_avg = avg(dec_time)*time_factor
    print('Key Size {size},Key {key_time} Enc {enc_time}, Dec {dec_time}.'
          .format(size=key_size, key_time=key_avg, enc_time=enc_avg, dec_time=dec_avg))
    ls = [key_size, key_avg, enc_avg, dec_avg]
    return ls

    #   print(private_key)


"""def rsa_enc_time(public_key, plain_text, iterations=1):
    '''Generates encrypts for plain text with specific public key and returns with time of generation in milli seconds

    Args:
        public_key (RSAPublicKey): RSAPublicKey to be used for  encryption
        plain_text (str): Plain text to be encrypted
        iterations (int): no. of iterations for average time per operation  ( default is 1)

    Returns:
        list: a list of RSAPrivateKey object and time of execution
          '''
    init_time = time.time()
    cipher = ''
    for iteration in range(iterations):
        cipher = public_key.encrypt(
            plain_text, padding
            )
    #   key_size = private_key.key_size
    #   print(private_key.key_size)
    #   pub_key=private_key.public_key()
    #   pvt_num = private_key.private_numbers()
    #   p=pvt_num.p
    #   q=pvt_num.q

    end_time = time.time()
    time_factor = 1000
    program_time = ((end_time-init_time)*time_factor)/iterations

    print('Time is  {time},Encrypted {encrypted}.'.format(time=program_time, encrypted=cipher.decode()))
    ls = [cipher, program_time]
    return ls

    #   print(private_key)
"""