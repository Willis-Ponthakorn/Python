class node:
    def __init__(self,data,next=None):
        self.head = None
        self.data = data
      
    def __str__(self):
        s = ''
        current = self.head
        while(current):
            s+=str(current.data)
            current = current.next
        return s

def createList(l=[]):
    current = node('')
    for i in l:
        new_node = node(int(i))
        new_node.next = current.head
        current.head=new_node
    return current
    
def printList(H):
    cc = H.head
    s = []
    while(cc):
        s.append(str(cc.data))
        cc = cc.next
  
    return ' '.join(s[::-1])
def printListm(H):
    cc = H.head
    s =''
    while(cc):
        s+=str(cc.data) + ' '
        cc = cc.next
    return s


def mergeOrderesList(p,q):

    v = []
    m = node('')
    lp = p.head
    lq = q.head
    while lp!=None or lq!=None:

        if lp!=None and lq!=None:
            if lp.data > lq.data:
                new_node = node(lp.data)
                new_node.next = m.head
                m.head=new_node
                lp = lp.next
            else:
                new_node = node(lq.data)
                new_node.next = m.head
                m.head=new_node
                lq = lq.next
        else:
            if lp!=None:
                new_node = node(lp.data)
                new_node.next = m.head
                m.head=new_node
                lp = lp.next
            else:
                new_node = node(lq.data)
                new_node.next = m.head
                m.head=new_node
                lq = lq.next

    return m

s = input('Enter 2 Lists : ').split()

LL1 = createList(s[0].split(','))
LL2 = createList(s[1].split(','))
print('LL1 :',printList(LL1))
print('LL2 :',printList(LL2))
m = mergeOrderesList(LL1,LL2)
print('Merge Result :',printListm(m))