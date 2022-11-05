from cryptography.hazmat.primitives.asymmetric import rsa
import time


def rsa_key_time(key_size=512, iterations=10):
    """Generates key for specified key size and returns with time of generation in milli seconds

    Args:
        key_size (int): Key size for key generation more than 512  ( default is 512)
        iterations (int): no. of iterations for average time per operation  ( default is 10)

    Returns:
        list: a list of RSAPrivateKey object and time of execution
          """
    init_time = time.time()
    private_key = ''
    for iteration in range(iterations):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
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

    print('Key Size {size},Time {time}.'.format(time=program_time, size=key_size))
    ls = [private_key, program_time]
    return ls

    #   print(private_key)
