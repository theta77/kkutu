print("[물건 개수 구하기]")
count = 0
sum = 0
for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        sum = i * 500 + j * 1000
        if sum == 10000:
            count += 1
            print(f"500원 {i}개, 1000원 {j}개")
print(f"경우의 수는 {count}개 입니다")