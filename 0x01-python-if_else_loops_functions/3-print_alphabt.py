#!/usr/bin/python3
for i in range(97, 122):
    if i not in [ord("q"), ord("e")]:
        print("{:c}".format(i), end="")
