string = input("Enter some string")

def polindrom_check (string):
    if string == string[::-1]:
        print("This string is palindrome")
    else:
        print("This string i NOT palindrome")


polindrom_check(string)
