#! / usr / bin / python
# - * - coding: utf-8 - * -

str = "pythoniscool,isn'tit"

indexes = [6, 8, 12, 13, 18]

result = [];

for i in range(len(indexes)):
    prev = indexes[i - 1]
    current = indexes[i]

    if i > 0:
        result.append(str[prev:current]);
    else:
        result.append(str[:current]);

print(result)
