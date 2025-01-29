def from_F_to_C(temp):
    return (5/9)*(temp-32)
Ftemp = float(input("Enter a Fahrenheit temperature: "))
print(from_F_to_C(Ftemp))
