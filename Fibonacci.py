def fibonnaci_series(length):
    a=0
    b=1
    print(a,b, end=" ")
    for i in range(1,length): 
       c=a+b
       print(c,end = " ")
       a=b
       b=c

length=int(input("enter the length of series you want "))
fibonnaci_series(length)



