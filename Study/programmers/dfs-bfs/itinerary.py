#여행 경로
n = int(input())
tickets = [list(map(str, input().split())) for _ in range(n)]

def solution(tickets):
    answer = []
    start = "ICN"
    stack = [start]
    
    return answer