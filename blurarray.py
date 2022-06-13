import math
# array = [300,0,0,0,10,0,50,0,0,0,0,0,500,0,20,10,3,5]
array =[[0,0,0]]
blurredarray=[[]]
for i in range(100):
    array.append([0,0,0])
    blurredarray.append([])    
# array = [[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,0]]
# blurredarray=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# mask = [1,1,2,2,4,8,4,2,2,1,1]
mask = [1,2,3,4,5,5,9,5,5,4,3,2,1]
# mask = [1,3,6,9,6,3,1]
# blurredarray=[]

def printrgb(r,g,b,obj):
    print(f"\x1b[38;2;{r};{g};{b}m{obj}\x1b[0m",end="")
# print("\x1b[38;2;0;200;249mTRUECOLOR\x1b[0m\n")
# printrgb(255,0,0,array)
for i in array:
    printrgb(i[0],i[1],i[2],"X")
print()
def _blurarr(arr,msk,out):
    for colorIndex in range(len(arr[0])):
        # print(colorIndex)

        for pixelIndex in range(len(arr)):
            indexWithMaskRadius = pixelIndex-int(len(msk)/2)
            total = 0
            count = 0

            for j in enumerate(mask):
                arrindex = indexWithMaskRadius+j[0]
                if(arrindex<0):
                    # count=2
                    continue
                if(arrindex>len(arr)-1):
                    # count=2
                    continue
                count+=1
                # count=9
                total += j[1]*arr[arrindex][colorIndex]
            if(int(total/count)>255):
                blurredarray[pixelIndex].append(255)
                continue
            blurredarray[pixelIndex].append(int(total/count))


def _avgarr(arrsize,masksize,i):
    indexWithMaskRadius = i-int(masksize/2)
    total = 0
    count = 0
    for j in enumerate(mask):
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
# for i in enumerate(array):
#     _avgarr(18,5,i[0])
for j in range(50):
    print(j)
    array[j] = [255,255,0]
    _blurarr(array,mask,blurredarray)
    for i in array:
        printrgb(i[0],i[1],i[2],"X")
    print()
    array[j] = [0,0,0]