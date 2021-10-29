from BinaryTree import BinaryTree
from Product import Product

if __name__ == '__main__':
    product1 = Product(253, 250, 'Phone', 350)
    product2 = Product(532, 1296, 'Macbook', 1299)
    product3 = Product(296, 524, 'Laptop', 1596)
    binarytree = BinaryTree()
    binarytree.insert(product1)
    binarytree.insert(product2)
    binarytree.insert(product3)
    binarytree.print_tree()
    # binarytree.delete_item(532)
    # binarytree.print_tree()
    while True:
        print("Enter product_code and quantity to count price. 'stop' to exit")
        answer = input()
        if answer == 'stop':
            break
        args = answer.split()
        if len(args) != 2:
            print('Enter two arguments!')
            continue
        try:
            product_code = int(args[0])
            quantity = int(args[1])
        except:
            print('Entered values must be Integer type!')
            continue
        if product_code <= 0 or quantity <= 0:
            print('Entered values must be more than 0!')
            continue
        if not binarytree.find(product_code):
            print('There is no product with such code!')
            continue
        print(binarytree.count_price(product_code, quantity))
