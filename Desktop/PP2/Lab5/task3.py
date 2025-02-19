import re
print(re.findall(r"\b[a-z]+(?:_+[a-z]+)*\b", "ab_c_ef ab_ ab__cd _b_a"))

