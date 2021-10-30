string = "Hello, i \'think\', that you \"know\" what to do"

def change(string):

    print(string)
    print("String with changes")
    string = str(string).replace('\'', '\"')
    print(string)

    change(string)
