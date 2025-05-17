N, M = map(int, input().split())
amount = []
for _ in range(N):
    amount.append(int(input()))

def binary_search(n, m, amount):
    low = max(amount)
    high = sum(amount)

    while low < high:
        mid = (low + high) // 2
        if possible_k(mid, m, amount):
            high = mid
        else:
            low = mid + 1

    return low


def possible_k(mid, m, amount):
    out_count = 1
    remain = mid

    for cost in amount:
        if cost > mid:
            return False
        if remain < cost:
            out_count += 1
            remain = mid
        remain -= cost
    return out_count <= m

print(binary_search(N, M, amount))