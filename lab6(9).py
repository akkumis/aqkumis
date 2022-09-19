N = int(input("N: "))
array = []
min_ = float('inf')
for i in range(N):
    num = float(input(f"array[{i}] : "))
    array.append(num)
    if abs(num) < abs(min_):
        min_ = num
print(f"min module: {min_}")
print("Array in reverse order: ", end=' ')
for i in reversed(range(0, N)):
    print(array[i], end=' ')
