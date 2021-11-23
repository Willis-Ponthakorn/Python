class Node:
    def __init__(self, data, freq, left = None, right = None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def addSortList(li,node):
    newli = []
    if len(li) == 0:
        newli.append(node)
    for i in range(len(li)):
        if li[i].freq < node.freq:
            newli += li[0:i] + [node] + li[i::]
            break
        if li[i].freq == node.freq:
            if li[i].data != '*' and node.data != '*':
                if ord(li[i].data) < ord(node.data):
                    newli += li[0:i] + [node] + li[i::]
                    break
            elif li[i].data == '*' and node.data == '*':
                newli += li[0:i] + [node] + li[i::]
                break
        if i == len(li)-1:
            newli = li + [node]
            break
    return newli

def huffman_code(node, left=True, binString=''):
    if node.data != '*':
        return {node.data: binString}
    d = dict()
    d.update(huffman_code(node.right, False, binString + '1'))
    d.update(huffman_code(node.left, True, binString + '0'))  
    return d

inp = input("Enter Input : ")
T = Tree()
freq = {}
li = []
char = []
for i in inp:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    if i not in char:
        char.append(i)
while len(char) > 0:
    temp = char.pop()
    li = addSortList(li,Node(str(temp),int(freq[temp])))
print([e.data for e in li])
while len(li) > 1:
    temp1 = li.pop()
    temp2 = li.pop()
    li = addSortList(li,Node('*',temp1.freq+temp2.freq,temp1,temp2))
    print([e.data for e in li])
T.root = li.pop()
allCode = huffman_code(T.root)
print(allCode)
T.printTree(T.root)
print("Encoded! :",''.join(allCode[e] for e in inp))