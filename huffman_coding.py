import sys
from operator import attrgetter


class Node:

    def __init__(self):
        self.name = ''
        self.weight = 0
        self.code = ''

    def initSet(self, name, weight):
        self.name = name
        self.weight = weight

    def setRoot(self, root):
        self.root = root

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def addCode(self, code):
        self.code = code + self.code


def buildHuffTree(tree):

    def setHuffcode(root, code):
        root.addCode(code)

        try:
            setHuffcode(root.left, code)
        except:
            pass
        try:
            setHuffcode(root.right, code)
        except:
            pass

        return root

    while len(tree) >= 2:
        tree = sorted(tree, key=attrgetter('weight'))
        newNode = Node()
        name = tree[0].name + tree[1].name
        weight = tree[0].weight + tree[1].weight
        newNode.initSet(name, weight)
        tree[0].setRoot(newNode)
        tree[1].setRoot(newNode)
        setHuffcode(tree[0], '1')
        setHuffcode(tree[1], '0')
        newNode.setLeft(tree[0])
        newNode.setRight(tree[1])
        tree.pop(1)
        tree.pop(0)
        tree.append(newNode)


def Decoder(codelist, code):
    huffDecode = dict((i.code, i.name) for i in codelist)
    newcode = ''
    while len(code) != 0:
        for i in range(len(code)):
            try:
                newcode += huffDecode[code[0:i+1]]
                code = code[i+1:len(code)+1]
                break
            except:
                pass
    print(newcode)


def Encoder(codelist, code):
    huffIncode = dict((i.name, i.code) for i in codelist)
    newcode = ''
    for i in range(len(code)):
        try:
            newcode += huffIncode[code[i]]
        except:
            pass
    print(newcode)


def main(opt):
    weight = input()
    code = input()
    weight = weight.split()

    Tree = [Node() for i in range(len(weight))]
    originNode = []

    for i, T in enumerate(Tree):
        T.initSet(str(i), float(weight[i]))
        originNode.append(T)

    buildHuffTree(Tree)

    option = opt
    if option == '-e':
        Encoder(originNode, code)
    elif option == '-d':
        Decoder(originNode, code)
    else:
        print("The option doesn't exist.")

if __name__ == '__main__':
    try:
        option = sys.argv[1]
    except:
        option = '-d'
    main(option)
sys.exit()
