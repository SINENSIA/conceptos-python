import unittest
from src.conceptos.saludar import di_hola

class TestMain(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(di_hola("World"), "Hola, World!")

if __name__ == "__main__":
    unittest.main()