# kvIn = [
#     [0,1,2,3],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]
# ]
kvIn = [
    [1,0,1,1],
    [0,1,1,0],
    [1,1,1,1],
    [1,1,1,1]
]
print(kvIn)
buf = kvIn[2] 
kvIn[2] = kvIn[3]
kvIn[3] = buf
for i in kvIn:
    print(i)
for i in enumerate(kvIn):
    buf = i[1][2]
    kvIn[i[0]][2] = kvIn[i[0]][3]
    kvIn[i[0]][3] = buf
print()
for i in kvIn:
    print(i)