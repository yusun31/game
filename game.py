import random

# 소스코드 수정 중

answer = random.randrange(1, 101)
print(answer)

count = 0

while(True):
    guess = int(input("정답을 추측해보세요.:"))
    count+=1

    if guess > answer:
        print("다운")
    elif guess < answer:
        pritn("업")
    elif guess == answer:
        break

print("축하합니다! 시도 횟수는 {}번 입니다.".format(count))
