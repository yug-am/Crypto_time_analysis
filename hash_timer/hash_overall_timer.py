from hash_timer.hash_timer import *


def hash_overall_timer(time_factor, algo_name, byte_size_from=4, byte_sizes=200, n_iterations=100):
    """Repeatedly calls respective algo operations function for time measure for key sizes

       Args:
        time_factor (int) : time factor to scale time values by
        algo_name (str) : name of algo to plot time
        byte_size_from (int) : Initial starting of byte size ( default is 4)
        byte_sizes (int) : no of byte_sizes to measure time ( default is 200)
        n_iterations (int) : no of iterations to measure time ( default is 1)

       Returns:
           list of key_size_list and hash_time_list
             """
    print("Hashes function call")
    size_ls = []
    hash_ls = []
    byte_size_to = byte_size_from + byte_sizes
    for byte_size in range(byte_size_from, byte_size_to + 1):
        byte_size, hash_time_val = hash_time(byte_size,
                                             time_factor, algo_name=algo_name, n_iterations=n_iterations)
        size_ls.append(byte_size)
        hash_ls.append(hash_time_val)
    return [size_ls, hash_ls]
