
string = """Hello, i 'think', that you "know" what to do"""
print(string)

def change(string):


    def split(s):
        return [char for char in s]


    split_string = split(string)
    print(split_string)


    for i in range(len(split_string)):
        element = split_string[i]
        if(element == "\'"):
            split_string[i] = "\""
            if(element == "\""):
                split_string[i] = "\'"

    new_sting = ('').join(split_string)
    print(new_sting)

change(string)

