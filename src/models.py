"""
Создайте классы Product и Category
Для класса Product определите следующие свойства:
    название (name),
    описание (description),
    цена (price),
    количество в наличии (quantity).
Для класса Category определите следующие свойства:
    название (name),
    описание (description),
    список товаров категории (products).
Для этих двух классов добавьте инициализацию так, чтобы каждый параметр был передан при создании объекта и сохранен.
Также для класса Category добавьте два атрибута класса.
Доступ к этим атрибутам должен быть у каждого объекта класса, и в них должна храниться общая информация для всех объектов.
Эти атрибуты хранят в себе количество категорий и количество товаров.
Атрибуты класса должны заполняться автоматически при инициализации нового объекта.
Здесь нет необходимости считать количество на складе, можно посчитать длину списка с товарами.
(требуется только создать класс и описать атрибуты, которые будут принадлежать к каждому классу.
нужно сделать описание типов данных тех значений, которые будут храниться в атрибутах.
Для каждого поля используйте наиболее подходящий тип данных, цена может быть указана с копейками,
а количество лучше измерять в штуках. у класса «Категории» в списке товаров должны храниться именно объекты класса продуктов,
в атрибуте «Список товаров категории» должен быть список объектов класса Product.)
Важно определить, что принимает на вход метод инициализации, а также какие атрибуты используются через
self, а какие через Category, чтобы соблюсти доступность сохраненной информации для всех объектов класса
Category. Для автоматического заполнения атрибутов класса Category добавьте в код инициализации увеличение
значения атрибутов класса на необходимые значения Category.атрибут += значение
"""


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
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. (Остаток: {self.quantity} шт.)"


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
        self.products = products if products is not None else []

        # Увеличение атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product):
        """
        Add a product to the category and update counters

        Args:
            product: Product object to add to the category

        Returns:
            True if product was added, False if it's already in the category
        """
        # Check if product is already in the category
        if product not in self.products:
            self.products.append(product)
            # Increment the total unique products counter
            Category.total_unique_products += 1
            return True
        return False

    def remove_product(self, product):
        """
        Remove a product from the category and update counters

        Args:
            product: Product object to remove from the category

        Returns:
            True if product was removed, False if it wasn't in the category
        """
        if product in self.products:
            self.products.remove(product)
            # Decrement the total unique products counter
            Category.total_unique_products -= 1
            return True
        return False

    def __str__(self):
        # Format the category information with product count
        return f"{self.name}, {self.description} (количество продуктов: {len(self.products)})"

    @property
    def product_count(self):
        """Returns the number of products in this category"""
        return len(self.products)
