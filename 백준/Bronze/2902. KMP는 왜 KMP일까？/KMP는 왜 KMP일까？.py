name = input()
def shortname(name):
    result = ''
    sname = []
    for char in name:
        if char.isupper():
            sname.append(char)
            result = ''.join(sname)
    return result


print(shortname(name))