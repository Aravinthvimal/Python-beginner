import string

check = input()

if(set(check.lower()) >= set(string.ascii_lowercase)):
    print("panagram")
else:
    print("not a panagram")