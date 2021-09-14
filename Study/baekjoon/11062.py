#카드 게임 
## 참고 (https://hillier.tistory.com/97)

def solution(cards, i, j): #cards에서 i번째부터 j번쨰 카드가 있을 때 카드를 선택하는 함수
    if dp[i][j]: #이미 정보가 있는 경우
        return dp[i][j]
    
    if i == j: #한장만 남은 경우, 첫번째 사람만 가져감
        dp[i][j] = [cards[i], 0]
        return dp[i][j]
    
    first1, second1 = solution(cards,i+1, j) #왼쪽에서 뽑는 경우
    score1 = second1 + cards[i]

    first2, second2 = solution(cards,i,j-1) #오른쪽에서 뽑는 경우
    score2 = second2 + cards[j]

    if score1>score2:
        dp[i][j] = [score1,first1]
    else:
        dp[i][j] = [score2,first2]
    
    return dp[i][j]


t = int(input())
for i in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [[None for _ in range(n+1)] for _ in range(n+1)] #[1번째로 뽑는 사람 점수, 2번째 뽑는 사람 점수]
    print(solution(cards,0,n-1)[0])

