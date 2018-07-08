def swap_case(given_string):

    assert type(given_string) == str
    assert 0 < len(given_string) <= 1000

    swapped_string = ""
    for letter in range(0,len(given_string)):
        if given_string[letter].isalpha() == True:
            if given_string[letter].isupper() == True:
                swapped_string += str(given_string[letter].lower())
            else:
                swapped_string += str(given_string[letter].upper())
        else:
            swapped_string += str(given_string[letter])

return swapped_string
