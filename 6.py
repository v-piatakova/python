string = input("Enter some string")
def get_shortest_word(string):

    split_str = string.split(" ")
    print(split_str)

    your_string = min(split_str, key=len)
    print(your_string)

get_shortest_word(string)
