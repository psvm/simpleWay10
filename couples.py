# Count the numbers of different couples (ignore spaces) in string


def counte_different_couples(text):
    len_of_string = len(text)
    counter = 0
    for i in range(0, len_of_string // 2):
        if text[i] == text[len_of_string - 1 - i] and text[i] != " ":
            counter = counter + 1
    return counter


print(counte_different_couples("df ghg    dlag fd"))
