u = [10, 20]
v = [10, 20]

while True:
    new_u = u[-1] / u[-2]
    u.append(new_u)
    new_v = (v[-1] + 1) / v[-2]
    v.append(new_v)
    if u[-1] == v[-1] and u[-2] == v[-2]:
        break

print(len(u)-1)
