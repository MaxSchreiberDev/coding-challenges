counter = int(input())
for _ in range(counter):
    _ = input()
    s, t = map(str, input().split())
    # Dein Ansatz ist gut, aber das hier wäre noch eleganter:
    if sorted(s) == sorted(t):
        print("YES")
    else:
        print("NO")