from collections import Counter

def avg(n):
    listavg = sum(n) / len(n)
    return listavg

def maxFrequency(n):
    count = Counter(n)
    max_freq = max(count.values())
    modes = [key for key, values in count.items() if values == max_freq] #items() 메서드는 (key,value)쌍의 리스트를 반환
    result = str(modes[0])
    return result

intList = []
for _ in range(10):
    intList += list(map(int, input().split()))

print(int(avg(intList)))
print(maxFrequency(intList))

