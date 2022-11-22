class BinaryTree:
    def __init__(self, left_subtree, right_subtree):
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree
        self.binary_code = ''
        self.nodes = []
        self.update_left_codes()
        self.update_right_codes()
        self.set_nodes()

    def update_left_codes(self):
        if self.left_subtree:
            for node in self.left_subtree.nodes:
                node.binary_code = self.binary_code + '0' + node.binary_code

    def update_right_codes(self):
        if self.right_subtree:
            for node in self.right_subtree.nodes:
                node.binary_code = self.binary_code + '1' + node.binary_code

    def set_nodes(self):
        self.nodes = [self] + (self.left_subtree.nodes if self.left_subtree else []) + (
            self.right_subtree.nodes if self.right_subtree else [])

    def is_leaf(self):
        return not (self.left_subtree or self.right_subtree)

    def get_leaves(self):
        return list(filter(lambda x: x.is_leaf(), self.nodes))

    def get_interval_subdivision(self):
        binary_codes = [leaf.binary_code for leaf in self.get_leaves()]
        return [int(code, 2) / 2 ** len(code) for code in binary_codes] + [1.0]


def to_tree(expr):
    if len(expr) == 1:
        return BinaryTree(None, None)
    else:
        if expr[0] != '(':
            left_subexpr = expr[0]
            right_start_ind = 1
        else:
            left_subexpr = ''
            parentheses_diff = 1
            i = 1
            while True:
                char = expr[i]
                if char == '(':
                    parentheses_diff += 1
                if char == ')':
                    parentheses_diff -= 1
                if parentheses_diff == 0:
                    break
                left_subexpr = left_subexpr + char
                i += 1
            right_start_ind = i + 1
    if expr[right_start_ind] == '(':
        right_subexpr = expr[right_start_ind + 1:-1]
    else:
        right_subexpr = expr[right_start_ind]

    left_subtree = to_tree(left_subexpr)
    right_subtree = to_tree(right_subexpr)

    return BinaryTree(left_subtree, right_subtree)
