arr = [[1 ,1,1, 0, 0, 0],
       [0 ,1 ,0 ,0 ,0 ,0],
       [1 ,1, 1, 0, 0, 0],
       [0 ,0 ,2 ,4 ,4 ,0],
       [0 ,0, 0, 2, 0, 0],
       [0 ,0 ,1 ,2 ,4 ,0]]

maxNum = -9 * 7 #Hourglass got 7 elements and in the range of -9 to +9
for row in range(4):
    for coloumn in range(4):
        a = arr[row][coloumn]
        b = arr[row][coloumn+1]
        c = arr[row][coloumn+2]
        d = arr[row+1][coloumn+1]
        e = arr[row+2][coloumn]
        f = arr[row+2][coloumn+1]
        g = arr [row+2][coloumn+2]

        total = a+b+c+d+e+f+g
        maxNum = max(total,maxNum)

print(maxNum)

