from rsa_timer.timer import *


def overall_timer():
    """Repeatedly calls respective algo operations function for time measure for key sizes

       Args:


       Returns:
           list of key_size_list and time_list
             """

    time_ls = []
    key_ls = []
    key_size_from = 512
    key_size_to = 2048
    n_iterations = 20
    for key_size in range(key_size_from, key_size_to+1):
        res_ls = rsa_key_time(key_size, iterations=n_iterations)
        run_time = res_ls[1]
        time_ls.append(run_time)
        key_ls.append(key_size)
    return [key_ls, time_ls]
