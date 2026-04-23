def data_types():
    var_int = 21
    var_str = "School"
    var_float = 1.5
    var_bool = True
    var_list = [1, 2]
    var_dict = {"key": 21}
    var_tuple = (1, 2)
    var_set = {1, 2}

    all_variables = [var_int, var_str, var_float, var_bool, var_list, var_dict, var_tuple, var_set]

    type_names = [type(var).__name__ for var in all_variables]
    print(f"[{', '.join(type_names)}]")

if __name__ == '__main__':
    data_types()

