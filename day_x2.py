a, b = map(int, input().split())
if a == 1:
    k = 0
if a == 2:
    k = 31
if a == 3:
    k = 59
if a == 4:
    k = 90
if a == 5:
    k = 120
if a == 6:
    k = 151
if a == 7:
    k = 181
if a == 8:
    k = 212
if a == 9:
    k = 243
if a == 10:
    k = 273
if a == 11:
    k = 304
if a == 12:
    k = 334
if b > 31 or a < 1 or a > 12 or b < 1:
    print("-1")
else:
    c = k + b
z = 365 - c

