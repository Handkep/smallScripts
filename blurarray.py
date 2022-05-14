import math
array = [0,0,0,0,10,0,0,0,0]
blurredarray=[]
print(array)
mask = [1,2,4,2,1]
def _avgarr(arrsize,masksize,i):
    i=i-int(masksize/2)
    avg = 0
    count = 0
    for j in enumerate(mask):
        arrindex = i+j[0]
        if(arrindex<0):
            continue
        if(arrindex>arrsize):
            continue
        count+=1
        avg += j[1]*array[arrindex-1]
    blurredarray.append(int(avg/count))




# print(int(5/2))
# print(mask[int(5/2)])
for i in enumerate(array):

    _avgarr(9,5,i[0])
print(blurredarray)