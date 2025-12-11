data = [x.strip().split(': ') for x in open('in').readlines()]
paths = {x[0]:x[1].split() for x in data}

ans_1= 0
ans_2= 1

cache = {}
def getNext(curr, paths):
    if curr in cache:
        return cache[curr]
    ret = [tuple([x]) for x in  paths.get(curr, [])]
    cache[curr] = ret
    return ret

def pathFrom(starting,target,paths,toskip):
    memos = {}
    query= [(starting,x) for x in paths[starting]]
    memos = {k:0 for k in toskip if k != target}
    while query:
        n = query.pop()
        l = n[-1]
        if l == target:
            for node in n[:-1]:
                memos[node] = memos.get(node,0) + 1
        else:
            nxt = getNext(l,paths) 
            for node in nxt:
                if node[0] in memos:
                    for elem in n:
                        memos[elem] = memos.get(elem,0) + memos[node[0]]
            ns = [n+x for x in nxt if x[-1] not in memos]
            query.extend(ns)
    return memos

ans_1 = pathFrom("you","out",paths,{})["you"]

c1 = pathFrom("dac", "out",paths,{})
c2 = pathFrom("fft", "dac", paths,c1)
c3 = pathFrom("svr", "fft", paths,c2)
print(c1["dac"])
print(c2["fft"])
print(c3["svr"])

ans_2 = c1["dac"] * c2["fft"] * c3["svr"]
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
