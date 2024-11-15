from unittest import TestCase, main
# from decimal import Decimal

class Calc:
    def soma(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        else:
            raise Exception('insira somente numeros') 
    
    def sub(self, x, y):
        return x - y
    

class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()
    
    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 2), 4)
    
    def test_soma_neg(self):
        self.assertEqual(self.calc.soma(-2, -3), -5)
    
    # def test_soma_float(self):
    #     self.assertEqual(self.calc.soma(2.0, 1.0), 3.0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2,2), 0)

    def test_sub_float(self):
        self.assertEqual(self.calc.sub(2.0,2.0), 0)

    def test_soma_string(self):
        with self.assertRaises(Exception):
            self.calc.soma('Eduardo', 'jaber')
    
    def test_sub_string(self):
        with self.assertRaises(Exception):
            self.calc.sub('Eduardo', 'jaber')


if __name__ == '__main__':
    main()
    