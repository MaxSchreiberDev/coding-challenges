counter = int(input())
for _ in range(counter):
    input() #brauch die zahl garrnicht haha
    a = input().split()
    l = []
    for i in a[0]:
        l.append(i)
    for i in a[1]:
        if l.__contains__(i):
            l.remove(i)
    if l == []:
        print("YES")
    else:
        print("NO")
        