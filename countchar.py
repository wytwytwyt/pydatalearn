def countchar(str):
    countlist = []
    str = str.lower()
    for word in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        countlist.append(str.count(word))
    return countlist

if __name__ == '__main__':
    str = input()
    print(countchar(str))