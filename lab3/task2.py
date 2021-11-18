from OrderPizza import OrderPizza
from Pizza import Pizza

if __name__ == '__main__':
    order1 = OrderPizza(1, None)
    order1.pizza.add_ingredient('new')
    order2 = OrderPizza(2, 'Monday')
    custom_pizza = Pizza("Custom pizza", 150, ["zucchini", "artichoke", "asparagus", "spinach", "pesto"])
    custom_pizza.add_to_json()
    order3 = OrderPizza(2, None, custom_pizza)
    print(order1)
    print(order2)
    print(order3)
