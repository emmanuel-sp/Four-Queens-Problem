s = set()
def solve(pos: list) -> int:
    count = 0
    for i in range (len(pos)):
        l = 1
        k = 1
        for j in range(i + 1, len(pos)):
            if pos[i] == pos[j]:
                count += 1
            if pos[i] + k == pos[j]:
                count += 1
            k += 1
            if pos[i] - l == pos[j]:
                count += 1
            l += 1
    return count

def neighbors(pos: list) -> list[list]:
    l = []
    for i in range(len(pos)):
        if pos[i] < 4:
            g = pos.copy()
            g[i] = g[i] + 1
            l.append(g)
        if pos[i] > 1:
            g = pos.copy()
            g[i] = g[i] - 1
            l.append(g)
    l.sort(key = lambda x: x[3])
    l.sort(key = lambda x: x[2])
    l.sort(key = lambda x: x[1])
    l.sort(key = lambda x: x[0])
    l.sort(key = lambda x: solve(x))
    return l

def printn(d:list, i: int):
    if tuple(d) in s:
        print(f"{d} Failed")
        return
    s.add(tuple(d))
    if i == 10:
        print("Failed")
        return    
    if solve(d) == 0:
        print(f"Solution reached with: {d}")
        return
    print(f"Step {i + 1})")
    print(f"{d} h = {solve(d)}")
    print("Neighbors:")
    for l in neighbors(d):
        print(f"{l} = {solve(l)}")
    print("\n")
    
    printn(neighbors(d)[0], i + 1)

printn([1,2,3,4], 0)
    
        

