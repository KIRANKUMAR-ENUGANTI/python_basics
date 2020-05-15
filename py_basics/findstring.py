def c_substring(string, sub_string):
    if (string.isascii() and len(string) >= 1 and len(string) <= 200):
        c = 0
        for i in range(len(string)):
            if (string[i:i + len(sub_string)] == sub_string[0:len(sub_string)]): c += 1


    return c


def count_substring(string, sub_string):
    if (string.isascii() and len(string) >= 1 and len(string) <= 200):
        c = 0
        for i in range(len(string)):
                j = i + len(sub_string)
                if (string[i:j+1].count(sub_string)): c += 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)