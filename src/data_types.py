def data_types():
    var_int = 21
    var_str = "School"
    var_float = 1.5
    var_bool = True
    var_list = [1, 2]
    var_dict = {"key": 21}
    var_tuple = (1, 2)
    var_set = {1, 2}

    all_types_of_variables = [var_int, var_str, var_float, var_bool, var_list, var_dict, var_tuple, var_set]

    types_names = [type(var).__name__ for var in all_types_of_variables]
    print(types_names)

if __name__ == '__main__':
    data_types()
