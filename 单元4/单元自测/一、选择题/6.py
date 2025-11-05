p = "abcdcba"
if p[1] == p[-1]:
    print(p[1])
else:
    if p[2] != p[-2]:
        print(p[2])
    else:
        print(p[-2])
