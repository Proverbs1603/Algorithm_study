def solution(bandage, health, attacks):
    now_health = health #현재체력
    time = 0 #현재시간
    cast_time = bandage[0] #시전시간
    t_heal = bandage[1] #초당 회복량
    add_heal = bandage[2] #추가 회복량
    
    l_attacks = attacks[len(attacks)-1][0] #공격횟수 시간
    idx = 0 #리스트 인덱스

    #체력회복
    def heal(now_health, time):
        nonlocal t_heal
        nonlocal health
        nonlocal cast_time
        nonlocal add_heal
        
        #캐스팅 회복이 성공했는지 여부 변수
        is_success = False
        
        #초당체력 회복하기
        future_health = now_health + t_heal
        
        #캐스팅 시간이 충족되면 추가힐
        if (time == cast_time):
            future_health += add_heal
            is_success = True
            
        #현재체력 + 초당회복력이 최대체력을 넘어가면 최대체력 되기
        if (future_health >= health):
            future_health = health
    
        
        return future_health, is_success
    
    answer = 0
    #시뮬레이션 시작
    while True:


        #피가 0 이하로 떨어지면 -1 리턴
        if (now_health <= 0):
            answer = -1
            break
        
        #몬스터 공격이 다끝나면 현재 체력 리턴 
        if (l_attacks < idx):
            answer = now_health
            break

        
        time += 1 #시간 1초 증가
        
        #몬스터가 공격하는지 확인
        if (idx == attacks[0][0]):
            now_health -= attacks[0][1]
            time = 0 #캐스팅시간 초기화
            idx += 1 #idx 증가
            attacks.pop(0)  #공격했다면 pop하기 
            continue
        
        #힐 하기
        now_health, is_success = heal(now_health, time)
        #캐스팅 스킬 성공시 시간초기화
        if is_success:
            time = 0 
            
        #idx 증가
        idx += 1
    
    
    return answer

