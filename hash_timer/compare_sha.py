import matplotlib.pyplot as plt
from tick_handler.tick_handler import *
from data_io.data_io import *
from hash_timer.hash_overall_timer import *


def compare_sha_grapher():
    """calls overall timer and plots graph from the overall_timer values
         Args:
         Returns:
             Nil
               """
    read_from_file = True
    n_iterations = 100
    time_factor = 1000000
    batch_size = 500
    hash_algos = ["SHA224", "SHA256", "SHA384", "SHA512"]
    hash_byte_size_from = 4
    hash_byte_sizes = 10000
    byte_size_ls = []
    hash_ls = []
    for algo_name in hash_algos:
        byte_file_name = algo_name + "_byte_size_file"
        hash_file_name = algo_name + "_hash_size_file"

        if not read_from_file:
            byte_size_ls, hash_ls = hash_overall_timer(time_factor, algo_name, byte_size_from=hash_byte_size_from,
                                                       byte_sizes=hash_byte_sizes, n_iterations=n_iterations)
            data_dump_write(byte_size_ls, byte_file_name)
            data_dump_write(hash_ls, hash_file_name)

        else:

            byte_size_ls = data_dump_read(byte_file_name)
            hash_ls = data_dump_read(hash_file_name)
        byte_size_ls_clubbed, hash_ls_clubbed = point_club_batch([byte_size_ls, hash_ls], batch_size)
        plt.plot(byte_size_ls_clubbed, hash_ls_clubbed, label=algo_name, marker="o")

        plt.ylabel("Time in micro seconds for "+str(n_iterations)+" operations")
        plt.xlabel("Input size")
        plt.title("Hash computation time")

    plt.legend()
    plt.show()
