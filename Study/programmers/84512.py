# 위클리 챌린지 5주차

word = input()

def solution(word):
    vowel = ['A','E','I','O','U']
    dic = []
    
    def make_word(cur_word):
        if len(cur_word)>5:
            return
        dic.append(cur_word)
        for v in vowel:
            make_word(cur_word+v)
    
    for v in vowel:
        make_word(v)
    
    return dic.index(word)+1
    
print(solution(word))