import sys

N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]


##전위/중위/후위 순회마다 재귀함수 코드의 순서 바꾸기
#한번 재귀할 때마다 탐색을 한번 더 하는 의미로 받아들이자
#함수 안의 ~~order(tree[root][0]) 재귀함수는 왼쪽으로 끝까지 탐색한다는 의미
#함수 안의 ~~order(tree[root][1]) 재귀함수는 오른쪽으로 끝까지 탐색한다는 의미
#root -> 출력하면 됨

#1. 전위 순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식이므로 재귀함수 순서도 root 출력문 -> 왼쪽 재귀함수 -> 오른쪽 재귀함수

def preorder(root): #루트 -> 왼쪽 자식 -> 오른쪽 자식 순으로 탐섹
    if root != '.':
        print(root, end="") #root
        preorder(tree[root][0]) #left -> right 가 새로운 root가 된다.
        preorder(tree[root][1]) #right -> right 가 새로운 root가 된다.

#2. 중위 순회 : 왼쪽 자식 -> 루트 -> 오른쪽 자식이므로 재귀함수 순서도 root 출력문 -> 오른쪽 재귀함수
def inorder(root):
    if root != '.':
        #Test case를 예로 들면, B에서 tree[root][0] = 'D'이고 D의 tree(root[0]) = "." 이 돼서 root인 D를출력하고 right로 넘어간다
        inorder(tree[root][0])#left
        print(root, end='') #root
        inorder(tree[root][1]) #right
#후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 루트이므로 재귀함수 순서도 왼쪽 재귀함수 -> 오른쪽 재귀함수 -> 루트 출력문
def postorder(root):
    if root != '.':
        postorder(tree[root][0])#left
        postorder(tree[root][1])#right
        print(root, end="")#root

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()