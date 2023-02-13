def cards(a, b):
    ab = a+b

    aa = a
    bb = b

    aabb = []
    count = 1

    while aabb != ab:
        aabb = []
        for i in range(len(a)):
            aabb.append(aa[i])
            aabb.append(bb[i])
        
        aa = aabb[0:len(aabb)//2]
        bb = aabb[len(aabb)//2:len(aabb)]
        count += 1

    return len(a), count

# prepared lines below generates 100 shuffle variants starting from 2 (a1, b1) cards

y = 100
with open('result.txt', 'a') as w:
    for i in range(2, y+1):
        a = [f'a{j}' for j in range(1, i)]
        b = [f'b{j}' for j in range(1, i)]
        f, g = cards(a, b)
        final = [f'n = {f}', f'Shuffle No. = {g}']
        result = '\n'.join(str(i) for i in final)
        w.write('----------------\n')
        w.write(result)
        w.write('\n----------------')
        w.write('\n\n')

# creating lines to find number of cards needed to get 8 shuffles

with open('8_shuffles.txt', 'w') as f:
    i = 2
    shuffle = 0
    while shuffle != 8:
        a = [f'a{j}' for j in range(1, i)]
        b = [f'b{j}' for j in range(1, i)]
        x, y = cards(a, b)
        final = [f'n = {x}', f'Shuffle No. = {y}']
        i += 1
        shuffle = y
    else:
        result = '\n'.join(str(i) for i in final)
        f.write('----------------\n')
        f.write(result)
        f.write('\n----------------')