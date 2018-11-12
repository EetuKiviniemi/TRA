'''Syöte: Taulukko A[0,1,..,n-1], n >= 1, taulukon alkiot ovat kasvavassa
järjestyksessä A[0] <= A[1] <= ... <= A[n-1]. Luku x jota haetaan taulukosta.
Tulostus: Alkion x indeksi taulukossa tai arvo -1, jos x ei esiinny
taulukossa.'''

#virhe ainakin se, että jos lukua ei löytynyt taulukosta, niin while-loop ei koskaan päättynyt
#korjattu laittamalla alkuun ehto tarkastamaan asia
import math
def haku(A,x):
    low=0
    up=len(A)-1
    if not x in A:
        return -1
    print("up = ", up)
    while low <= up:
        r = math.floor((low + up)/2)
        print("r = ", r)
        print("A[r] = ", A[r])
        print("x = ", x)
        if A[r] < x:
            low = r
            print("low = ", low)
        elif A[r] > x:
            up = r
            print("up = ", up)
        else:
            return r
    return -1
        
A=[1,2,3,4,5,6,7,8,9,10,11,12]
B=[2,4,6,8,9,9,10,12]

