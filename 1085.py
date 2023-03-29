x, y, w, h = map(int, input().split())
dist = []
dist.append(w-x)
dist.append(h-y)
dist.append(x)
dist.append(y)

print(min(dist))