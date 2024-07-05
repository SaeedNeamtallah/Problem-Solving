n, h = map(int, input().split())
h_persons = list(map(int, input().split()))
w=0
for x in (h_persons):
    if x <= h:
        w += 1
    else:
        w += 2

print(w)