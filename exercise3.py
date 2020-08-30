a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [];
for x in range(len(a)):
    if (a[x] < 5):
        b.append(a[x]);

print(b);