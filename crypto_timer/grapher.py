from crypto_timer.main_timer import *
import matplotlib.pyplot as plt


def grapher():
    """calls overall timer and plots graph from values

         Args:


         Returns:
             Nil
               """
    key_ls, time_ls = overall_timer()
    #   plt.plot(key_ls, time_ls)
    plt.scatter(key_ls, time_ls, alpha=0.7)
    plt.xlabel("Key size")
    plt.ylabel("Time in milliseconds")
    plt.title("RSA Key generation time")
    plt.show()
