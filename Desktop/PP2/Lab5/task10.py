import re
def change(s):
    while(True):
        match = re.search(r"[a-z][A-Z]", s)
        if match == None:
            break
        st = s[match.start():match.end()]
        new = s[match.start()]+'_'+s[match.end()-1].lower()
        s = re.sub(st, new, s)
    return s

print(change("thisIsAnExampleOfCamelCaseString"))
