def timeConversion(s):
    a = s[-2:]
    b = int(s[0:2])

    if(a == "AM"):
        if(s[:2] == "12"):
            res = "00" + s[2:-2]
        else:
            res = s[:-2]
    else:
        if(s[:2] == "12"):
            res = s[:-2]
        else:
            res = str(b+12) + s[2:-2]

    return res

if __name__ == '__main__':

    s = input()

    print(timeConversion(s))