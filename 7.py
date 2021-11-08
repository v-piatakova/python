def foo(array):
    t = 1
    pref = [1]
    for i in range(1, len(array)):
        t *= array[i - 1]
        pref.append(t)
    print(pref)
    t = 1
    suf = [1]
    for i in range(len(array) - 2, -1, -1):
        t *= array[i + 1]
        suf.insert(0, t)
    print(suf)
    result = []
    for i in range(len(array)):
        result.append(pref[i] * suf[i])
    print(result)


foo([1, 2, 3, 4, 5])
