class ProductOfNumbers:
    def __init__(self, products=[], count=0):
        self.products = products
        self.count = count

    def add(self, num: int) -> None:
        self.count += 1
        if num == 0:
            self.products = [1]

        elif self.products == []:
            self.products.append(num)

        else:
            new_product = self.products[-1] * num
            self.products.append(new_product)

    def getProduct(self, k: int) -> int:
        return int(self.products[-1] / self.products[len(self.products) - (k + 1)])
