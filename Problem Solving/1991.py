import sys

def pre_order(node):
  if node == '.':
    return
  print(node, end='')
  pre_order(tree[node][0])
  pre_order(tree[node][1])

def post_order(node):
  if node == '.':
    return
  post_order(tree[node][0])
  print(node, end='')
  post_order(tree[node][1])

def in_order(node):
  if node == '.':
    return
  in_order(tree[node][0])
  in_order(tree[node][1])
  print(node, end='')

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
  node, left, right = sys.stdin.readline().strip().split(' ')
  tree[node] = (left, right)

pre_order('A')
print()
post_order('A')
print()
in_order('A')