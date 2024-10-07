def apply_all_func(int_list, *functions):
    results = {}
    for i in int_list:
        if isinstance(i, int) or isinstance(i, float):
            for func in functions:
                res_f = func(int_list)
                results.update({func.__name__:res_f})
    return results





print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# Вывод на консоль:
#
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}