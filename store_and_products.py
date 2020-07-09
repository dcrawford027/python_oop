import math

class Store:
    def __init__(self, name, listOfProducts=[]):
        self.name = name
        self.listOfProducts = listOfProducts

    def addProduct(self, newProduct):
        self.listOfProducts.append(newProduct)
        return self

    def sellProduct(self, id):
        print(self.listOfProducts[id])
        self.listOfProducts.pop(id)
        return self

    def inflation(self, percentIncrease):
        for product in self.listOfProducts:
            product.updatePrice(percentIncrease, True)
        return self

    def clearance(self, percentDecrease):
        for product in self.listOfProducts:
            product.updatePrice(percentDecrease, False)
        return self


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def updatePrice(self, percentChange, isIncreased):
        if isIncreased:
            self.price += self.price * percentChange
        else:
            self.price -= self.price * percentChange
        return self

    def printInfo(self):
        print(self.name, self.category, self.price)
        return self

store = Store('myStore')
prod1 = Product('book', 20, 'education')
prod2 = Product('action_figure', 39.99, 'toy')
prod3 = Product('lamp', 89.99, 'furniture')

store.addProduct(prod1)
store.addProduct(prod2)
store.sellProduct(0)
store.addProduct(prod3)

prod1.updatePrice(0.25, True)
prod1.printInfo
prod1.updatePrice(0.6, False)
prod1.printInfo

store.inflation(0.1)
for product in store.listOfProducts:
    product.printInfo
store.clearance(0.4)
for product in store.listOfProducts:
    product.printInfo