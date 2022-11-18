from rsa_timer.rsa_timer import *
from aes_timer.aes_timer import *


def overall_timer(plain_text_bytes, time_factor, algo, key_size_from=800, key_sizes=2000, n_iterations=1):
    """Repeatedly calls respective algo operations function for time measure for key sizes

       Args:
        plain_text_bytes (bytes) : bytes data to be encrypted
        time_factor (int) : time factor to scale time values by
        algo (str) : name of algo to plot time
        key_size_from (int) : Initial starting of key size ( default is 800)
        key_sizes (int) : no of key sizes to measure time ( default is 2000)
        n_iterations (int) : no of iterations to measure time ( default is 1)

       Returns:
           list of key_size_list and time_list
             """

    size_ls = []
    key_ls = []
    enc_ls = []
    dec_ls = []
    key_size_to = key_size_from + key_sizes
    if algo == "AES":
        print("AES call in overall timer")
        aes_key_size_ls = [ 128, 192, 256]
        for key_size in aes_key_size_ls:
            res_ls = []
            res_ls = aes_time(plain_text_bytes, time_factor, key_size, iterations=n_iterations)

    if algo == "RSA":
        for key_size in range(key_size_from, key_size_to + 1):
            res_ls = []
            res_ls = rsa_time(plain_text_bytes, time_factor, key_size, iterations=n_iterations)

        key_size = res_ls[0]
        key_time = res_ls[1]
        enc_time = res_ls[2]
        dec_time = res_ls[3]
        size_ls.append(key_size)
        key_ls.append(key_time)
        enc_ls.append(enc_time)
        dec_ls.append(dec_time)

    return [size_ls, key_ls, enc_ls, dec_ls]
