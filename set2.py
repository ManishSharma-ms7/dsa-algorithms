def gridTraveller(m, n):
    if m*n == 0: return 0
    if m*n == 1: return 1
    if m*n == 2: return 1
    a = gridTraveller(m-1, n)
    b = gridTraveller(m, n-1)
    return a+b

print(gridTraveller(2,2))
print(gridTraveller(2,3))
print(gridTraveller(3,3))
print(gridTraveller(10,1))
