#이 문제는 다음에 다시 풀어보도록 하자..ㅎㅎ
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if data[0] == '1':
  count0 += 1
else:
  count1 +=1

for i in range(len(data) -1):
  if data[i] != data[i + 1]:
    #다음  수가 1로 바뀔 때
    if data[i + 1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count0, count1))
  