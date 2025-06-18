from django.test import TestCase

class TestSenzillet(TestCase):
    def test_veritat_vertadera(self):
        self.assertTrue(True)

    def test_falsetat_falsa(self):
        self.assertFalse(False)

    def test_que_ja_no_falla(self):
        self.assertTrue(1==1)
