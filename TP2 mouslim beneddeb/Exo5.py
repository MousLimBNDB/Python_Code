import re
import unittest

class TestPasswordValidator(unittest.TestCase):
    def test_short_password(self):
        self.assertEqual(password_validator("mslm"),False)
        
    def test_upper_case(self):
        self.assertEqual(password_validator("mslmbeneddeb"),False)

    def test_lower_case(self):
        self.assertEqual(password_validator("MMLKJLLKJLJHL"),False)
        
    def test_digit(self):
        self.assertEqual(password_validator("MLksjhklklj"),False)
        
    def test_special_characters(self):
        self.assertEqual(password_validator("MLOJSdkjz09968"),False)
        
    def test_correct(self):
        self.assertEqual(password_validator("Mouslim.061004"),True)
        
def password_validator(tompo):
    
    if len(tompo) < 8 : 
        print("the password is too short")
        return 0
    
    if not re.findall(r"[A-Z]",tompo):
        print("your password must Contain at least one uppercase letter")
        return 0
    
    if not re.findall(r"[a-z]",tompo):
        print("your password must Contain at least one lowercase letter")
        return 0
    
    if not re.findall(r"[0-9]",tompo):
        print("your password must Contain at least one digit")
        return 0

    if not re.findall(r'[!@#$%^&*.]', tompo):
        print("your password must Contain at least one special character (!@#$%^&*)")
        return False
    else:
        print("you have a strong password")
        return True

if __name__ == "__main__":
    unittest.main()
