if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max=-101
    for i in arr:
        if i>max:
            max=i
    max2=-101
    for i in  arr:
        if i>max2 and i!=max:
            max2=i
    print max2 
