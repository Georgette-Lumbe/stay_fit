from django.test import TestCase
from .models import Category, Product


class TestCategoryModel(TestCase):
    """
    test the category model
    """

    def test_category_string_method_returns_name(self):
        """
        test category model string method
        """
        category = Category.objects.create(name="category_name")
        self.assertEqual(str(category), "category_name")

    def test_category_friendly_name_str_method(self):
        """
        testing category models friendly name string
        method returns friendly name
        """
        test_case = Category()
        test_case.friendly_name = "Friendly"
        self.assertEqual(test_case.get_friendly_name(), "Friendly")


class TestProductModel(TestCase):
    """
    test product model
    """
    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_product_string_method_returns_name(self):
        """
        test product model string method
        """
        product = Product.objects.create(name="product_name", price=21.99)
        self.assertEqual(str(product), "product_name")
