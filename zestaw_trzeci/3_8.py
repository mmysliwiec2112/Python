def compare_strings(string1, string2):
    in_both = ""
    each_unique = ""
    print(f'Compared strings: {string1}, {string2}')
    for x in range(0, len(string1)):
        if not string1[x] in each_unique:
            each_unique += string1[x]
    for y in range(0, len(string2)):
        if string2[y] in string1 and not string2[y] in in_both:
            in_both += string2[y]
        else:
            each_unique += string2[y]
    return each_unique, in_both


if __name__ == '__main__':
    print(compare_strings('Lorem', "ipsom"))
    print(compare_strings('aabcheka', 'kechpoer'))
