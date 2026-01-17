# 36. XARAJATLAR
x = []

while True:
    c = input()
    if c == "add": x.append(int(input()))
    if c == "sum": print(sum(x))
    if c == "exit": break
