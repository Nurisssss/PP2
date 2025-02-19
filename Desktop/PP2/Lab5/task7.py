import re
st = "snake_case_string"
def change(s):
    while(True):
        match = re.search("_[a-z]", s)
        if match == None:
            break
        st = s[match.start():match.end()]
        s = re.sub(st, st[1].upper(), s)
    return s
print(change(st))
