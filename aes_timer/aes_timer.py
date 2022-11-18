import time
import os
import secrets
from handy_function.math_function import avg
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#   ------------work in progress##############


def aes_time(plain_text_bytes, time_factor, key_size=128, iterations=1):
    """Generates key for specified key size and returns with time of generation in mprovided time factor

    Args:
        plain_text_bytes (bytes) : Plain text to be encrypted
        time_factor (int) : time factor to multiply values by
        key_size (int): Key size for key generation more than 512  ( default is 32)
        iterations (int): no. of iterations for average time per operation  ( default is 1)

    Returns:
        list: a list of key_size, avg_key_generation_time,  avg_encryption_time, avg_decryption_time
          """
# block size 512-bits, and it has a word size of 32-bits
    key_time = []
    enc_time = []
    dec_time = []

    for iteration in range(iterations):
        plain_text_bytes = secrets.token_bytes(key_size)
        key_init_time = time.time()
        key = os.urandom(key_size)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        key_end_time = time.time()
        key_time_diff = key_end_time - key_init_time
        key_time.append(key_time_diff)
        enc_init_time = time.time()
        encryptor = cipher.encryptor()
        ct = encryptor.update(plain_text_bytes) + encryptor.finalize()
        enc_end_time = time.time()
        enc_time_diff = enc_end_time - enc_init_time
        enc_time.append(enc_time_diff)
        dec_init_time = time.time()
        decryptor = cipher.decryptor()
        plain_text = decryptor.update(ct) + decryptor.finalize()

        dec_end_time = time.time()
        dec_time_diff = dec_end_time - dec_init_time
        dec_time.append(dec_time_diff)
    key_avg = avg(key_time)*time_factor
    enc_avg = avg(enc_time)*time_factor
    dec_avg = avg(dec_time)*time_factor
    print('Key Size {size},Key {key_time} Enc {enc_time}, Dec {dec_time}.'
          .format(size=key_size, key_time=key_avg, enc_time=enc_avg, dec_time=dec_avg))
    ls = [key_size, key_avg, enc_avg, dec_avg]
    return ls
    #   print(private_key)
