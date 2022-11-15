import pickle

dump_directory = "./data_dump/"


def data_dump_read(file_name):
    """
        Args:
            file_name(str) :filename to write data into

        Returns:
            data_list(list) : data list read from file_name file

    """
    with open(dump_directory+file_name, "rb") as fp:
        data_list = pickle.load(fp)
    return data_list


def data_dump_write(data_list, file_name):
    """
        Args:
            data_list(list) : data list to enter data into
            file_name(str) :filename to write data into


        Returns:

    """
    with open(dump_directory+file_name, "wb") as fp:
        pickle.dump(data_list, fp)
