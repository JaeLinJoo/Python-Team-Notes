#여행 경로
n = int(input())
tickets = [list(map(str, input().split())) for _ in range(n)]

def solution(tickets):
    tickets.sort(reverse=True)
    answer = []
    start = ["ICN"]
    route = {}
    for f, t in tickets:
        if f in route:
            route[f].append(t)
        else:
            route[f] = [t]

    while start:
        s = start[-1]
        if s not in route or len(route[s]) == 0:
            answer.append(start.pop())
        else:
            start.append(route[s].pop())
    answer.reverse()
    return answer

print(solution(tickets))