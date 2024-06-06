nterm=int(input("enter nterm"))
fibonacci=[0,1]
for i in range(2, nterm):
    nterm=fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(nterm)
for term in fibonacci:
    print(term)
    