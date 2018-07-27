import unittest
from validate_phone import has_phone_number, get_phone_number, get_all_phone_numbers, hide_phone_numbers, format_phone_number

class TestValidatePhone(unittest.TestCase):

    def test_has_phone_number(self):
        self.assertEqual(has_phone_number("my phone number: 111-222-3333"), True)
        self.assertEqual(has_phone_number("please confirm your phone number: XXX-XXX-1234"), False)
    
    def test_get_phone_number(self):
        self.assertEqual(get_phone_number("please don't share this: 999-888-1234"),"999-888-1234")
        self.assertEqual(get_phone_number("please confirm your phone number: XXX-XXX-1234"), None)
    
    def test_get_all_phone_numbers(self):
        self.assertEqual(get_all_phone_numbers("234-609-1422, 350-802-0744,123-603-8762"),["234-609-1422", "350-802-0744", "123-603-8762"])
        self.assertEqual(get_all_phone_numbers("please confirm your phone number: XXX-XXX-1422"),[])

    def test_hide_phone_numbers(self):
        self.assertAlmostEqual(hide_phone_numbers("234-620-1422, 350-830-0744, 123-603-8762"), "XXX-XXX-1422, XXX-XXX-0744, XXX-XXX-8762")
        self.assertAlmostEqual(hide_phone_numbers("please confirm your phone number: XXX-XXX-1422"), "please confirm your phone number: XXX-XXX-1422")
        
    def test_format_phone_number(self):
        self.assertEqual(format_phone_number("3112223333, 350.820.0744, 123-630-8762"), "311-222-3333, 350-820-0744, 123-630-8762")
        self.assertEqual(format_phone_number("please confirm your phone number: 421142233"), "please confirm your phone number: 421142233")
        
if __name__ == '__main__':
    unittest.main()
