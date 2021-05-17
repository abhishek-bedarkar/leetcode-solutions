def jos(n:int,k:int)->int:
    if n == 1:
        return 0
    else:
        return (jos(n-1,k)+k)%n
if __name__ == '__main__':
    print(jos(7,3))
    print(jos(8,5))