

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта Product

        :param name: название товара
        :param description: описание товара
        :param price: цена товара (с копейками)
        :param quantity: количество товара в наличии (в штуках)
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. (Остаток: {self.quantity} шт.)"

    @classmethod
    def new_product(cls, params: dict, products: list = None):
        """
        Создает новый экземпляр Product из словаря параметров.
        Если товар с таким же именем уже существует, обновляет его количество и выбирает максимальную цену.

        :param params: словарь с параметрами товара (name, description, price, quantity)
        :param products: список товаров, в которых нужно искать дубликаты (по имени)
        :return: новый или обновленный экземпляр Product
        """
        if products is None:
            products = []

        # Поиск товара с таким же именем
        for product in products:
            if product.name.lower() == params["name"].lower():
                # Обновление количества и выбор максимальной цены
                product.quantity += params["quantity"]
                product.price = max(product.price, params["price"])
                return product

        # Если дубликат не найден, создаем новый товар
        return cls(
            name=params["name"],
            description=params["description"],
            price=params["price"],
            quantity=params["quantity"]
        )
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print(f"Некорректная цена: {value}. Цена товара должна быть больше нуля.")
            raise ValueError("Цена не может быть меньше или равна нулю")
        self.__price = value


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

