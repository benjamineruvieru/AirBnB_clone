#!/usr/bin/python3
"""Unit test module for the user model."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test class for the User class."""

    def test_init(self):
        """Tests the initialization of the User class"""
        self.assertIsInstance(User(), BaseModel)
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertEqual(User().first_name, '')
        self.assertEqual(User().last_name, '')
        self.assertEqual(User().email, '')
        self.assertEqual(User().password, '')
        self.assertEqual(User('Ben').first_name, '')
        self.assertEqual(User('Pardon').last_name, '')
        self.assertEqual(User('bp@ymail.com').email, '')
        self.assertEqual(User('password123').password, '')
        self.assertEqual(User(first_name='Michael').first_name, 'Michael')
        self.assertEqual(User(last_name='Murphy').last_name, 'Murphy')
        self.assertEqual(User(email='mm@ymail.com').email, 'mm@ymail.com')
        self.assertEqual(User(password='12345').password, '12345')
        self.assertEqual(User('Steph', first_name='Simi').first_name, 'Simi')
        self.assertEqual(User('Eric', last_name='Castel').last_name, 'Castel')
        self.assertEqual(User('mo', email='n@rmail.com').email, 'n@rmail.com')
        self.assertEqual(User('12345', password='Nami').password, 'Nami')
