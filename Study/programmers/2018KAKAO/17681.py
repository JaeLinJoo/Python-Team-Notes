# [1차] 비밀지도

n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def solution(n, arr1, arr2):
    
    #2진수로 변경
    def turn_binary(n, arr):
        for i,a in enumerate(arr):
            binary = format(a,"b")
            if len(binary)!=n:
                while len(binary)!=n : binary = '0'+binary
            arr[i] = binary
        return arr
    arr1 = turn_binary(n,arr1)
    arr2 = turn_binary(n,arr2)


    secret_map = []
    for i in range(n):
        answer = ''
        for j in range(n):
            if int(arr1[i][j]) + int(arr2[i][j]) == 0:
                answer += ' '            
            else:
                answer += '#'
        secret_map.append(answer)
    
    return secret_map

print(solution(n,arr1,arr2))


# 다른 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer



