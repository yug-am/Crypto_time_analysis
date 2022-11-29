import matplotlib.pyplot as plt
from tick_handler.tick_handler import *
from data_io.data_io import *
from key_exchange_timer.dh_overall_timer import dhke_overall_timer


def dh_key_exchange_grapher():
    """calls overall timer and plots graph from the overall_timer values for Diffie Hellman
         Args:
         Returns:
             Nil
               """
    read_from_file = False
    club_points = True
    n_iterations = 1
    time_factor = 1000
    batch_size = 10
    key_size_from = 512
    key_sizes = 100
    algo_name = "DHKE"
    key_size_file_name = algo_name + "_key_size_file"
    key_file_name = algo_name + "_key_time_file"

    if not read_from_file:
        #   print("in DHKE Grapher")
        key_size_ls, key_ls = dhke_overall_timer(time_factor, key_size_from=key_size_from, key_sizes=key_sizes,
                                                 n_iterations=n_iterations)
        data_dump_write(key_size_ls, key_size_file_name)
        data_dump_write(key_ls, key_file_name)
    else:
        key_size_ls = data_dump_read(key_size_file_name)
        key_ls = data_dump_read(key_file_name)
    if club_points:
        key_size_ls, key_ls = point_club_batch([key_size_ls, key_ls], batch_size)
    plt.plot(key_size_ls, key_ls, label=algo_name, marker="o")
    plt.ylabel("Time in milli seconds for key generation")
    plt.xlabel("Key size")
    plt.title("Diffie Hellman Key Generation")

    plt.legend()
    plt.show()
