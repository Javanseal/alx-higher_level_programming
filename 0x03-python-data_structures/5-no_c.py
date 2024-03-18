#!/usr/bin/python3
#!/usr/bin/python3



def no_c(my_string):
    """Removes all characters c and C from a string

    Args:
        my_list: a string

    Returns:
        the new string
    """

     
    dict = {ord(char): None for char in "cC"}

    new_string = my_string.translate(dict)
    return new_string
