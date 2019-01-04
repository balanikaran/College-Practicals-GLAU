from itertools import combinations

def findSet(m, notes):
    s = set(notes)
    subsets = sum(map(lambda r: list(combinations(s, r)), range(1, len(s)+1)), [])
    for subset in subsets:
        # print(sum(set(subset)))
        if sum(set(subset)) == m:
            return "Yes"
    return "No"

t = int(input())
for i in range(t):
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    notes = [int(x) for x in input().split()]
    print(findSet(m, notes))