k = int(input())
def merge(*lsts):
    lsts = []
    for l in range(k):
        ls =+ list(map(int, input().split(',')))
        print(f"ls = {ls}, sorted(ls) = {sorted(ls)}" )
        lsts.sort()
    return lsts
print(f"ls = {ls}, sorted(ls) = {sorted(ls)}" )
print (merge(*lsts))
