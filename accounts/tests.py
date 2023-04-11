from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class CustomUserTests(TestCase):

    def setUp(self):
        self.User = get_user_model()

    # create superuser test
    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username='shukrimusa',
            email='shukrimusa@gmail.com',
            age='24',
            password='xxxxx'
        )
        self.assertEqual(admin_user.username, 'shukrimusa')
        self.assertEqual(admin_user.email, 'shukrimusa@gmail.com')
        self.assertEqual(admin_user.age, '24')
        self.assertTrue(admin_user.is_superuser)

   # create user test
    def test_create_user(self):
        user = self.User.objects.create_user(
            username='John1234',
            email='shukrimusa@gmail.com',
            age='24',
            password="eeeeeee"
        )
        self.assertEqual(user.username, 'John1234')
        self.assertEqual(user.email, 'shukrimusa@gmail.com')
        self.assertEqual(user.age, '24')
        self.assertFalse(user.is_superuser)
