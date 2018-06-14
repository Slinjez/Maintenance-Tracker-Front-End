'''the tests should cover 
1. username is not blank
2. email is not blank
3. passwords are not blank
4. passwords match
'''
from app import app
import unittest
from flask import request
import json
import sys

class TestSignupV2(unittest.TestCase):
    requestalldata = {
        "username": "aname",
        "useremail": "somemail@mail",
        "userpassword": "apassword",
        "userpassword2": "apassword"
    }
    requestnousername = {
        "username": "",
        "useremail": "nameless@mail",
        "userpassword": "apassword",
        "userpassword2": "apassword"
    }
    requestnoemail = {
        "username": "no email guy",
        "useremail": "",
        "userpassword": "apassword",
        "userpassword2": "apassword"
    }
    requestnops1 = {
        "username": "no password 1 guy",
        "useremail": "ihatepasswords@mail",
        "userpassword": "",
        "userpassword2": "apassword"
    }
    requestnops2 = {
        "username": "no password 2 guy",
        "useremail": "ihatepasswords@mail",
        "userpassword": "apassword",
        "userpassword2": ""
    }
    requestmissmatchps = {
        "username": "forgetful guy",
        "useremail": "forget@mail",
        "userpassword": "apassword",
        "userpassword2": "forgot my password"
    }
    requestshortpassword = {
        "username": "forgetful guy",
        "useremail": "forget@mail",
        "userpassword": "apassword",
        "userpassword2": "forgot my password"
    }
    defaultuserid=""

    def setup(self):
        pass
        
        

    def test_unername_blank(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/signup',data=json.dumps(self.requestnousername),headers=headers)
            self.assertEqual(result.status_code,400)
    

    def test_email_not_blank(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v2/auth/signup',data=json.dumps(self.requestnoemail), headers=headers)
            self.assertEqual(result.status_code,400)
    
    def test_password1_not_blank(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v2/auth/signup',data=json.dumps(self.requestnops1), headers=headers)
            self.assertEqual(result.status_code,400)
    
    def test_password2_not_blank(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v2/auth/signup',data=json.dumps(self.requestnops2), headers=headers)
            self.assertEqual(result.status_code,400)
    
    def test_passwords_match(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v2/auth/signup',data=json.dumps(self.requestmissmatchps), headers=headers)
            self.assertEqual(result.status_code,400)
    
    def test_passwords_length(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v2/auth/signup',data=json.dumps(self.requestmissmatchps), headers=headers)
            self.assertEqual(result.status_code,400)


    
    
    
if __name__ == '__main__':
    unittest.main()