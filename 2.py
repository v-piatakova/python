#! / usr / bin / python
# - * - coding: utf-8 - * -

string = u"А роза азора"
new_string = string.replace(" ", "").replace(",", "").replace(".", "")
new_string = new_string.lower()
print(new_string)


def polindrom_check(new_string):
    if new_string == new_string[::-1]:
        print("This string is palindrome")
    else:
        print("This string is NOT palindrome")



polindrom_check(new_string)
