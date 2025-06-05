def combinasi(n,k):  
    return 1 if k == 0 or n == k else combinasi(n - 1,k - 1) + combinasi(n - 1,k)

print(combinasi(6,3))
print(combinasi(5,2))
print(combinasi(10,8))