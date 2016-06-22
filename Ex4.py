# [(1,  500), (2, 470), (5, 900), (1, 520), (3, 460), (2, 455), (6, 300)]

properties = [(1, 500), (2, 470), (5, 900), (1, 520), (3, 460), (2, 455), (6, 300)]

# print sum([x[1] for x in properties])

dic = {}
# shortcut: shift + f6
for (id, price) in properties:
    if id not in dic:
        dic[id] = [price, 1]
    else:
        # dictionary
        dic[id][0] += price
        dic[id][1] += 1

print dic
"""
d = {}
for key, value in properties:
    if key not in d:
        d[key] = []
    d[key].append(value)

print d.values()
print d.items()
"""