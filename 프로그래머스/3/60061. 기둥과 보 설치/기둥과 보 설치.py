#build_frame의 원소는 [x, y, a, b]형태입니다.
#x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
#a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
#b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.

def check_build(answer):
    for x, y, a in answer:
        #기둥인 경우
        if a==0:

            if (y!=0 and                        #좌표가 바닥에 있지 않을때
                [x,y-1,0] not in answer and     #좌표 아래에 기둥이 존재하지 않을 때
                [x, y, 1] not in answer and     #보의 한 쪽 위 X
                [x-1,y,1] not in answer):       #보의 한 쪽 위 X
                return False
        #보인 경우
        else:
            
            if([x,y-1,0] not in answer and      #아래에 기둥 존재 X
               [x+1,y-1,0] not in answer and    #아래에 기둥 존재 X
               ([x-1,y,1] not in answer or      #양쪽에 보 존재 X
               [x+1,y,1] not in answer)):       #양쪽에 보 존재 X
                return False
    return True


def solution(n, build_frame):
    answer = []

    #빌드프레임 만큼 반복해서 확인
    for x,y,a,b in build_frame:
        #삭제라면
        if b == 0:
            answer.remove([x,y,a])
            #삭제 후, check가 통과되지 못하면, 재설치
            if not check_build(answer):
                answer.append([x,y,a])
        
        #설치라면
        elif b==1:
            answer.append([x,y,a])
            #설치 후, check가 통과되지 못하면, 삭제처리
            if not check_build(answer):
                answer.remove([x,y,a])
    
    answer.sort(key=lambda x : (x[0], x[1], x[2]))            
    return answer