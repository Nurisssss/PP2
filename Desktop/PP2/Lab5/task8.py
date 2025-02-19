import re
st = "someStringWithUppercaseLetters"
s = re.split("(?=[A-Z])", st)
print(s)
