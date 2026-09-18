import heapq

class Node:
    def __init__(self, d, i, left=None, right=None):
        self.data = d
        self.index = i
        self.left = left
        self.right = right

def preOrder(root, ans, curr):
    if root is None:
        return

    if root.left is None and root.right is None:
        if curr == "":
            curr = "0"
        ans.append(curr)
        return

    preOrder(root.left, ans, curr + '0')
    preOrder(root.right, ans, curr + '1')

def huffmanCodes(s, freq):
    n = len(s)
    pq = []

    for i in range(n):
        tmp = Node(freq[i], i)
        heapq.heappush(pq, (tmp.data, tmp.index, tmp))

    if n == 1:
        return ["0"]

    while len(pq) >= 2:
        f1, i1, l = heapq.heappop(pq)
        f2, i2, r = heapq.heappop(pq)

        newNode = Node(l.data + r.data, min(l.index, r.index), l, r)
        heapq.heappush(pq, (newNode.data, newNode.index, newNode))

    root = pq[0][2]
    ans = []
    preOrder(root, ans, "")
    return ans

s = "abcdef"
freq = [5, 9, 12, 13, 16, 45]

print(huffmanCodes(s, freq))