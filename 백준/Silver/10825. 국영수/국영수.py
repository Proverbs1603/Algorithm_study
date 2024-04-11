N = int(input())
data = []
for _ in range(N):
    # 각 줄을 입력받고 공백을 기준으로 분리
    input_data = input().split()
    # 문자열을 제외한 나머지 값을 정수로 변환하여 리스트에 추가
    scores = list(map(int, input_data[1:]))
    # 문자열과 숫자로 이루어진 리스트를 리스트에 추가
    data.append([input_data[0], *scores])
data.sort(key=lambda x : (-x[1], x[2],-x[3], x[0]))


for result in data:
    print(result[0])