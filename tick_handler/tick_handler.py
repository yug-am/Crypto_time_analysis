import math


def equi_spaced_axis_interval(axis_max):
    """generates list of coordinates into equispaced in to powers of 10
                      Args:
                          axis_max (int) : max coordinate values of that axis

                      Returns:
                          coordinates_ls (list) : list of  axis values
              """
    axis_max_int = int(axis_max)
    #   print("Axis max {ami} in equispaced ticks gen func".format(ami=axis_max_int))

    max_dig = len(str(axis_max_int))
    #   print("max dig {max_dig} in ticks gen func".format(max_dig=max_dig))
    coor_ls = [0]
    ticks_ls = ["0"]
    spacing_factor = int(axis_max/max_dig)
    #   print("spacing factor {spacing_factor} in ticks gen func".format(spacing_factor=spacing_factor))

    for i in range(1, max_dig+1):
        coor_ls.append(i*spacing_factor)
        val = "10^" + str(i)
        if i <= 2:
            val = str(10**i)
        ticks_ls.append(val)
    #   print("coordinate list")
    #   print(coor_ls)
    #   print("ticks list")
    #   print(ticks_ls)

    return [coor_ls, ticks_ls]


def ticks_generator(axis_max, handle_overwriting=True):
    """generates list of coordinates into numbers in to powers of 10
                      Args:
                          axis_max (int) : max coordinate values of that axis
                          handle_overwriting (bool) :handle overwriting( default is True)
                      Returns:
                          coordinates_ls (list) : list of  axis values
              """
    #   print("Axis max{am} in ticks gen func".format(am=axis_max))
    axis_max_int = int(axis_max)
    #   print("Int of Axis max {am} in ticks gen func".format(am=axis_max_int))
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
    #   print(coor_ls)
    #   print(ticks_ls)
    #   print("Axis max{am} in ticks gen func".format(am=axis_max))
    #   print("Digits in max {dig_max} in ticks gen func".format(dig_max=max_dig))

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


def point_club_batch(list_pt_ls, group_size):
    """generates list of points from average of batch sizes of original point list


            Args:
                list_pt_ls (list) : list of lists of y axis values
                group_size (int) : size of group to club values in

            Returns:
                master_ls (list) : list of coordinates in group of group_size
    """
    master_ls = []
    for ls in list_pt_ls:
        ls = point_club(ls, group_size)
        master_ls.append(ls)
    return master_ls


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
