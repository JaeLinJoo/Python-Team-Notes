#이 구역의 승자는 누구야?!
alpha = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

S = input()
answer = 0
for s in S:
    answer += alpha[ord(s)-ord("A")]
if answer%2==0:
    print("You're the winner?")
else:
    print("I'm a winner!")

