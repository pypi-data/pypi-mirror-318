import time


def measure_(func, *args, **kwargs):
    """用于测量某个函数的执行时间"""
    return_result = dict()
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = "{:.2f}".format(end_time - start_time)
    # print(f"Function '{func.__name__}' executed in {elapsed_time} seconds")
    return_result['result'] = result
    return_result['elapsed_time'] = elapsed_time
    return return_result
