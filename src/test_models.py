import unittest
from src.models import Product, Category


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


class TestCategory(unittest.TestCase):
    def setUp(self):
        # Сброс аттрибутов класса перед следующим тестом
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        category = Category("Test Category", "Test Description")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test Description")
        self.assertEqual(category.products, [])

    def test_category_count(self):
        Category("Category 1", "Description 1")
        self.assertEqual(Category.category_count, 1)
        Category("Category 2", "Description 2")
        self.assertEqual(Category.category_count, 2)

    def test_product_count(self):
        product1 = Product("Product 1", "Description 1", 100, 10)
        product2 = Product("Product 2", "Description 2", 200, 20)

        Category("Category 1", "Description 1", [product1])
        self.assertEqual(Category.product_count, 1)

        Category("Category 2", "Description 2", [product2])
        self.assertEqual(Category.product_count, 2)
