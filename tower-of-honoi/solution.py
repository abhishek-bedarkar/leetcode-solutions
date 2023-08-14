def tower_of_hanoi(n:int,rod_a,rod_b,rod_c):
    if n == 1 :
        print("moving ",n," from ",rod_a,' ->',rod_c)
    else:
        tower_of_hanoi(n-1,rod_a, rod_c, rod_b)
        print("moving ",n," from ",rod_a,' ->',rod_c)
        tower_of_hanoi(n-1,rod_b,rod_a,rod_c)


if __name__ == '__main__':
    tower_of_hanoi(3,'a','b','c')