import re
pat = r"a.+b$"

def check(s):
    if re.search(pat, s) != None:
        return True
    return False
print(check("lkndflkna ljdflkn ;odflkn b"))
print(check("bak sdlknb"))
print(check("lsdlkgjb"))
print(check("lkndflknalknlknkn"))
