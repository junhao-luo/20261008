A = int(input())
B = int(input())

if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("輸入錯誤")
else:
    if A == 1 or B == 1:
        result_or = 1
    else:
        result_or = 0

    if A == 1 and B == 1:
        result_and = 1
    else:
        result_and = 0

    if A != B:
        result_xor = 1
    else:
        result_xor = 0

    print(f"OR={result_or}")
    print(f"AND={result_and}")
    print(f"XOR={result_xor}")