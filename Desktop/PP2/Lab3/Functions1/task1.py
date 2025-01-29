def from_grams_to_ounces(g):
    return g*28.3495231
grams = float(input("Enter grams for the ingredient: "))
ounces = from_grams_to_ounces(grams)
print(ounces)
    
