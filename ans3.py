from collections import defaultdict
def Combination(n,k):  
    C=defaultdict(int)  
    for row in range(n+1):  
        C[row,0]=1  
        for col in range(1,k+1):  
            if col <= row:  
                C[row,col]=C[row-1,col-1]+C[row-1,col]  
    return C[n,k]  

def main():
    n = 990
    r = 33
    print(Combination(n,r))

if __name__ == '__main__':
    main()