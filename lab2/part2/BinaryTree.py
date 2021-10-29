from Product import Product


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def delete(self):
        self.root = None

    def insert(self, value):
        if self.find(value.product_code):
            raise ValueError("Product codes must be unique!")
        if not isinstance(value, Product):
            raise TypeError('Inserted data must be a Product type!')
        if not self.root:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    @staticmethod
    def __insert(node, value):
        if value.product_code < node.data.product_code:
            if node.left:
                BinaryTree.__insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                BinaryTree.__insert(node.right, value)
            else:
                node.right = Node(value)

    def find(self, product_code):
        if self.root:
            return self.__find(product_code, self.root)
        else:
            return None

    @staticmethod
    def __find(product_code, node):
        if product_code == node.data.product_code:
            return node
        elif product_code < node.data.product_code and node.left:
            return BinaryTree.__find(product_code, node.left)
        elif product_code > node.data.product_code and node.right:
            return BinaryTree.__find(product_code, node.right)

    def delete_item(self, product_code):
        if self.root:
            self.__delete_item(product_code, self.root)
        else:
            print('Tree is empty!')

    @staticmethod
    def __delete_item(product_code, node):
        if product_code < node.data.product_code:
            node.left = BinaryTree.__delete_item(product_code, node.left)
        elif product_code > node.data.product_code:
            node.right = BinaryTree.__delete_item(product_code, node.right)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            temp = BinaryTree.find_min_val(node.right)
            node.data.product_code = temp.product.code
            node.right = BinaryTree.__delete_item(temp.product_code, node.right)
        return node

    @staticmethod
    def find_min_val(node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def print_tree(self):
        if self.root:
            self.__print_tree(self.root)

    def __print_tree(self, node):
        if node:
            self.__print_tree(node.left)
            print(str(node.data))
            self.__print_tree(node.right)

    def count_price(self, product_code, quantity):
        return f'Total price: {self.find(product_code).data.price * quantity}'


