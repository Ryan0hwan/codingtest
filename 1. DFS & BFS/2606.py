def dfs(c):
    global ans            # 이것만 주의.
    v[c] = 1
    ans += 1
    
    for n in adj[c]:
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

ans = 0
v = [0]*(N+1)
dfs(1)

print(ans-1)        # 처음 1은 포함 안됨
