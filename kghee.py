# a = 5
# if a == 5:
#     print("엘소드")
# print("롤")

# first = 1; last = 10; plma = 1
# for i in range(first, last, plma):
#     print(f"i = {i}, 엘소드")
# print("롤")

# li = ["엘소드", "냥코대전쟁", "롤"]
# for i in li: # -> for i in range(0, 3, 1):
#     print(i) # ->   print(li[i])
# for i in range(0, 3, 1):
#     print(li[i])
# print("쿠키런")

# 첫번째 : i에 first 자리에 들어가는 값이 들어감
# 두번째 : (first가 last보다 작다는 가정하에) i가 last보다 작은지 비교를 해
# 세번째 : 위의 조건이 참이라면 코드를 실행해
# 엘소드
# 네번째 : 코드가 끝났으면 위로 올라가서 plma에 있는 값을 i에 더해
# 다섯번째 : '두번째'의 조건을 다시 실행해
# ~
# 마지막 : i가 last보다 커짐
# 반복문에서 나와


# 첫번째 실행 : i = 1 = first
# i = 1, 비교 결과 = True, 실행 결과 = 엘소드

# 두번째 실행 : i = 3 = second = first + 2
# 세번째 실행 : i = 5 = third = second + 2 = first + 2 + 2
# 네번째 실행 : i = 7 = fourth = third + 2 ~
# 다섯번째 실행 : i = 9 = fifth = fourth + 2 ~
# 여섯번째 실행 : i = 11 = sixth = fifth + 2 ~

# a = 10
# i = 0
# while i < a + 1:
#     i += 1
#     if i % 3 == 0:
#         continue
#     print(f"i : {i}, 엘소드")
# print("롤")

# a = input("이름 : ")
# print(a)

# a = 1234
# print("%08d" %(a))

# a = 12.34
# print("%.0f" %(a))