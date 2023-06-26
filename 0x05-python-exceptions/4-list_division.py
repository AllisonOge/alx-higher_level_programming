#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    length = []
    for i in range(list_length):
        try:
            _ = iter(my_list_1[i])
            _ = iter(my_list_2[i])
            print("wrong type")
        except TypeError:
            try:
                result = int(my_list_1[i]) / int(my_list_2[i])
                length.append(result)
            except ValueError:
                print("wrong type")
                length.append(0)
            except ZeroDivisionError:
                print("division by 0")
                length.append(0)
            except IndexError:
                print("out of range")
                length.append(0)
        except IndexError:
            print("out of range")
            length.append(0)
        finally:
            continue
    return length
