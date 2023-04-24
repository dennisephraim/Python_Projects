blanks = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ",]
print(blanks)
blanks[2] = "a"
blanks[5] = "r"
s = ""
for a in blanks:    
    s = s + a[0] + " "
print(s)