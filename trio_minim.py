def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    grau = [0] * (n + 1)

    for u, v in edges:
        adj[u][v] = True
        adj[v][u] = True
        grau[u] += 1
        grau[v] += 1

    major = [[] for _ in range(n + 1)]
    for u, v in edges:
        if u > v:
            u, v = v, u
        major[u].append(v)

    millor = -1

    for i in range(1, n + 1):
        adj_i = adj[i]
        for j in major[i]:
            adj_j = adj[j]
            base = grau[i] + grau[j] - 6

            for k in major[j]:
                if adj_i[k]:
                    g = base + grau[k]
                    if millor == -1 or g < millor:
                        millor = g
    return millor