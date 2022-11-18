from crypto_timer.main_timer import *
import matplotlib.pyplot as plt
from tick_handler.tick_handler import *
from data_io.data_io import *
from hash_timer.hash_overall_timer import *


def grapher():
    """calls overall timer and plots graph from the overall_timer values
         Args:
         Returns:
             Nil
               """
    algo_name = "SHA512"
    size_key_file_name = algo_name+"_size_key_file"
    key_gen_file_name = algo_name+"_key_gen_size_file"
    enc_file_name = algo_name+"_enc_size_file"
    dec_file_name = algo_name+"_dec_size_file"
    byte_file_name = algo_name + "_byte_size_file"
    hash_file_name = algo_name + "_hash_size_file"
    plot_key_gen = True
    read_from_file = False
    handle_axis_overwriting = False
    equi_spaced_axis_deca = True
    key_size_rounds = 4000
    n_iterations = 100
    key_size_from = 800
    plain_text = 'encrypt me hahaha knx'
    time_factor = 1000000
    batch_size = 500
    size_ls = []
    key_ls = []
    enc_ls = []
    dec_ls = []
    byte_size_ls = []
    hash_ls = []
    hash_algos = ["SHA256", "SHA512", ]
    hash_byte_size_from = 4
    hash_byte_sizes = 10000
    if not read_from_file:
        if algo_name in hash_algos:
            print("Hash flag")
            byte_size_ls, hash_ls = hash_overall_timer(time_factor, algo_name, byte_size_from=hash_byte_size_from,
                                                       byte_sizes=hash_byte_sizes, n_iterations=n_iterations)
            data_dump_write(byte_size_ls, byte_file_name)
            data_dump_write(hash_ls, hash_file_name)

        else:
            plain_text_bytes = str.encode(plain_text)
            size_ls, key_ls, enc_ls, dec_ls = overall_timer(plain_text_bytes, time_factor,
                                                            algo=algo_name, key_size_from=key_size_from,
                                                            key_sizes=key_size_rounds, n_iterations=n_iterations)

            data_dump_write(size_ls, size_key_file_name)
            data_dump_write(key_ls, key_gen_file_name)
            data_dump_write(enc_ls, enc_file_name)
            data_dump_write(dec_ls, dec_file_name)
    else:
        if algo_name in hash_algos:
            byte_size_ls = data_dump_read(byte_file_name)
            hash_ls = data_dump_read(hash_file_name)
        else:
            size_ls = data_dump_read(size_key_file_name)
            key_ls = data_dump_read(key_gen_file_name)
            enc_ls = data_dump_read(enc_file_name)
            dec_ls = data_dump_read(dec_file_name)
    if algo_name == "RSA":
        size_ls, key_ls, enc_ls, dec_ls = point_club_batch([size_ls, key_ls, enc_ls, dec_ls], batch_size)
    fig, ax = plt.subplots()
    if algo_name in hash_algos:
        # from one because first result is abnormally high
        # 100 batch sizes to avoid crowding
        # scatter plot to avoid noises in line plot
        byte_size_ls_clubbed, hash_ls_clubbed = point_club_batch([byte_size_ls, hash_ls], batch_size)
        ax.plot(byte_size_ls_clubbed, hash_ls_clubbed, label="Hash computation", marker="o")
        plt.xlabel("Input size")
        plt.ylabel("Time in micro seconds for "+str(n_iterations)+" operations")
        plt.title(algo_name + " Hash computation time")
    else:
        plt.title(algo_name + " operations time")
        plt.ylabel("Time in microseconds")
        if plot_key_gen:
            ax.plot(size_ls, key_ls, marker='x', label="Key generation")
        ax.plot(size_ls, enc_ls, marker='x', label="Encryption")
        ax.plot(size_ls, dec_ls, marker='x', label="Decryption")
        if algo_name == "RSA":

            y_mini, y_maxi = ax.get_ylim()
            offset = 550
            size_ls_offset = [int(i-offset+1) for i in size_ls]
            plt.xticks(size_ls, size_ls_offset)
            if equi_spaced_axis_deca:
                y_coor_ls, y_ticks_ls = equi_spaced_axis_interval(y_maxi)
            else:
                y_coor_ls, y_ticks_ls = ticks_generator(y_maxi, handle_overwriting=handle_axis_overwriting)
            plt.yticks(y_coor_ls, y_ticks_ls)
            plt.xlabel("Key size")
    if algo_name not in hash_algos:
        plt.margins(x=0)
    plt.legend()
    plt.show()
