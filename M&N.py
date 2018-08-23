import hello as h
import urllib
def main(m,n) -> object:
    h.QuickSort([49,38,65,97,76,13,27,49],0,7)
    for i in n:
        for j in i:
            j-=1
            m[j]=m[j]+1
    for index,value in enumerate(m):
        if value == 1 :
            print(index)
            for v in n:
                if index in v:
                    v="1"
                    print(v)
                    #n[v]="m"+str(index)
                    #print(i)
    print(n)
m = [0,0,0,0,0,0,0,0,0,0]
n = [[1,2], [2,3], [3,4], [1,2], [5], [6]]
main(m,n)
