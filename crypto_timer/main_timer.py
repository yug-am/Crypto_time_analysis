from rsa_timer.rsa_timer import *


def overall_timer(plain_text_bytes, time_factor, key_size_from=800, key_sizes=2000, n_iterations=1):
    """Repeatedly calls respective algo operations function for time measure for key sizes

       Args:
        time_factor (int) : time factor to scale time values by
        plain_text_bytes (bytes) : bytes data to be encrypted
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
    for key_size in range(key_size_from, key_size_to+1):
        #   print(sys.getsizeof(plain_text_bytes))
        #   print(plain_text_bytes)
        #   print(key_size)
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
