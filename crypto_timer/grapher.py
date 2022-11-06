from crypto_timer.main_timer import *
import matplotlib.pyplot as plt


def grapher():
    """calls overall timer and plots graph from values

         Args:


         Returns:
             Nil
               """
    key_size_rounds = 200
    n_iterations = 10
    size_ls, key_ls, enc_ls, dec_ls = overall_timer(key_sizes=key_size_rounds,n_iterations=n_iterations)
    #   [size_ls, key_ls, enc_ls, dec_ls]
    #   plt.plot(key_ls, time_ls)
    plt.scatter(size_ls, key_ls, alpha=0.7)
    plt.plot(size_ls, key_ls, label="Key gen time")
    plt.plot(size_ls, enc_ls, label="enc time")
    plt.plot(size_ls, dec_ls, label="dec time")
    x_axis_tick_interval = 100
    plt.xticks(size_ls[::x_axis_tick_interval])
    plt.legend()
    plt.xlabel("Key size")
    plt.ylabel("Time in milliseconds")
    plt.title("RSA Key generation time")
    plt.show()
