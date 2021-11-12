def split(input_str):
    out_list = []
    word = ""
    delimiter = " "
    for c in input_str:
        if c not in delimiter:
            word += c
        else:
            out_list.append(word)
            word = ""
    out_list.append(word)
    return out_list


print(split("1 2 3  4"))
