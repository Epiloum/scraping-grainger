def merge_arrays_to_dict_list(keys1, keys2, array1, array2):
    min_length = min(len(array1), len(array2))
    return [{keys1: array1[i], keys2: array2[i]} for i in range(min_length)]