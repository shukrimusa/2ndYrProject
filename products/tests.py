from django.test import TestCase
from django.urls import reverse
from .models import Product, Category


class ProductTest(TestCase):
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
    # test categroy listing

    def test_category_listing(self):
        self.assertEqual(self.category.name, 'Mouse')

    # test product listing
    def test_product_listing(self):
        self.assertEqual(self.product.title, 'Pink Mouse')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.price, '22.00')
        self.assertEqual(self.product.stock, '3')

     # test product list view
    def test_product_list_view(self):
        response = self.client.get(reverse('products:all_products'))
        response1 = self.client.get(self.category.get_absolute_url())
        no_response = self.client.get('/products/dfdsf3eff4dfdfs43dfsdfsdf/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pink Mouse')
        self.assertTemplateUsed(response, 'products/category.html')
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response1.status_code, 200)
        self.assertContains(response1, 'Pink Mouse')
        self.assertTemplateUsed(response1, 'products/category.html')

     # test prodcut detail view
    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get(
            f'/products/{self.product.category.id}/sdfsfojlsdf45fsjdfsdffdf4532/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Pink Mouse')
        self.assertTemplateUsed(response, 'products/product.html')

    # test product create view
    def test_product_create_view(self):
        response = self.client.get(reverse('products:product_new'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_new.html')

    # test product edit view
    def test_product_edit_view(self):
        response = self.client.get(
            f'/products/product/{self.product.id}/edit/')
        no_response = self.client.get(
            '/products/product/erdf34efsdf3fs3fvxvdfsdf/edit/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'product_edit.html')
        self.assertContains(response, 'Edit Product')
        self.assertContains(response, '22.00')
        self.assertContains(response, '3')

    # test product delete view
    def test_product_delete_view(self):
        response = self.client.get(
            f'/products/product/{self.product.id}/delete/')
        no_response = self.client.get(
            '/products/product/dsfsd3434dsf234324dfsdf43r/delete/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(
            response, f'Are you sure you want to delete "{self.product.title}"?')
        self.assertContains(response, 'Delete Product')
        self.assertTemplateUsed(response, 'product_delete.html')
