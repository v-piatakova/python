def foo(array):
    len(array)
    t = 1
    result_arr = [1]
    for i in range(1, len(array)):
        t *= array[i - 1]
        result_arr.append(t)
    t = 1
    for i in range(len(array) - 2, -1, -1):
        t *= array[i + 1]
        result_arr[i] *= t
    print(result_arr)


foo([1, 2, 3, 4, 5])


