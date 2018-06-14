'''the tests should cover 
1. email is not blank
2. password is not blank
4. password is correct
5. the provided email is registered or existing
'''
from app import app
import unittest
from flask import request
import json
import sys


class TestLogIn(unittest.TestCase):
    
    def setup(self):
        app=flask.Flask(__name__)
    
    requestalldata = {"useremail": "somemail@mail","userpassword": "apassword"}
    requestnoemail = {"useremail": "","userpassword": "apassword"}
    requestnopassword = {"useremail": "nops@mail","userpassword": ""}
    requestnotexisting = {"useremail": "nops@mail","userpassword": "somps"}
    requestbadpassword = {"useremail": "mwangiwathiga@gmail.com","userpassword": "mypss"}
    requestshortpassword = {"useremail": "mwangiwathiga@gmail.com","userpassword": "ss"}
    requestsuccess = {"useremail": "mwangiwathiga@gmail.com","userpassword": "myps"}
    noemailds = {"useremail": "","userpassword": "myps"}
    nopsds = {"useremail": "mwangiwathiga@gmail.com","userpassword": ""}
    shortpsds = {"useremail": "mwangiwathiga@gmail.com","userpassword": ""}
    wrongpsds = {"useremail": "mwangiwathiga@gmail.com","userpassword": "wrong ps"}
    unregisteredemail = {"useremail": "mwangiwathigas@gmail.com","userpassword": "myps"}
    gooddataset = {"useremail": "mwangiwathiga@gmail.com","userpassword": "myps"}
    invalidemailds = {"useremail": "mwangiwathdiga@gmail.com","userpassword": "myps"}
    shortpsds = {"useremail": "mwangiwathdiga@gmail.com","userpassword": "ms"}


    def test_email_not_blank(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.requestnoemail),headers=headers)
            self.assertEqual(result.status_code,400)
            #self.assertEqual(result.json(), {"response": "email is required"})

    def test_password_not_blank(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.requestnopassword),headers=headers)
            self.assertEqual(result.status_code,400)
            #self.assertEqual(result.json(), {"response": "password is required"})

    def test_test_email_is_existing(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.requestnotexisting),headers=headers)
            self.assertEqual(result.status_code,400)
            #self.assertEqual(result.json(), {"response": "Unregistered email"})

    def test_password_is_correct(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.requestbadpassword),headers=headers)
            self.assertEqual(result.status_code,400)
            

    def test_password_is_short(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.requestshortpassword),headers=headers)
            self.assertEqual(result.status_code,400)
            
    def test_login_is_sussessful(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.requestsuccess),headers=headers)
            self.assertEqual(result.status_code,400)
            
    def test_good_dataset(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.gooddataset),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_no_email(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.noemailds),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_invalid_email(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.invalidemailds),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_no_ps(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.nopsds),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_short_ps(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.shortpsds),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_wrong_ps(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.wrongpsds),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_unreg_email(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.unregisteredemail),headers=headers)
        self.assertEqual(result.status_code,400)

    def test_vshortps_email(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.post('/api/v2/auth/login',data=json.dumps(self.shortpsds),headers=headers)
        self.assertEqual(result.status_code,400)


if __name__ == '__main__':
    unittest.main()
