if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list =[]
    temp =[] 
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a + b + c != n:
                    temp.append(a)
                    temp.append(b)
                    temp.append(c)
                    list.append(temp)
                    temp =[]

    print(list)