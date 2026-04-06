t = int(input())
for _ in range(t):
    sticks = input().split()
    if len(set(sticks)) == 1 and len(sticks) == 4: # Ein Set hat nur 1 Element, wenn alle gleich sind
        print("YES")
    else:
        print("NO")