counter = input()

content = []

for _ in range(int(counter)):
    a = []
    b = input()
    c = ""
    for i in b:
        if not i == " ":
            c = c + i
        else:
            a.append(c)
            c = ""
    a.append(c)
    content.append(a)

for i in range(len(content)):
    a = content[i]
    if len(a) == 4 and a[1] == a[2] == a[3] == a[0]:
        print("YES")
    else:
        print("NO")