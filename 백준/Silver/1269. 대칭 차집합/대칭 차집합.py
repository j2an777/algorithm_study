a, b = map(int, input().split())
aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))

print(len(aSet - bSet) +len(bSet - aSet))