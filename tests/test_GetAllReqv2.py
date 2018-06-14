'''the tests should cover 
1. missing requests for user id
7. 
'''
from app import app
import unittest
from flask import request
import json
import sys


class TestLogIn(unittest.TestCase):
    
    def setup(self):
        
        pass

    useridgood={
        "userid":2
    }
    useridbad={
        "userid":8
    }

    def test_good_request(self):
            headers = {'content-type': 'application/json'}
            with app.test_client() as c:
                result =c.get('/api/v2/users/requests',data=json.dumps(self.useridgood),headers=headers)
            self.assertEqual(result.status_code,401)
    
    def test_bad_request(self):
            headers = {'content-type': 'application/json'}
            with app.test_client() as c:
                result =c.get('/api/v2/users/requests',data=json.dumps(self.useridbad),headers=headers)
            self.assertEqual(result.status_code,401)
    
    def test_JSONgood_request(self):
            headers = {'content-type': 'application/json'}
            with app.test_client() as c:
                result =c.get('/api/v2/users/requests',data=json.dumps(self.useridgood),headers=headers)
            self.assertEqual(result.status_code,401)
            


if __name__ == '__main__':
    unittest.main()
