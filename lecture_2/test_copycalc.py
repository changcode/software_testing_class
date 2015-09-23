import unittest
import copycalc

class Test_000_Calculator(unittest.TestCase):

    def test_single_digit(self):
        i = 0
        for c in '0123456789':
            self.assertEqual(copycalc.evaluate(c),i)
            i = i + 1
    
    def test_multiple_digits(self):
        self.assertEqual(copycalc.evaluate('99999'),99999)
        self.assertEqual(copycalc.evaluate('12345'),12345)
        self.assertEqual(copycalc.evaluate('99999'),99999)
        self.assertEqual(copycalc.evaluate('99'),99)
        self.assertEqual(copycalc.evaluate('00'),00)

    def test_negative_numbers(self):
        self.assertEqual(copycalc.evaluate('-123'),-123)
        self.assertEqual(copycalc.evaluate('-1'),-1)
        self.assertEqual(copycalc.evaluate('0'),0)
        self.assertEqual(copycalc.evaluate('---123'),-123)

    def test_floating_numbers(self):
        self.assertEqual(copycalc.evaluate('123.456'),123.456)
        self.assertEqual(copycalc.evaluate('-123.456'),-123.456)

    def test_hexadecimal_numbers(self):
        self.assertEqual(copycalc.evaluate('0x00'),0)
        self.assertEqual(copycalc.evaluate('0x10'),16)
        self.assertEqual(copycalc.evaluate('0xff'),255)
        self.assertEqual(copycalc.evaluate('0xFF'),255)

if __name__ == "__main__":
    unittest.main()
