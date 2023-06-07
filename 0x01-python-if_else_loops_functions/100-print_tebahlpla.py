#!/usr/bin/python3
alphabets = ""
for i, c in enumerate(range(65, 91)):
    if (i - 1) % 2 == 0:
        alphabets += "{:c}".format(c + 32)
    else:
        alphabets += "{:c}".format(c)
print(alphabets[::-1], end="")
