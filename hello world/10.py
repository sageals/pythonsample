names=['john',  'bob', 'mosh' , 'sarah','mary']
print(names[-2])
print(names[2:4])
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
number = [5, 2, 7, 8, 9]
number.insert(0, 10) # other methods are append, remove, pop, index, count, sort, reverse, copy
print(number)
print(50 in number)
dupremove = [2, 2, 3, 4 , 4]
uniques = []
for duplicate in dupremove:
    if duplicate not in uniques:
        uniques.append(duplicate)
print(uniques)

numbern = (1, 2, 3)
print(numbern[0])