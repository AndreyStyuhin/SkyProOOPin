from src.product import Product



class Category:
    # Атрибуты класса для хранения общей информации
    category_count = 0  # количество категорий
    product_count = 0  # общее количество товаров

    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализация объекта Category

        :param name: название категории
        :param description: описание категории
        :param products: список товаров категории (объекты класса Product)
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличение атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """
        Геттер для получения списка товаров категории
        :return: список товаров категории
        """
        return self.__products

    def add_product(self, product):
        """
        Добавление товара в категорию
        :param product: объект класса Product или его наследника
        :raises TypeError: если передан объект неправильного типа
        """
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    def remove_product(self, product: Product):
        """
        Удаление товара из категории
        :param product: объект класса Product
        """
        if product in self.__products:
            self.__products.remove(product)
            Category.product_count -= 1

