from django.test import TestCase
from .models import Cart, CartItem
from products.models import Category, Product
from django.urls import reverse

# Create your tests here.


class CartTests(TestCase):
    def setUp(self):

        self.category = Category.objects.create(
            name='Mouse',
            image='{%%}'
        )

        self.product = Product.objects.create(
            title='Pink Mouse',
            category=self.category,
            price='22.00',
            stock='3',
            image="{%%}"
        )
        self.cart = Cart.objects.create(
           cart_id = 'dfkjoiufdj9joijldfjoidf'
    
        )

        self.cartItem = CartItem.objects.create(
            product = self.product,
            cart = self.cart,
            quantity = '2',
            active = 'True'
        )


    def test_Cart_listing(self):
        self.assertEqual(self.cart.cart_id, 'dfkjoiufdj9joijldfjoidf')

    def test_cart_item_listing(self):
        self.assertEqual(self.cartItem.product, self.product)
        self.assertEqual(self.cartItem.cart, self.cart)
        self.assertEqual(self.cartItem.quantity, '2')
        self.assertEqual(self.cartItem.active, 'True')
    
    def test_cart_detail_view(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
        self.assertContains(response, 'Your shopping cart')
    

