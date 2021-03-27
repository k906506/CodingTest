import sys

def search(node, src, visit):
    if src not in visit:
        visit.append(src)
        for element in node[src]:
            search(node, element, visit)
    return visit

def main():
    n, m = map(int, input().split())
    node = dict()
    
    for i in range(1, n+1):
        node[i] = []
    
    for i in range(n-1):
        src, dst = map(int, sys.stdin.readline().split())
        node[src].append(dst)
    
    for i in range(m):
        src, dst = map(int, sys.stdin.readline().split())

        visit = list()
        visit = search(node, src, visit)

        if dst in visit:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()