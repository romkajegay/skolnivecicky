veci = ["Skibidi", "Alfa", "Beta", "Omega", "SigmaBoy", "Rizz"]
x = len(veci)
print(x)
for y in veci:
  print(y)
z = (input("pridej neco:"))
veci.append(z)

veci.pop(1)
print(veci)

veci.sort()
print(veci)

veci.sort(reverse=True)
print(veci)

