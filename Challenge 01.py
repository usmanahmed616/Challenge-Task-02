
#Challenge 01

print('Input Number you want to retrive from fibonnacci series')
n = int(input())
fiboArray = [0,1]
for i in range(2, n):
        new_num = fiboArray[-1] + fiboArray[-2]
        fiboArray.append(new_num)
print (fiboArray)
print('Fibonnacci Number on index ',n, ' is ',fiboArray[-1])

print ('Enter Number to Check if its Fibonnacci Number or Not')
N = int(input())
N1 = 1
N2 = 1
N3 = 0
count = 1
if (N == 0 or N == 1):
    print("Entered Number is Fibonnaci Number")
else:
    while N3 < N:
        N3 = N1+N2
        N2 = N1
        N1 = N3
        count+=1
        print('N3', N3)
        print('N2',N2)
        print('count',count)
    if N3 == N:
     print("Entered Number is Fibonnaci Number")
    else:
        print("Entered Number is NOT Fibonnaci Number")
        if (N3-N>N-N2):
            print(' The closest index n in the fibonacci sequence is ', count)
        elif (N3-N<N-N2):
            print(' The closest index n in the fibonacci sequence is ', count+1)
        else:
            print('The closest indexes in the fibonacci sequence is', count,' and ', count+1)
            
   
        
        
    
