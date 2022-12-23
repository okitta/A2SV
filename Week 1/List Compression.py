def listCompression(x,y,z,n):
    mainList=[[i,j,k]  for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k != n:
    #                mainList.append([i,j,k])
    return mainList 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(listCompression(x,y,z,n))