class Product:
    def __init__(self, name, category, price, stock, desc=""):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.desc = desc

    def __str__(self):
        return f"商品名称: {self.name}\n类别: {self.category}\n价格: ¥{self.price:.2f}\n库存: {self.stock}件\n描述: {self.desc}\n"