l=[]
a=int(input("Введите число "))

def main(a):
    for i in range(0,a):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
    print(l)
main(a)