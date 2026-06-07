import time
from product import Product


class SupermarketCMS:
    def __init__(self):
        self.product_list = [
            Product("苹果", "水果", 5.99, 100, "新鲜红富士苹果"),
            Product("牛奶", "乳制品", 65.00, 50, "进口纯牛奶"),
            Product("面包", "食品", 8.50, 80, "全麦面包"),
            Product("洗发水", "日用品", 35.00, 60, "去屑止痒"),
            Product("大米", "粮油", 45.00, 200, "优质大米")
        ]

    @staticmethod
    def show_view():
        print("*" * 30)
        print("超市商品管理系统V2.0版本")
        print("\t1. 添加商品信息")
        print("\t2. 删除商品信息")
        print("\t3. 修改商品信息")
        print("\t4. 查询单个商品信息")
        print("\t5. 查询所有商品信息")
        print("\t6. 库存预警查询")
        print("\t0. 退出系统")
        print("*" * 30)

    def add_product(self):
        name = input("请输入商品名称：")
        category = input("请输入商品类别：")
        while True:
            try:
                price = float(input("请输入商品价格："))
                break
            except ValueError:
                print("价格必须是数字，请重新输入！")
        while True:
            try:
                stock = int(input("请输入商品库存："))
                break
            except ValueError:
                print("库存必须是整数，请重新输入！")
        desc = input("请输入商品描述信息（可选）：")

        product = Product(name, category, price, stock, desc)
        self.product_list.append(product)
        print(f"添加{name}商品信息成功！\n")

    def del_product(self):
        del_name = input("请输入要删除的商品名称：")
        found = False
        for product in self.product_list:
            if product.name == del_name:
                self.product_list.remove(product)
                print(f"商品{del_name}信息删除成功~\n")
                found = True
                break
        if not found:
            print("查无此商品，请重新检查!\n")

    def update_product(self):
        update_name = input("请输入要修改的商品名称：")
        found = False
        for product in self.product_list:
            if product.name == update_name:
                product.name = input("请录入修改后的商品名称：")
                product.category = input("请录入修改后的类别：")
                while True:
                    try:
                        product.price = float(input("请录入修改后的价格："))
                        break
                    except ValueError:
                        print("价格必须是数字，请重新输入！")
                while True:
                    try:
                        product.stock = int(input("请录入修改后的库存："))
                        break
                    except ValueError:
                        print("库存必须是整数，请重新输入！")
                product.desc = input("请录入修改后的描述信息：")
                print(f"商品{update_name}信息修改成功！\n")
                found = True
                break
        if not found:
            print("查无此商品，请重新操作！\n")

    def search_one_product(self):
        search_name = input("请输入要查找的商品名称：")
        found = False
        for product in self.product_list:
            if product.name == search_name:
                print(product)
                found = True
                break
        if not found:
            print("查无此商品，请重新操作！\n")

    def search_all_product(self):
        if len(self.product_list) == 0:
            print("暂无商品信息，请先添加\n")
        else:
            for product in self.product_list:
                print(product)
            print()

    def low_stock_alert(self):
        threshold = 10
        low_stock_items = [p for p in self.product_list if p.stock <= threshold]
        if not low_stock_items:
            print("所有商品库存充足！\n")
        else:
            print(f"库存预警（库存≤{threshold}件）：")
            for product in low_stock_items:
                print(f"商品: {product.name}, 库存: {product.stock}件")
            print()

    def start(self):
        while True:
            time.sleep(0.5)
            SupermarketCMS.show_view()
            input_num = input("请输入要操作的编号：")
            if input_num == "1":
                self.add_product()
            elif input_num == "2":
                self.del_product()
            elif input_num == "3":
                self.update_product()
            elif input_num == "4":
                self.search_one_product()
            elif input_num == "5":
                self.search_all_product()
            elif input_num == "6":
                self.low_stock_alert()
            elif input_num == "0":
                result = input("您确定要退出吗？（Y/N）->")
                if result.lower() == "y":
                    print("谢谢您的使用，期待下次再会\n")
                    break
            else:
                print("输入错误\n")


if __name__ == "__main__":
    cms = SupermarketCMS()
    cms.start()