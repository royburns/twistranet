"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class WallTest(TestCase):

    def test_wall_creation(self):
        """
        We check a sample wall object creation.
        """
