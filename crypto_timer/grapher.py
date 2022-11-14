from crypto_timer.main_timer import *
import matplotlib.pyplot as plt
import pickle
import math


def ticks_generator(axis_max, handle_overwriting=True):
    """generates list of coordinates into numbers in to powers of 10
                      Args:
                          axis_max (int) : max coordinate values of that axis
                          handle_overwriting (bool) :handle overwriting( default is True)
                      Returns:
                          coordinates_ls (list) : list of  axis values
              """
    #   min_ele = min(ls)
    #   max_ele = max(ls)
    #   min_dig = (len(str(math.floor(min_ele))))
    #   max_dig = (len(str(math.floor(max_ele))))

    print("Axis max{am} in ticks gen func".format(am=axis_max))
    axis_max_int = int(axis_max)
    print("Int of Axis max {am} in ticks gen func".format(am=axis_max_int))
    max_dig = len(str(axis_max_int))
    coor_ls = []
    ticks_ls = []
    init_dig = 0
    if handle_overwriting:
        init_dig = max_dig-3
    for i in range(init_dig, max_dig):
        coor_ls.append(10**i)
        ticks_ls.append("10^"+str(i))
    coor_ls[0] = 0
    ticks_ls[0] = "10^0"
    if axis_max % 10:
        coor_ls.append(axis_max)
        ticks_ls.append("10^"+str(max_dig))
    print(coor_ls)
    print(ticks_ls)
    #   print("Axis max{am} in ticks gen func".format(am=axis_max))
    print("Digits in max {dig_max} in ticks gen func".format(dig_max=max_dig))

    return [coor_ls, ticks_ls]


def generate_coordinates_from_log(ls):
    """generates list of coordinates into numbers from list


                  Args:
                      ls (list) : list of values

                  Returns:
                      coordinates_ls (list) : list of log scaled
          """
    new_ls = []
    for ele in ls:
        new_ls.append(math.ceil(ele))
    return new_ls


def log_scale(pt_ls):
    """generates list of coordinates in 10 raise to power for given low and high values


              Args:
                  pt_ls (list) : list of y axis values

              Returns:
                  coordinates_ls (list) : list of log scaled
      """
    new_ls = []
    for ele in pt_ls:
        new_ls.append(math.log(ele))
    return new_ls


def point_club(pt_ls, group_size):
    """generates list of points from average of batch sizes of original point list


            Args:
                pt_ls (list) : list of y axis values
                group_size (int) : size of group to club values in

            Returns:
                coordinates_ls (list) : list of coordinates in group of group_size
    """
    new_ls = []
    curr_ptr = 0
    n_iter = len(pt_ls)//group_size
    for i in range(n_iter):
        t_ls = pt_ls[curr_ptr: curr_ptr+group_size:]
        avg_ls = sum(t_ls)/len(t_ls)
        new_ls.append(avg_ls)
        curr_ptr += group_size
    return new_ls


def generate_coordinates(low, high):
    """generates list of coordinates in 10 raise to power for given low and high values


             Args:
                 low (int) : starting value of axis
                 high (int) : ending value of axis


             Returns:
                 coordinates_ls (list) : list of coordinates in int

                   """
    low_y = len(str(low))
    high_y = len(str(high))

    coordinates_ls = [0]
    coordinates_ls_temp = [int('1' + '0' * i) for i in range(low_y, high_y + 1)]
    coordinates_ls = coordinates_ls + coordinates_ls_temp
    #   print(coordinates_ls)
    return coordinates_ls


def generate_labels(low, high):
    """generates list of labels in 10 raise to power for given low and high values


             Args:
                 low (int) : starting value of axis
                 high (int) : ending value of axis


             Returns:
                 coordinates_ls (list) : list of labels in string

                   """
    low_y = len(str(low))
    high_y = len(str(high))
    ticks_ls = ['10^0']
    ticks_ls_temp = ["10^" + str(i) for i in range(low_y, high_y + 1)]
    ticks_ls = ticks_ls + ticks_ls_temp
    #   print(ticks_ls)
    return ticks_ls


