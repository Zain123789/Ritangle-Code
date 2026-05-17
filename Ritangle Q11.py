import itertools

friendly = []
final_list = []
total = 0

num_list = [i for i in range(1, 101)]

for c in itertools.product(num_list, repeat=4):
    x1 = c[0]
    y1 = c[1]
    x2 = c[2]
    y2 = c[3]

    if 2*(x1+y1) == x2*y2 and 2*(x2+y2) == x1*y1:
        friendly.append(x1)
        friendly.append(y1)
        friendly.append(x2)
        friendly.append(y2)


for num in friendly:
    if num not in final_list:
        final_list.append(num)

for num in final_list:
    total += num

final_answer = (total * 6) + 129

print(total)
print(final_answer)
