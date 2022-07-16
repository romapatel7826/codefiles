exp = [2200,  2350, 2600, 2130, 2190]

print("print in feb this much extra", exp[1]-exp[0])
print(exp)

print("the total expense of first three month", exp[0]+exp[2])
print(exp)

exp.append(1980)
print(" expense at the end of june: ", exp)

exp[3] = exp[3] - 200
print("expense after 200 return in april:\n", exp)