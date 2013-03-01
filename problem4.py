def find_biggest_polindrom():
    list_num=[]
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            if num == int(str(num)[::-1]):
                list_num.append(num)
    return max(list_num)

print find_biggest_polindrom()
