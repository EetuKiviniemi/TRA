import random
import time

def randperm(n,A):
    for i in range(0,n):
        A[i] = i +1
    for i in range(0,n-1):
        x = random.randint(0,n-1)
        A[i], A[x] = A[x], A[i]
    return A

    
def permtest(A):
    if A[0]%4 == A[1]%4 ==  A[2]%4 == A[3]%4 == A[5]%4:
        return True
    else:
        return False
    

def main(n,A):
    start_time = time.time()
    yes = 0
    no = 0
    while yes < 500:
        if permtest(randperm(n,A)):
            yes += 1
        else:
            no += 1
    print("Yescount = ", yes)
    print("Nocount = ", no)
    print("Suhde = ",yes/(yes+no))
    print("Aikaa kului: ", time.time() - start_time, "s")
    return
    
        
A6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]       


main(52,A6)