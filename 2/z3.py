

dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

ks = set()
vs = set()
for key, value in dct.items():
    ks.add(key)
    vs.add(value)

common = ks | vs
print(ks)
print(vs)
print(common)