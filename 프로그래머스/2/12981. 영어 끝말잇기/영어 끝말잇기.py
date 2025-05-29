def solution(n, words):
    used_words = set()
    
    for i in range(len(words)):
        if i == 0:
            used_words.add(words[i])
        else:
            if words[i] in used_words or words[i-1][-1] != words[i][0]:
                return [(i % n) + 1, (i // n) + 1]
            used_words.add(words[i]) 

    return [0,0]