class Tree:
    def __init__(self,id):
        self.id = id
        self.left = None
        self.right = None


def linear_search(no,id):
    while no is not None:
        if no.id == id:
            return no
        elif id > no.id:
            no = no.right
        else:
            no = no.left
    return None

def insert(no, id):
    if no is None:
        no = Tree(id)
    else:
        if id < no.id:
            no.left = insert(no.left, id)
        else:
            no.right = insert(no.right,id)
    return no
def max(x, y):
    if x > y:
        return x
    return y

def height(no):
    if no is None:
        return 0
    return 1 + max(height(no.left), height(no.right))
def search_father(no, f):
    father = no
    while no is not None:
        if no.id == f:
            return father 
        father = no
        if no.id < f:
            no = no.right
        else:
            no = no.left
    return father
def mLeft(no):
    no = no.left
    while no.right is not None:
        no = no.right
    return no
def delete(no,f):
    now = linear_search(no,f)
    if now is None:
        return False
    father = search_father(no,f)
    if now.left is None or now.right is None:
        if now.left is None:
            another = now.right
        else:
            another = now.left
        if father is None:
            no = another
        elif f > father.id:
            father.right = another
        else:
            father.left = another
    else:
        another = mLeft(now)
        now.id = another.id
        if another.left is not None:
            now.left = another.left
        else:
            now.left = None
    return True

def balance(no):
    if no is None:
        return True
    h_left = height(no.left)
    h_right = height(no.right)

    if abs(h_left - h_right) > 1:
        return False
    return balance(no.left) and balance(no.right)


def minHeight(no):
    q = []
    q.append(({'node': no, 'depth': 1}))
    while (len(q)>0):
        queueItem = q.pop(0)
        node = queueItem['node']
        depth = queueItem['depth']
        if node.left is None and node.right is None:
            return depth
        if node.left is not None:
            q.append({'node': node.left, 'depth': depth+1})
        if node.right is not None:
            q.append({'node':node.right, 'depth': depth+1})

def minHeight2(no):

    if no is None:
        return 0
    if no.left is None and no.right is None:
        return 1

    if no.left is None:
        return minHeight2(no.right)+1
    if no.right is None:
        return minHeight2(no.left) +1
     
    return min(minHeight2(no.left), minHeight2(no.right))+1


arvore = Tree(70)
insert(arvore,1)
insert(arvore,76)
insert(arvore,56)
insert(arvore,90)
insert(arvore,6)
insert(arvore,90)


print(height(arvore.right), height(arvore.left)) # Altura de ambos os lados da árvore
print(height(arvore)) # Altura máxima da árvore
print(minHeight(arvore)) # Altura mínima da árvore usando o método 1
print(minHeight2(arvore)) # Altura mínima da árvore usando o método 2

if balance(arvore): print('A árvore é balanceada') 
else: 
  print('A árvore não é balanceada') # Checar se a árvore é balanceada

  # Buscando o valor

if linear_search(arvore,6) is not None:
    print('O valor foi encontrado')
else:
    print('O valor não foi encontrado')


# Deletando o valor 

if delete(arvore, 6):
  print('Valor deletado com sucesso')
else:
  print('Valor não encontrado')


# Buscando novamente o valor

if linear_search(arvore,6) is not None:
    print('O valor foi encontrado')
else:
    print('O valor não foi encontrado')