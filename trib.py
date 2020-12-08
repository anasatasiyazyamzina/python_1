def fib3(n):
    arr = [1, 1, 1]
    for i in range(4, n + 1):
        tmp = sum(arr)
        arr = [arr[1], arr[2], tmp]
    return arr[2]




print("for 2")
print(fib3(8))
