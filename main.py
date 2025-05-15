from src.product import Product
from src.category import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("Товары в категории до добавления нового товара:")
    for product in category1.products:
        print(product)

    # Создание нового товара с именем, которое уже существует
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 190000.0, "quantity": 3},
        category1.products
    )

    print("\nТовары в категории после добавления нового товара:")
    for product in category1.products:
        print(product)

    # Проверка, что количество и цена обновились
    print("\nПроверка обновления товара:")
    print(f"Количество: {product1.quantity}")  # Ожидается 8 (5 + 3)
    print(f"Цена: {product1.price}")          # Ожидается 190000.0 (максимум из 180000 и 190000)

    # Проверка вывода информации о товарах
    print("\nИнформация о товарах в категории:")
    category1 = Category("Фрукты", "Фрукты и овощи")
    category1.add_product(Product("Яблоко", 80.5, 15, "Фрукты"))
    category1.add_product(Product("Банан", 119.99, 20, "Фрукты"))

    # Получение исходных объектов
    print("Объекты продуктов:", category1.products)

    # Получение форматированных строк с информацией о продуктах
    for info in category1.products_info:
        print(info)