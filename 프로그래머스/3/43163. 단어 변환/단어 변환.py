from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    if begin not in words:
        words.append(begin)

    word_graph = {word: [] for word in words}
        
    for word in words:
        # 원래 단어
        org_word = word
        # 원래 단어를 한글자씩 변형
        for i in range(len(org_word)):
            word_list = list(word)
            for letter in range(ord('a'), ord('z')+1):
                word_list[i] = chr(letter)
                trans_word = ''.join(word_list)
                if trans_word in words and trans_word != org_word:
                    word_graph[org_word].append(trans_word)
    
    queue = deque()
    
    def bfs(node):
        
        min_dist = int(1e9)
        queue.append((node, 0))
        while queue:
            node, dist = queue.popleft()
            if node == target:
                min_dist = dist
                return min_dist
            
            for new_node in word_graph[node]:
                queue.append((new_node, dist+1))
        
    return bfs(begin)