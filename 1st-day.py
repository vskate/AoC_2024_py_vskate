f = open("1day-data.txt")

def distances(ls1, ls2):
    add = []

    for i in range(len(ls1)):
        add.append(abs(ls1[i]-ls2[i]))

    sum = 0
    for j in add:
        sum += j
    
    return sum

def create_final_lists(f):
    
    left = []
    right = []

    for l in f:
        first, second = l.split()
        left.append(int(first))
        right.append(int(second))

    left.sort()
    right.sort()
    
    return left, right
     
lists = create_final_lists(f)

print(lists)

print(distances(lists[0], lists[1]))