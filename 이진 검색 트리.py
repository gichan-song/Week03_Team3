import sys

Input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

tree = []

while True:
    try:
        tree.append(int(Input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1       # 루트의 오른쪽 노드가 없을 때

    for i in range(start+1, end+1):
        if tree[i] > tree[start]:
            mid = i
            break
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(tree[start])

postorder(0, len(tree)-1)