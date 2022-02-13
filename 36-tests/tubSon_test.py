"""
#36-DARS.FUNKSIYANI TEKSHIRISH

Muallif:ANVARXON MAJIDOV AMALIYOT


"""
import unittest
from tubSonmi import tubSonmi


class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))

    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))


# if __name__ == '__main__':
# unittest.main()
unittest.main()
