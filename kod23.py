class Product:

    def __init__(self, name, price, quality, tax):
        if isinstance(name, str):
            self.name = name
        else:
            self.name = ""
        if price >= 0:
            self.price = price
        else:
            self.price = 0
        self.quality = 0 if quality < 0 else quality
        self.tax = tax if tax >= 0 else 0
