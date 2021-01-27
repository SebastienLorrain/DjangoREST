
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

User = get_user_model()


def sample_user(email='test@admin.com', password='test123'):
    """Creates a sample user"""
    return User.objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@github.com'
        password = 'Testpass123'
        user = User.objects.create_user(
                                        email=email,
                                        password=password
                                        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that a new user has its email normalized"""
        email = 'test@GITHUB.COM'
        user = User.objects.create_user(email=email, password='test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password='test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser(
            email='admin@admin.com',
            password='test123'
            )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
                user=sample_user(),
                name='Vegan'
                )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
            )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
            )

        self.assertEqual(str(recipe), recipe.title)
