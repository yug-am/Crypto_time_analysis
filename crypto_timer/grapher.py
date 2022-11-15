from crypto_timer.main_timer import *
import matplotlib.pyplot as plt
from tick_handler.tick_handler import *
from data_io.data_io import *


def grapher():
    """calls overall timer and plots graph from the overall_timer values
         Args:
         Returns:
             Nil
               """
    algo_name = "RSA"
    size_key_file_name = algo_name+"_size_key_file"
    key_gen_file_name = algo_name+"_key_gen_size_file"
    enc_file_name = algo_name+"_enc_size_file"
    dec_file_name = algo_name+"_dec_size_file"
    plot_key_gen = False
    read_from_file = True
    handle_overwriting = False
    equi_spaced_axis_deca = True
    key_size_rounds = 4000
    n_iterations = 1
    key_size_from = 800
    plain_text = 'encrypt me hahaha knx'
    time_factor = 1000000
    gp_size = 500
    if not read_from_file:
        plain_text_bytes = str.encode(plain_text)
        size_ls, key_ls, enc_ls, dec_ls = overall_timer(plain_text_bytes, time_factor,
                                                        algo=algo_name, key_size_from=key_size_from,
                                                        key_sizes=key_size_rounds, n_iterations=n_iterations)
        data_dump_write(size_ls, size_key_file_name)
        data_dump_write(key_ls, key_gen_file_name)
        data_dump_write(enc_ls, enc_file_name)
        data_dump_write(dec_ls, dec_file_name)
    else:
        size_ls = data_dump_read(size_key_file_name)
        key_ls = data_dump_read(key_gen_file_name)
        enc_ls = data_dump_read(enc_file_name)
        dec_ls = data_dump_read(dec_file_name)
    size_ls, key_ls, enc_ls, dec_ls = point_club_batch([size_ls, key_ls, enc_ls, dec_ls], gp_size)
    fig, ax = plt.subplots()
    if plot_key_gen:
        ax.plot(size_ls, key_ls, marker='x', label="Key generation")
    ax.plot(size_ls, enc_ls, marker='x', label="Encryption")
    ax.plot(size_ls, dec_ls, marker='x', label="Decryption")
    y_mini, y_maxi = ax.get_ylim()
    offset = 550
    size_ls_offset = [int(i-offset+1) for i in size_ls]
    plt.xticks(size_ls, size_ls_offset)
    if equi_spaced_axis_deca:
        y_coor_ls, y_ticks_ls = equi_spaced_axis_interval(y_maxi)
    else:
        y_coor_ls, y_ticks_ls = ticks_generator(y_maxi, handle_overwriting=handle_overwriting)
    plt.yticks(y_coor_ls, y_ticks_ls)
    plt.margins(x=0)
    plt.legend()
    plt.xlabel("Key size")
    plt.ylabel("Time in microseconds")
    plt.title(algo_name+" operations time")
    plt.show()
