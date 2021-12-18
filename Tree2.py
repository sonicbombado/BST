from random import randint


class info:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f'{self.id}'


class nodo:
    def __init__(self, objeto=None, esq=None, dir=None):
        self.objeto = objeto
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return f'{self.objeto.id}'


class Arvore:

    def __init__(self, raiz=None):
        self.raiz = raiz
        self.cont_espaco = 10

    def __repr__(self):
        self.exibir(self.raiz)
        return ''

    def exibir(self, raiz=None, espaco=0):

        if (raiz == None):
            return
        espaco += self.cont_espaco
        self.exibir(raiz.dir, espaco)
        print(end=" " * (espaco - self.cont_espaco))
        print(raiz.objeto.id)
        self.exibir(raiz.esq, espaco)

    def inserir(self, chave):
        objeto = info(chave)
        no = nodo(objeto)
        if (self.raiz == None):
            self.raiz = no
        else:
            atual = self.raiz
            while True:
                anterior = atual

                if chave <= atual.objeto.id:
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = no
                        return

                else:
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = no
                        return

    def Maior(self):
        ponteiro = self.raiz
        while True:
            if ponteiro.dir == None:
                break
            ponteiro = ponteiro.dir
        return f'Maior valor da árvore: {ponteiro.objeto.id}'

    def nosucessor(self, apaga):
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir

        while atual != None:
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq

        if sucessor != apaga.dir:
            paidosucessor.esq = sucessor.dir
            sucessor.dir = apaga.dir

        return sucessor

    def remover(self, v):
        if self.raiz == None:
            return False
        atual = self.raiz
        pai = self.raiz
        filho_esq = True
        while atual.objeto.id != v:
            pai = atual
            if v < atual.objeto.id:
                atual = atual.esq
                filho_esq = True
            else:
                atual = atual.dir
                filho_esq = False
            if atual == None:
                return False
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None
            else:
                if filho_esq:
                    pai.esq = None
                else:
                    pai.dir = None
        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.esq
            else:
                if filho_esq:
                    pai.esq = atual.esq
                else:
                    pai.dir = atual.esq

        elif atual.esq == None:
            if atual == self.raiz:
                self.raiz = atual.dir
            else:
                if filho_esq:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir

        else:
            sucessor = self.nosucessor(atual)

            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filho_esq:
                    pai.esq = sucessor
                else:
                    pai.dir = sucessor
            sucessor.esq = atual.esq

    def minn(self, atual):
        if atual == self.raiz:
            self.raiz = atual
        while atual.esq:
            atual = atual.esq
        return atual

    def minArvore(self):
        return f"\nValor mínimo da árvore:{(self.minn(self.raiz))}"

    def search(self, key):
        atual = self.raiz
        while atual is not None:
            if atual.objeto.id == key:
                return True
            elif key > atual.objeto.id:
                atual = atual.dir
            else:
                atual = atual.esq
        return False

    def searchChildrens(self, key):
        atual = self.raiz
        while atual is not None:
            if atual.objeto.id == key:
                x = atual.dir
                y = atual.esq
                return f'Filho direito: {x}, Filho esquerdo: {y}'
            elif key > atual.objeto.id:
                atual = atual.dir
            else:
                atual = atual.esq
        return False


arvore = Arvore()

for c in range(10):
    x = randint(1, 99)      # Populando a árvore
    arvore.inserir(x)
print(arvore)

x = int(input('Informe um valor a ser procurado na árvore: \n')) # Busca
if arvore.search(x):
  print('Valor encontrado na árvore')
else:
  print('Valor não encontrado na árvore')

print(arvore.minArvore()) # Mínimo
print(arvore.Maior()) # Máximo
print('\n')
x = int(input('Informe um valor para procurar os filhos na árvore: \n')) 
if arvore.searchChildrens(x) is not False:      # Buscar filhos na árvore
  print(arvore.searchChildrens(x))
else:
  print('Valor não existe na árvore')