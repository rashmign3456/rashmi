if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    s = set(arr)
     
    s = sorted(s)
    
    print(s[-2]) 
