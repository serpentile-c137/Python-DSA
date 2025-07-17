class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = '\t' * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def add_child(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("drinks", [])
cold = TreeNode("cold", [])
hot = TreeNode("hot", [])

tree.add_child(cold)
tree.add_child(hot)

tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])

coke = TreeNode("coke", [])
sprite = TreeNode("sprite", [])

cold.add_child(coke)
cold.add_child(sprite)
hot.add_child(tea)
hot.add_child(coffee)

print(tree)


