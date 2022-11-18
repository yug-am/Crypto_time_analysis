from key_exchange_timer.key_exchange_timer import *


def dhke_overall_timer(time_factor=1000, key_size_from=512, key_sizes=512, n_iterations=1):
    """Repeatedly calls Diffie hellman operations function for time measure for key sizes

       Args:
        time_factor (int) : time factor to scale time values by (default is 1000)
        key_size_from (int) : Initial starting of byte size ( default is 100)
        key_sizes (int) : no of byte_sizes to measure time ( default is 2000)
        n_iterations (int) : no of iterations to measure time ( default is 1)

       Returns:
           list of key_size_list and key_gen_time_list
             """
    #   print("in DHKE Overall")
    size_ls = []
    key_ls = []
    key_size_to = key_size_from + key_sizes
    for key_size in range(key_size_from, key_size_to + 1):
        key_size, key_time_val = dh_key_exchange_timer(time_factor, key_size, n_iterations=n_iterations)
        size_ls.append(key_size)
        key_ls.append(key_time_val)
        print("key size :{key_size} Key_time :{key_time_val} DHKE"
              .format(key_size=key_size, key_time_val=int(key_time_val)))
    return [size_ls, key_ls]