def grapher():
    """calls overall timer and plots graph from values

         Args:


         Returns:
             Nil
               """
    size_key_file_name = "size_key_file"
    key_gen_file_name = "key_gen_size_file"
    enc_file_name = "enc_size_file"
    dec_file_name = "dec_size_file"
    plot_key_gen = False
    read_from_file = True
    #   x_axis_tick_interval = 500
    if not read_from_file:
        key_size_rounds = 2000
        n_iterations = 1
        key_size_from = 800
        plain_text = 'encrypt me hahaha knx '
        time_factor = 1000000
        plain_text_bytes = str.encode(plain_text)
        size_ls, key_ls, enc_ls, dec_ls = overall_timer(plain_text_bytes, time_factor, key_size_from=key_size_from,
                                                        key_sizes=key_size_rounds, n_iterations=n_iterations)
        with open(size_key_file_name, "wb") as fp:  # Pickling
            pickle.dump(size_ls, fp)
        with open(key_gen_file_name, "wb") as fp:  # Pickling
            pickle.dump(key_ls, fp)
        with open(enc_file_name, "wb") as fp:  # Pickling
            pickle.dump(enc_ls, fp)
        with open(dec_file_name, "wb") as fp:  # Pickling
            pickle.dump(dec_ls, fp)
    else:
        with open(size_key_file_name, "rb") as fp:  # Unpickling
            size_ls = pickle.load(fp)
        with open(key_gen_file_name, "rb") as fp:  # Unpickling
            key_ls = pickle.load(fp)
        with open(enc_file_name, "rb") as fp:  # Unpickling
            enc_ls = pickle.load(fp)
        with open(dec_file_name, "rb") as fp:  # Unpickling
            dec_ls = pickle.load(fp)
        #   print("Len")
        #   print(len(enc_ls))
    #   size_ls = size_ls[1:]
    #   key_ls = key_ls[1:]
    #   enc_ls = enc_ls[1:]
    #   dec_ls = dec_ls[1:]

    #   key_ls, enc_ls, dec_ls
    #   [size_ls, key_ls, enc_ls, dec_ls]
    #   plt.plot(key_ls, time_ls)
    gp_size = 500
    size_ls = point_club(size_ls, gp_size)
    key_ls = point_club(key_ls, gp_size)
    enc_ls = point_club(enc_ls, gp_size)
    dec_ls = point_club(dec_ls, gp_size)
    #   key_ls_scaled = log_scale(key_ls)
    fig, ax = plt.subplots()
    if plot_key_gen:
        ax.plot(size_ls, key_ls, marker='x', label="Key gen time")
    ax.plot(size_ls, enc_ls, marker='x', label="enc time")
    ax.plot(size_ls, dec_ls, marker='x', label="dec time")
    #   plt.xlim(500, 2500)
    y_mini, y_maxi = ax.get_ylim()
    print('Y axis,Min {y_min} Max {y_max}.'
          .format(y_min=y_mini, y_max=y_maxi))

    #   key_ls = log_scale(key_ls)

    #   x_labels = size_ls
    #   x_labels[0] = '500'
    offset = 550
    size_ls_offset = [int(i-offset+1) for i in size_ls]
    plt.xticks(size_ls, size_ls_offset)
    y_coor_ls, y_ticks_ls = ticks_generator(y_maxi)

    plt.yticks(y_coor_ls, y_ticks_ls)
    #   plt.yticks([0, 10, 100, 1000,10000], ['10^0', '10^1', '10^2', '10^3','10^4'])
    #   min_y = int(min(min(key_ls), min(enc_ls), min(dec_ls)))
    #   max_y = int(max(max(key_ls), max(enc_ls), max(dec_ls)))
    #key_ls_label = generate_coordinates_from_log(key_ls)

    #   y_coordinates = generate_coordinates_from_log(size_ls)
    #   y_coordinates = generate_coordinates(min_y, max_y)
    #   y_labels = generate_labels(min_y, max_y)
    #   plt.yticks(key_ls, key_ls_label)

    #   plt.yticks(y_ls)
    plt.margins(x=0)
    plt.legend()
    plt.xlabel("Key size")
    plt.ylabel("Time in microseconds")
    plt.title("RSA Key generation time")
    plt.show()
