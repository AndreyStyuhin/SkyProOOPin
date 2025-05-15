import unittest
from src.product import Product
from src.category import Category

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        '''
        тесты для классов, которые проверяют:
            корректность инициализации объектов класса
            Category, корректность инициализации объектов класса
            Product, подсчет количества продуктов,
            подсчет количества категорий.
            #pytest #assert #fixtures
        '''
        product = Product("Test Product", "Test Description", 100, 10)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.quantity, 10)
    def test_new_product(self):
        product1 = Product("Test Product 1", "Test Description 1", 100, 10)
        product2 = Product("Test Product 2", "Test Description 2", 200, 20)
        category = Category("Test Category", "Test Description", [product1, product2])
        new_product = Product.new_product({"name": "Test Product 1", "description": "Test Description 1", "price": 150, "quantity": 5}, category.products)
        self.assertEqual(new_product.name, "Test Product 1")
        self.assertEqual(new_product.description, "Test Description 1")
        self.assertEqual(new_product.price, 150)
        self.assertEqual(new_product.quantity, 15)
        self.assertEqual(Category.product_count, 2)

    def setUp(self):
        # Создаю несколько тестовых продуктов
        self.product1 = Product("Laptop", "Powerful laptop", 50000.0, 5)
        self.product2 = Product("Phone", "Smartphone", 20000.0, 10)
        self.product3 = Product("Tablet", "Android tablet", 15000.0, 8)

        # Создаю список продуктов для тестирования
        self.products_list = [self.product1, self.product2, self.product3]

    def test_get_products_string(self):
        # Тест статического метода
        products_string = Product.get_products_string(self.products_list)

        # Ожидаемый результат
        expected = "1. Laptop, 50000.0 руб. (Остаток: 5 шт.)\n" \
                   "2. Phone, 20000.0 руб. (Остаток: 10 шт.)\n" \
                   "3. Tablet, 15000.0 руб. (Остаток: 8 шт.)"

        # Сравнение результата с ожидаемым результатом
        self.assertEqual(products_string, expected)

    def test_empty_products_list(self):
        # Тест для пустого списка продуктов
        empty_string = Product.get_products_string([])
        self.assertEqual(empty_string, "Список продуктов пуст")

