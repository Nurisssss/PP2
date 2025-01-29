def solve(numheads, numlegs):
    for i in range(0, numheads+1):
        if i*2+(numheads-i)*4 == numlegs:
            return (i, numheads-i)
pair = solve(35, 94)
print("Number of chickens: ", end=" ")
print(pair[0])
print("Number of rabbits: ", end=" ")
print(pair[1])
