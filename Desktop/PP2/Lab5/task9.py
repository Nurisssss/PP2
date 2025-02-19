import re
def change(s):
    while(True):
        match = re.search(r"[A-Za-z][A-Z]", s)
        if match == None:
            break
        st = s[match.start():match.end()]
        new = st[0] + ' ' + st[1]
        s = re.sub(st, new, s)
    return s
print(change("ThisIsAnExample Iguess thisShouldWork"))
