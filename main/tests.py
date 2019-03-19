from django.test import TestCase
from converters.base_two import BaseTwo

class BaseTwoTest(TestCase):
    
    def convertTest(self):
        tenBase2 = BaseTwo().convert(10)
        self.assertEqual(tenBase2, '1010')
        
        hundredBase2 = BaseTwo().convert(100)
        self.assertEqual(hundredBase2, '1100100')
        
    def convertFailStringTest(self):
        try:
            BaseTwo().convert("test")
            self.fail()
        except:
            pass
        
    def convertFailFloatTest(self):
        try:
            BaseTwo().convert(1.5)
            self.fail()
        except:
            pass