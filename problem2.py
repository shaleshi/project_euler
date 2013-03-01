sum_list=[]
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        if a%2==0:
            if a>4000000:
                break;
            sum_list.append(a)
    print sum(sum_list)
fib(35)