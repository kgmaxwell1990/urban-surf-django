from django.test import TestCase

from .views import user_cart
from django.core.urlresolvers import resolve
 
class CartTest(TestCase):
    def test_cart_resolves(self):
        cart_page = resolve('/cart/')
        self.assertEqual(cart_page.func, user_cart)
