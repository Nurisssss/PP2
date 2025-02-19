import re
def change(s):
    s = re.sub(r" ", ":", s)
    s = re.sub(r",", ":", s)
    s = re.sub(r"[.]", ":", s)
    return s
st = "abf.lknf,lkndf f,."
new = change(st)
print(new)

