import time
from cryptography.hazmat.primitives import hashes
import secrets


def hash_time(byte_size, time_factor, algo_name="SHA256", n_iterations=10):
    """Generates key for specified key size and returns with time of generation in provided time factor

    Args:
        byte_size (int): Key size for key generation more than 512  ( default is 512)
        algo_name (str): algo name to use
        time_factor (int) : time factor to multiply values by
        n_iterations (int): no. of iterations for average time per operation  ( default is 10)

    Returns:
        list: byte size and time of computing hash of n_iterations
          """

    algo = hashes.SHA256()
    byte_to_hash = secrets.token_bytes(byte_size)
    if algo_name == "SHA256":
        algo = hashes.SHA256()
    if algo_name == "SHA512":
        algo = hashes.SHA512()
    hash_init_time = time.time()
    for iteration in range(n_iterations):

        digest = hashes.Hash(algo)
        digest.update(byte_to_hash)
        digest.finalize()
    hash_end_time = time.time()
    hash_time_diff = (hash_end_time - hash_init_time)*time_factor
    print('File Size {size},Hash time {hash_time}'
          .format(size=byte_size, hash_time=hash_time_diff))
    ls = [byte_size, hash_time_diff]
    return ls
