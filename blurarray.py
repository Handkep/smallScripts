import math
array = [300,0,0,0,10,0,50,0,0]
blurredarray=[]
print(array)
mask = [1,2,4,2,1]
def _avgarr(arrsize,masksize,i):
    indexWithMaskRadius = i-int(masksize/2)
    total = 0
    count = 0
    for j in enumerate(mask):
        # print(j)
        arrindex = indexWithMaskRadius+j[0]
        if(arrindex<0):
            continue
        if(arrindex>arrsize-1):
            continue
        count+=1
        total += j[1]*array[arrindex]
    blurredarray.append(int(total/count))




# print(int(5/2))
# print(mask[int(5/2)])
for i in enumerate(array):
    _avgarr(9,5,i[0])
print(blurredarray)