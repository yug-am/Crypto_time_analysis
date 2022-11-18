from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import time
from handy_function.math_function import avg


def dh_key_exchange_timer(time_factor=1000, key_size=512, n_iterations=1):
    """Generates key for specified key size and returns with time of generation in milli seconds

    Args:
        time_factor (int) : time factor to multiply values by (default is 1000)
        key_size (int): Key size for key generation more than 512  ( default is 512)
        n_iterations (int): no. of iterations for average time per operation  ( default is 1)

    Returns:
        list: a list of key_size, avg_key_generation_time,  avg_encryption_time, avg_decryption_time
          """
    key_time = []
    #   print("in DHKE exchange"+str(key_size))
    for iteration in range(n_iterations):

        key_init_time = time.time()

        parameters = dh.generate_parameters(generator=2, key_size=key_size)
        server_private_key = parameters.generate_private_key()
        peer_private_key = parameters.generate_private_key()

        shared_key = server_private_key.exchange(peer_private_key.public_key())

        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
        ).derive(shared_key)
        key_end_time = time.time()
        key_time_diff = key_end_time - key_init_time
        print('Key Size {size},Key {key_time}.'
              .format(size=key_size, key_time=key_time_diff))

        key_time.append(key_time_diff)

    key_avg = avg(key_time)*time_factor
    #   print('Key Size {size},Key {key_time} DHKE'.format(size=key_size, key_time=int(key_avg)))
    ls = [key_size, key_avg]
    return ls
