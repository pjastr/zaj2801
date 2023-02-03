class Product:

    def __init__(self, name: str, price: float, quality: int, tax: float):
        if name.isalpha():
            self.name = name
        else:
            self.name = ''

        if price < 0:
            self.price = 0
        else:
            self.price = price

        if quality < 0:
            self.quality = 0
        else:
            self.quality = quality

        if tax < 0:
            self.tax = 0
        else:
            self.tax = tax
